#!/usr/bin/env python3
"""Check literal LaTeX figures/tables, captions and assets without rendering."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
from check_manuscript import visible_source
import writing_metrics as wm


def braced(text,start):
    if start>=len(text) or text[start]!='{':return None
    depth=0
    for index in range(start,len(text)):
        if index and text[index-1]=='\\':continue
        if text[index]=='{':depth+=1
        if text[index]=='}':
            depth-=1
            if depth==0:return text[start+1:index]
    return None


def source_tree(main):
    root=main.resolve().parent;seen=set();parts=[];issues=[]
    def visit(path):
        path=path.resolve()
        if path in seen:return
        seen.add(path)
        if not path.is_relative_to(root):issues.append({'level':'WARN','message':'External input not inspected: '+str(path)});return
        if not path.exists():issues.append({'level':'ERROR','message':'Missing input: '+str(path)});return
        text=visible_source(path.read_text());parts.append((path,text))
        for m in re.finditer(r'\\(?:input|include)\s*\{([^{}]*)\}',text):
            name=m.group(1)
            if '\\' in name:issues.append({'level':'WARN','message':'Dynamic input is unverified: '+name});continue
            target=root/name
            if not target.suffix:target=target.with_suffix('.tex')
            visit(target)
    visit(main)
    return root,parts,issues


def inspect(main):
    root,parts,issues=source_tree(main);text='\n'.join(t for _,t in parts);floats=[]
    refs={x.strip() for m in re.finditer(r'\\(?:ref|cref|Cref|autoref)\*?\{([^{}]+)\}',text) for x in m.group(1).split(',')}
    graphicdirs=[root]
    for m in re.finditer(r'\\graphicspath\s*\{',text):
        value=braced(text,m.end()-1)
        if value:
            for name in re.findall(r'\{([^{}]+)\}',value):graphicdirs.append(root/name)
    for path,body in parts:
        for m in re.finditer(r'\\begin\{(figure\*?|table\*?)\}(.*?)\\end\{\1\}',body,re.S):
            env,content=m.groups();labels=re.findall(r'\\label\{([^{}]+)\}',content)
            captionmatch=re.search(r'\\caption(?:\[[^\]]*\])?\s*\{',content)
            caption=braced(content,captionmatch.end()-1) if captionmatch else None
            row={'file':str(path),'kind':env,'labels':labels,'caption_words':len(wm.WORD.findall(wm.plain(caption))) if caption else 0,'assets':[]}
            if not labels:issues.append({'level':'ERROR','message':'Float without label: '+str(path)})
            for label in labels:
                if label not in refs:issues.append({'level':'WARN','message':'Float not referenced in literal text: '+label})
            if caption is None:issues.append({'level':'ERROR','message':'Float without readable caption: '+str(labels)})
            if re.search(r'TODO|placeholder|\\FigPlan',content,re.I):issues.append({'level':'NOTE','message':'Pending figure/table content: '+str(labels)})
            for asset in re.finditer(r'\\includegraphics(?:\[[^\]]*\])?\s*\{([^{}]+)\}',content):
                name=asset.group(1);row['assets'].append(name)
                if '\\' in name:issues.append({'level':'WARN','message':'Dynamic graphic path is unverified: '+name});continue
                candidates=[directory/name for directory in graphicdirs]
                found=[p for base in candidates for p in ([base] if base.suffix else [base.with_suffix(ext) for ext in ['.pdf','.svg','.png','.jpg','.jpeg','.eps']]) if p.is_file()]
                if not found:issues.append({'level':'ERROR','message':'Missing graphic: '+name})
                elif found[0].suffix.lower() in {'.png','.jpg','.jpeg'}:
                    issues.append({'level':'NOTE','message':'Raster image; inspect whether this is a legitimate photo or a plot better exported as vector: '+name})
            floats.append(row)
    profile_path=Path(__file__).resolve().parents[1]/'data/corpus-stats.json'
    if profile_path.exists():
        profile=json.loads(profile_path.read_text()).get('figure1',{}).get('caption_metrics',{}).get('word_count')
        first=next((r for r in floats if r['kind'].startswith('figure')),None)
        if first and profile and (first['caption_words']<profile['p10'] or first['caption_words']>profile['p90']):
            issues.append({'level':'NOTE','message':f'First caption length {first["caption_words"]} is outside development Figure1 p10-p90 [{profile["p10"]:.1f}, {profile["p90"]:.1f}], n={profile["n"]}; advisory only.'})
    for macro in re.finditer(r'\\newcommand\s*\{\\[A-Za-z]+\}(?:\[[^\]]*\])?\s*\{',text):
        definition=braced(text,macro.end()-1) or ''
        if re.search(r'\\begin\{(?:figure|table)',definition):issues.append({'level':'WARN','message':'Float macro requires manual expansion; literal-source heuristic only.'})
    return {'floats':floats,'issues':issues,'limits':'No rendering or layout verification. Axis units, scientific content, visual fidelity and macro-generated figures need inspection.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('main',type=Path);p.add_argument('--json',action='store_true')
    a=p.parse_args();r=inspect(a.main)
    if a.json:print(json.dumps(r,indent=2))
    else:
        for issue in r['issues']:print(issue['level']+': '+issue['message'])
        print(f"Inspected {len(r['floats'])} literal figures/tables. "+r['limits'])
    return int(any(i['level']=='ERROR' for i in r['issues']))

if __name__=='__main__':raise SystemExit(main())
