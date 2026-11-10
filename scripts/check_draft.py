#!/usr/bin/env python3
"""Advisory rhetoric/style and evidence checks; neither acceptance nor truth scoring."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import writing_metrics as wm
from check_manuscript import visible_source
from style_metrics import report


def inspect(path,section=None,brief=None,final=False):
    raw=path.read_text(encoding='utf-8')
    if path.suffix.lower()=='.tex':raw=visible_source(raw)
    text=wm.plain(raw);issues=[]
    def add(level,kind,description):issues.append({'level':level,'kind':kind,'message':description})
    if re.search(r'\bTODO\b|\bTBD\b|\\(?:todo|draftnote)\b',raw,re.I):
        add('ERROR' if final else 'NOTE','pending','Draft contains explicitly pending text; replace before final submission.')
    for pattern,message in [
      (r'has attracted (?:increasing|growing) attention','Opening states popularity rather than the concrete research problem.'),
      (r'extensive experiments (?:show|demonstrate) (?:the )?(?:effectiveness|superiority)','Replace generic evaluation praise with the supported finding.'),
      (r'\b(?:paradigm shift|revolutionary|unprecedented)\b','Check whether this evaluative claim has concrete support.'),
      (r'\b(?:first|all workloads|always|guarantees?|proves?)\b','Inspect the scope, proof assumptions, or literature evidence for this strong claim.'),
      (r'\b(?:supplied|provided) (?:results|facts|notes|input)\b','Remove author-workflow narration from manuscript prose.')]:
        if re.search(pattern,text,re.I):add('WARN','rhetoric',message)
    metrics=report(path,section)
    for key,c in metrics['comparisons'].items():
        if c['outside_p10_p90']:
            add('NOTE','corpus_distribution',f'{key}={c["value"]:.2f} is outside development p10-p90 [{c["p10"]:.2f}, {c["p90"]:.2f}] (n={c["n"]}); review in context, not a mandatory correction.')
    if brief is not None:
        allowed={x.replace(',','') for x in wm.NUMBER.findall(brief)}
        found={x.replace(',','') for x in wm.NUMBER.findall(text)}
        extra=sorted(found-allowed)
        if extra:add('WARN','numeric_provenance','Numbers absent from the brief require manual source/derivation checking: '+', '.join(extra))
    return {'file':str(path),'issues':issues,'style':metrics,
      'limits':'No blanket ban on scope qualifiers, hypotheses or punctuation; lexical checks cannot verify mechanism or scientific truth.'}


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('files',type=Path,nargs='+');p.add_argument('--section',choices=['abstract','introduction'])
    p.add_argument('--brief',type=Path);p.add_argument('--final',action='store_true');p.add_argument('--json',action='store_true')
    a=p.parse_args();brief=a.brief.read_text() if a.brief else None
    rows=[inspect(f,a.section,brief,a.final) for f in a.files]
    if a.json:print(json.dumps(rows,indent=2))
    else:
        for row in rows:
            for issue in row['issues']:print(f'{issue["level"]} {row["file"]}: {issue["message"]}')
            print(row['limits'])
    return 1 if any(i['level']=='ERROR' for r in rows for i in r['issues']) else 0

if __name__=='__main__':raise SystemExit(main())
