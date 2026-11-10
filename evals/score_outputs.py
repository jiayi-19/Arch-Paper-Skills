#!/usr/bin/env python3
"""Reproduce source-only held-out output metrics and auditable rubric aggregation."""
from __future__ import annotations
import argparse
from collections import Counter
import difflib
import json
from pathlib import Path
import re
import sys
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
import writing_metrics as wm


def tokens(text):return re.findall(r'[a-z0-9]+',text.lower())
def ngrams(values,n=8):return {' '.join(values[i:i+n]) for i in range(max(0,len(values)-n+1))}


def measure_case(brief,output,reference=None):
    abstract=output['abstract'];intro=output['introduction']
    if not isinstance(abstract,str) or not isinstance(intro,list) or not all(isinstance(x,str) for x in intro):raise ValueError('Expected abstract string and introduction paragraph list')
    allowed_text=json.dumps(brief,ensure_ascii=False)
    text=abstract+'\n\n'+'\n\n'.join(intro)
    allowed={x.replace(',','') for x in wm.NUMBER.findall(allowed_text)}
    found={x.replace(',','') for x in wm.NUMBER.findall(wm.plain(text))}
    keys={r['key'] for r in brief.get('bibliography',[])}
    used={key.strip() for m in re.finditer(r'\\cite\w*\*?(?:\[[^\]]*\])*\{([^{}]+)\}',text) for key in m.group(1).split(',')}
    low,high=brief['task']['abstract_words']
    result={'case_id':brief['case_id'],'abstract_metrics':wm.measure(abstract),'introduction_metrics':wm.measure('\n\n'.join(intro)),
      'introduction_paragraphs':len(intro),'abstract_length_in_requested_range':low<=len(wm.WORD.findall(abstract))<=high,
      'expected_introduction_paragraphs':brief['task']['introduction_paragraphs'],
      'unverified_numeric_tokens':sorted(found-allowed),'unknown_citation_keys':sorted(used-keys),
      'pending_markers':len(re.findall(r'\bTODO\b|\bTBD\b|\\todo',text,re.I)),
      'note':'Unverified tokens are audit leads, not automatic fabrication judgments; known numbers can also be misused.'}
    if reference is not None:
        output_tokens=tokens(text);ref_tokens=tokens(reference);prompt_grams=ngrams(tokens(allowed_text))
        match=difflib.SequenceMatcher(None,output_tokens,ref_tokens,autojunk=False).find_longest_match()
        result['source_overlap']={'eightgram_matches_not_in_brief':len((ngrams(output_tokens)&ngrams(ref_tokens))-prompt_grams),
          'longest_contiguous_word_run':match.size,'interpretation':'Overlap is a copying/memorization warning, not proof of source exposure or original authorship.'}
    return result


def aggregate_grade(case_key,grade,key):
    weights={r['metric_id']:r['weight'] for r in key['rubric']}
    factweights={r['fact_id']:r['coverage_weight'] for r in case_key['fact_coverage']}
    coverage=grade['fact_coverage']
    if len({r['fact_id'] for r in coverage})!=len(coverage) or {r['fact_id'] for r in coverage}!=set(factweights):raise ValueError('Grader must cover each fact exactly once')
    if any(r['coverage_level'] not in {0,.5,1} for r in coverage):raise ValueError('Invalid coverage level')
    fraction=sum(r['coverage_level']*factweights[r['fact_id']] for r in coverage)/sum(factweights.values())
    scores={'fact_fidelity':weights['fact_fidelity']*fraction,'unsupported_numbers':weights['unsupported_numbers'],'baselines_scope':weights['baselines_scope']}
    for metric in weights:
        if metric in scores:continue
        value=grade['metric_raw_scores'][metric]
        if not isinstance(value,(int,float)) or not 0<=value<=5:raise ValueError('Quality scores must be 0-5')
        scores[metric]=weights[metric]*value/5
    rules={r['rule_id']:r for r in key['penalty_rules']};penalties=Counter()
    for row in grade.get('penalties',[]):
        if row['rule_id'] not in rules or type(row['count'])!=int or row['count']<0 or not row.get('evidence'):raise ValueError('Invalid/unsupported penalty')
        penalties[row['rule_id']]+=row['count']
    applied=[]
    for name,count in penalties.items():
        rule=rules[name];points=min(count*rule['points_per_occurrence'],rule['metric_penalty_cap'])
        scores[rule['metric_id']]=max(0,scores[rule['metric_id']]-points)
        applied.append({'rule_id':name,'count':count,'points':points,'metric_id':rule['metric_id']})
    return {'case_id':case_key['case_id'],'coverage_fraction':fraction,'metric_scores':scores,'total':sum(scores.values()),
      'penalties':applied,'fatal_fabrication':bool(grade.get('fatal_fabrication')),
      'interpretation':'One model-judged writing task; no predeclared pass threshold or statistical superiority claim.'}


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--briefs',required=True,type=Path);p.add_argument('--outputs',required=True,type=Path)
    p.add_argument('--references',type=Path,help='Private {case_id: original_text_path} map; source text never copied to report')
    p.add_argument('--key',type=Path);p.add_argument('--grades',type=Path);p.add_argument('--out',type=Path)
    a=p.parse_args();briefs=json.loads(a.briefs.read_text())['cases'];refs=json.loads(a.references.read_text()) if a.references else {}
    if not isinstance(refs,dict):p.error('--references expects a {case_id: text_path} map, not a source metadata list')
    if a.references and any(b['case_id'] not in refs for b in briefs):p.error('Reference mapping must include every requested case')
    rows=[]
    for brief in briefs:
        output=json.loads((a.outputs/(brief['case_id']+'.json')).read_text())
        if output['case_id']!=brief['case_id']:raise ValueError('Output case identity mismatch')
        rows.append(measure_case(brief,output,Path(refs[brief['case_id']]).read_text() if brief['case_id'] in refs else None))
    result={'mechanical_metrics':rows,'grading':None}
    if bool(a.key)!=bool(a.grades):p.error('--key and --grades must be supplied together')
    if a.key:
        key=json.loads(a.key.read_text());grades=json.loads(a.grades.read_text())
        if isinstance(grades,dict):grades=grades['cases']
        by_id={r['case_id']:r for r in grades}
        result['grading']=sorted([aggregate_grade(k,by_id[k['case_id']],key) for k in key['cases']],key=lambda r:r['case_id'])
    text=json.dumps(result,indent=2,ensure_ascii=False)+'\n'
    if a.out:a.out.write_text(text)
    else:print(text)

if __name__=='__main__':main()
