#!/usr/bin/env python3
"""Measure draft prose against the declared development corpus, with advisory percentiles."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import writing_metrics as wm
from check_manuscript import visible_source

ROOT=Path(__file__).resolve().parents[1]


def report(path, section=None, profile=None):
    text=path.read_text(encoding='utf-8')
    if path.suffix.lower()=='.tex':text=visible_source(text)
    metrics=wm.measure(text)
    result={'file':str(path),'section':section,'metrics':metrics,
      'measurement_note':'Draft sentence boundaries and grammatical counts are heuristics; development sentence boundaries were source-inspected.',
      'profile':None,'comparisons':{}}
    if profile is None:
        profile_path=ROOT/'data/corpus-stats.json'
        profile=json.loads(profile_path.read_text()) if profile_path.exists() else None
    if profile and section in profile['sections']:
        item=profile['sections'][section]
        result['profile']={'version':profile['version'],'split':profile['split'],'n':item['papers']}
        for key,value in metrics.items():
            if key not in item['metrics']:continue
            samples=[m[key] for m in item.get('samples',{}).values()]
            reference=item['metrics'][key]
            result['comparisons'][key]={'value':value,**reference,
              'empirical_percentile':100*sum(v<=value for v in samples)/len(samples) if samples else None,
              'outside_p10_p90':value<reference['p10'] or value>reference['p90']}
    return result


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('files',type=Path,nargs='+')
    p.add_argument('--section',choices=['abstract','introduction'])
    p.add_argument('--json',action='store_true')
    a=p.parse_args();rows=[report(path,a.section) for path in a.files]
    if a.json:print(json.dumps(rows,indent=2))
    else:
        for r in rows:
            print(r['file']);print(r['measurement_note'])
            for key,value in r['metrics'].items():
                c=r['comparisons'].get(key)
                suffix=(f" | development n={c['n']}, p10={c['p10']:.2f}, median={c['p50']:.2f}, p90={c['p90']:.2f}; percentile={c['empirical_percentile']:.1f}" if c and c['empirical_percentile'] is not None else '')
                print(f'{key}: {value:.2f}{suffix}')
    return 0

if __name__=='__main__':raise SystemExit(main())
