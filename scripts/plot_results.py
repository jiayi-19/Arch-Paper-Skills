#!/usr/bin/env python3
"""Draw vector architecture plots from explicit CSV data; no invented missing values."""
from __future__ import annotations
import argparse
import csv
import json
import math
from pathlib import Path


def load(path):
    with path.open(newline='') as f:raw=list(csv.DictReader(f))
    rows=[];seen=set()
    for row in raw:
        if not all(k in row for k in ['case','method','value','status']):raise ValueError('CSV requires case,method,value,status')
        key=row['case'],row['method']
        if key in seen:raise ValueError('Duplicate case/method')
        seen.add(key)
        if row['status'] not in {'valid','invalid','not_measured'}:raise ValueError('Unknown measurement status')
        value=float(row['value']) if row['value'].strip() else None
        if value is not None and (not math.isfinite(value) or value<0):raise ValueError('Values must be finite and nonnegative')
        if row['status']=='valid' and value is None:raise ValueError('Valid result lacks a value')
        if row['status']!='valid' and value is not None:raise ValueError('Unavailable result must not carry a numeric fallback')
        resource=float(row['resource']) if row.get('resource','').strip() else None
        if resource is not None and (not math.isfinite(resource) or resource<0):raise ValueError('Resource must be finite and nonnegative')
        rows.append({**row,'value':value,'source_value':value,'resource':resource})
    if not rows:raise ValueError('Empty data')
    return rows


def plot(args):
    import matplotlib
    matplotlib.use('Agg')
    import matplotlib.pyplot as plt
    rows=load(args.csv);cases=list(dict.fromkeys(r['case'] for r in rows));methods=list(dict.fromkeys(r['method'] for r in rows))
    if args.kind!='pareto':
        expected={(c,m) for c in cases for m in methods}
        if {(r['case'],r['method']) for r in rows}!=expected:raise ValueError('Represent every case/method; use explicit unavailable status instead of omitting failures')
    if args.normalize_to:
        if args.kind in {'stacked','pareto'}:raise ValueError('Normalization is defined only for bars/line')
        for case in cases:
            baseline=next((r for r in rows if r['case']==case and r['method']==args.normalize_to),None)
            if not baseline or baseline['value'] is None or baseline['value']<=0:raise ValueError('Each normalization baseline must be valid and positive')
            base=baseline['value']
            for row in rows:
                if row['case']==case and row['value'] is not None:row['value']/=base
    style=Path(__file__).resolve().parents[1]/'assets/figures/architecture.mplstyle'
    plt.style.use(str(style));fig,ax=plt.subplots(figsize=(3.35 if args.width=='column' else 6.9,2.35))
    colors=['#0072B2','#D55E00','#009E73','#CC79A7','#E69F00','#56B4E9']
    for mi,method in enumerate(methods):
        entries=[next(r for r in rows if r['case']==c and r['method']==method) for c in cases] if args.kind!='pareto' else [r for r in rows if r['method']==method]
        values=[r['value'] if r['value'] is not None else math.nan for r in entries]
        color=colors[mi%len(colors)]
        if args.kind=='bars':
            width=.8/len(methods);positions=[i-.4+width*(mi+.5) for i in range(len(cases))]
            ax.bar(positions,values,width,label=method,color=color,hatch=['','//','xx','..'][mi%4])
            for x,row in zip(positions,entries):
                if row['value'] is None:ax.text(x,.02,row['status'],transform=ax.get_xaxis_transform(),rotation=90,fontsize=6,ha='center',va='bottom')
        elif args.kind=='line':
            ax.plot(range(len(cases)),values,marker=['o','s','^','D'][mi%4],label=method,color=color)
            for x,row in enumerate(entries):
                if row['value'] is None:ax.text(x,.02,method+': '+row['status'],transform=ax.get_xaxis_transform(),rotation=90,fontsize=6)
        elif args.kind=='stacked':
            if any(r['value'] is None for r in entries):raise ValueError('Stacked decompositions require measured complete components')
            bottoms=[sum(r['value'] for r in rows if r['case']==c and methods.index(r['method'])<mi) for c in cases]
            ax.bar(range(len(cases)),values,bottom=bottoms,label=method,color=color)
        else:
            valid=[r for r in entries if r['value'] is not None]
            if any(r['resource'] is None for r in valid):raise ValueError('Pareto plot requires resource for every valid point')
            ax.scatter([r['resource'] for r in valid],[r['value'] for r in valid],label=method,color=color,marker=['o','s','^','D'][mi%4])
            for row in valid:ax.annotate(row['case'],(row['resource'],row['value']),fontsize=6)
    if args.kind!='pareto':ax.set_xticks(range(len(cases)),cases)
    else:ax.set_xlabel(args.x_label or 'Resource (declare units)')
    ax.set_ylabel(args.y_label);ax.legend(frameon=False)
    if args.normalize_to:ax.axhline(1,color='0.5',linewidth=.6,linestyle=':')
    if args.data_kind=='synthetic':fig.text(.5,1,'SYNTHETIC EXAMPLE — NOT RESEARCH RESULTS',ha='center',fontsize=7)
    if args.out.suffix.lower() not in {'.pdf','.svg'}:raise ValueError('Use vector .pdf or .svg output')
    args.out.parent.mkdir(parents=True,exist_ok=True)
    fig.savefig(args.out);plt.close(fig)
    manifest={'input':str(args.csv),'output':str(args.out),'data_kind':args.data_kind,'kind':args.kind,
      'normalization':'candidate/baseline' if args.normalize_to else None,'baseline':args.normalize_to,
      'y_label':args.y_label,'missing_results':sum(r['value'] is None for r in rows),'source_rows':len(rows),
      'plotted_rows':[{'case':r['case'],'method':r['method'],'source_value':r['source_value'],'plotted_value':r['value'],'status':r['status']} for r in rows]}
    args.out.with_suffix(args.out.suffix+'.json').write_text(json.dumps(manifest,indent=2)+'\n')
    return manifest


def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('csv',type=Path);p.add_argument('--out',required=True,type=Path)
    p.add_argument('--kind',choices=['bars','line','stacked','pareto'],default='bars');p.add_argument('--y-label',required=True)
    p.add_argument('--x-label');p.add_argument('--width',choices=['column','full'],default='column')
    p.add_argument('--data-kind',choices=['measured','modeled','synthetic'],required=True);p.add_argument('--normalize-to')
    a=p.parse_args()
    try:print(json.dumps(plot(a),indent=2))
    except (ValueError,ImportError) as e:p.error(str(e))

if __name__=='__main__':main()
