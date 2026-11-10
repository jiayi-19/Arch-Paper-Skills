#!/usr/bin/env python3
"""Convert offline architecture-intake.v2 JSON to a sourced brief and optional ledger."""
from __future__ import annotations
import argparse
import json
from pathlib import Path


def convert(data):
    if data.get('schema')!='architecture-intake.v2':raise ValueError('Expected architecture-intake.v2')
    project=data.get('project',{});research=data.get('research',{});evidence=data.get('evidence',[])
    if not isinstance(project,dict) or not isinstance(research,dict) or not isinstance(evidence,list):raise ValueError('Invalid intake object types')
    missing=[key for key in ['problem','mechanism'] if not research.get(key)]
    lines=['# Writing brief: '+(project.get('title') or 'Untitled research'),'']
    for key in ['venue','paper_type','sections','word_budget']:
        value=project.get(key)
        if value:lines.append(f'- {key}: {value}')
    lines+=['','## Research argument','']
    for key in ['problem','prior_approach','limitation','reason','insight','mechanism','closest_work','scope']:
        value=research.get(key)
        lines.append('### '+key.replace('_',' ').title())
        lines.append((json.dumps(value,ensure_ascii=False,indent=2) if isinstance(value,(list,dict)) else str(value)) if value else '[TODO: '+key+']')
        lines.append('')
    lines+=['## Claim and evidence map','']
    ids=set()
    for row in evidence:
        if not isinstance(row,dict) or not row.get('id') or row['id'] in ids:raise ValueError('Evidence IDs must be present and unique')
        ids.add(row['id'])
        if row.get('status') not in ['measured','modeled','derived','planned','unavailable']:raise ValueError('Unknown evidence status')
        lines+=['### '+row['id'],json.dumps(row,ensure_ascii=False,indent=2),'']
    if not evidence:lines+=['[TODO: evidence; do not invent a completed result]','']
    lines+=['## Figure plan',json.dumps(data.get('figures',[]),ensure_ascii=False,indent=2),'',
      '## Missing core fields',', '.join(missing) if missing else 'None','',
      'Source facts, hypotheses and planned measurements remain distinct. Missing results do not prevent drafting supported method text.']
    ledger={'version':'architecture-claim-ledger.v2','claims':evidence,'source':'User intake; values require source verification, not automatic truth certification'}
    return '\n'.join(lines)+'\n',ledger,missing


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('input',type=Path)
    p.add_argument('--out',type=Path);p.add_argument('--ledger',type=Path);p.add_argument('--bib',type=Path)
    a=p.parse_args()
    try:
        data=json.loads(a.input.read_text());text,ledger,missing=convert(data)
    except (ValueError,KeyError,TypeError) as e:p.error(str(e))
    if a.out:a.out.write_text(text)
    else:print(text)
    if a.ledger:a.ledger.write_text(json.dumps(ledger,indent=2)+'\n')
    if a.bib and data.get('bibliography'):a.bib.write_text(data['bibliography'].rstrip()+'\n')
    return 2 if missing else 0

if __name__=='__main__':raise SystemExit(main())
