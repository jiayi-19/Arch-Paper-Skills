#!/usr/bin/env python3
"""Create randomized A/B writing candidates, with condition mapping kept separately."""
import argparse
import json
from pathlib import Path
import random


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--control',type=Path,required=True);p.add_argument('--skill',type=Path,required=True)
    p.add_argument('--out',type=Path,required=True);p.add_argument('--mapping',type=Path,required=True);p.add_argument('--seed',type=int,default=29)
    a=p.parse_args()
    if a.out.exists():p.error('Use a new output directory')
    c={p.stem:p for p in a.control.glob('*.json')};s={p.stem:p for p in a.skill.glob('*.json')}
    if not c or c.keys()!=s.keys():p.error('Conditions must cover the same nonempty case set')
    a.out.mkdir(parents=True);rng=random.Random(a.seed);mapping={}
    for case_id in sorted(c):
        arms=[('control',c[case_id]),('skill',s[case_id])];rng.shuffle(arms)
        candidates=[];mapping[case_id]={}
        for label,(condition,path) in zip(['A','B'],arms):
            row=json.loads(path.read_text());candidates.append({'label':label,'abstract':row['abstract'],'introduction':row['introduction']})
            mapping[case_id][label]=condition
        (a.out/(case_id+'.json')).write_text(json.dumps({'case_id':case_id,'candidates':candidates},indent=2)+'\n')
    a.mapping.write_text(json.dumps({'seed':a.seed,'mapping':mapping},indent=2)+'\n')
    print('Prepared blinded candidate files. Keep the condition mapping from the judge until grades are saved.')

if __name__=='__main__':main()
