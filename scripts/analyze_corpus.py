#!/usr/bin/env python3
"""Build text-free public annotation data and development-only empirical profiles."""
from __future__ import annotations
import argparse
from collections import Counter, defaultdict
import json
from pathlib import Path
import writing_metrics as wm

LABELS={'context','problem','prior_work','limitation','observation','insight','mechanism','methodology','result','contribution','scope','roadmap'}
PARAGRAPHS={'setting','gap','prior_work','insight','approach','evidence','contributions','scope','roadmap','mixed'}


def build(private, repo):
    split=json.loads((repo/'data/splits.json').read_text())
    corpus={r['id']:r for r in json.loads((repo/'references/corpus.json').read_text())}
    expected=set(split['development_ids'])
    actual={p.stem for p in private.glob('*.json')}
    if actual!=expected:raise ValueError(f'Private annotation set mismatch; missing={sorted(expected-actual)}, extra={sorted(actual-expected)}')
    records=[];sections=defaultdict(list);coverage=[];figure_samples=[]
    for paper_id in sorted(expected):
        raw=json.loads((private/(paper_id+'.json')).read_text())
        if raw['paper_id']!=paper_id:raise ValueError('Paper identity mismatch')
        if raw['annotation_version']!='architecture-moves.v1':raise ValueError('Unknown annotation version')
        seen=set();out={'paper_id':paper_id,'paper_url':corpus[paper_id]['paper_url'],
          'annotation_method':'Model-agent source reading with deterministic structural checks; not human ground truth',
          'source_version':corpus[paper_id].get('version_note',corpus[paper_id].get('source_note','Recorded corpus PDF')),
          'cleaning_notes':raw.get('cleaning_notes',[]),'sections':[]}
        for section in raw['sections']:
            name=section['name']
            if name not in {'abstract','introduction'} or name in seen:raise ValueError('Invalid/duplicate section')
            seen.add(name);offset=0;paragraphs=[];all_sentences=[];all_text=[]
            for pi,para in enumerate(section['paragraphs'],1):
                if para['role'] not in PARAGRAPHS:raise ValueError(f'Bad paragraph role: {paper_id} {para["role"]}')
                page0,page1=para['pdf_page_start'],para['pdf_page_end']
                if type(page0)!=int or type(page1)!=int or not 1<=page0<=page1:raise ValueError('Bad source pages')
                ps=[];joined=[];start=offset
                for si,sentence in enumerate(para['sentences'],1):
                    text=' '.join(sentence['text'].split())
                    if not text:raise ValueError('Empty source sentence')
                    primary=sentence['primary'];secondary=sentence.get('secondary',[])
                    if primary not in LABELS or any(x not in LABELS for x in secondary):raise ValueError(f'Bad sentence role: {paper_id} {primary}/{secondary}')
                    ps.append({'sentence_index':si,'start':offset,'end':offset+len(text),
                      'primary':primary,'secondary':secondary,'word_count':len(wm.WORD.findall(wm.plain(text)))})
                    offset+=len(text)+1;joined.append(text);all_sentences.append(text)
                paragraph_text=' '.join(joined)
                if not joined:raise ValueError('Empty paragraph')
                paragraphs.append({'paragraph_index':pi,'start':start,'end':offset-1,
                  'pdf_page_start':page0,'pdf_page_end':page1,'subsection':para.get('subsection',''),
                  'role':para['role'],'summary':para['summary'],'sentences':ps})
                offset+=1;all_text.append(paragraph_text)
            if not all_sentences:raise ValueError('Empty section')
            metrics=wm.measure('\n\n'.join(all_text),all_sentences)
            metrics['paragraph_count']=len(paragraphs)
            public={'name':name,'complete':bool(section['complete']),
              'offset_convention':'Zero-based Unicode codepoints in normalized section: sentences joined by one space, paragraphs by two newlines; end exclusive',
              'metrics':metrics,'paragraphs':paragraphs}
            out['sections'].append(public)
            if section['complete']:sections[name].append((paper_id,public))
            coverage.append({'paper_id':paper_id,'section':name,'complete':bool(section['complete']),
              'paragraphs':len(paragraphs),'sentences':len(all_sentences),'words':metrics['word_count']})
        if seen!={'abstract','introduction'}:raise ValueError(f'Missing target section: {paper_id}')
        figure=raw.get('figure1')
        if figure and figure.get('caption'):
            caption_metrics=wm.measure(figure['caption'])
            fig={'paper_id':paper_id,'pdf_page':figure['pdf_page'],'kind':figure['kind'],
              'panels':figure.get('panels'),'full_width':figure.get('full_width'),
              'notes':figure.get('notes',''),'metrics':caption_metrics}
            out['figure1']=fig;figure_samples.append(fig)
        records.append(out)
    output=repo/'data/annotations';output.mkdir(exist_ok=True,parents=True)
    for row in records:(output/(row['paper_id']+'.json')).write_text(json.dumps(row,indent=2,ensure_ascii=False)+'\n')
    return summarize(records,repo)


def summarize(records,repo):
    sections=defaultdict(list);coverage=[];figure_samples=[]
    for row in records:
        for section in row['sections']:
            name=section['name']
            if section['complete']:sections[name].append((row['paper_id'],section))
            coverage.append({'paper_id':row['paper_id'],'section':name,'complete':section['complete'],
              'paragraphs':len(section['paragraphs']),'sentences':sum(len(p['sentences']) for p in section['paragraphs']),
              'words':section['metrics']['word_count']})
        if row.get('figure1'):figure_samples.append(row['figure1'])
    stats={'version':'architecture-style-profile.v2','split':'development only',
      'selection':f'Curated {len(records)} papers, not a random conference population',
      'annotation_method':'Model-agent labeling of complete abstract/introduction passages; manual source inspection by model agents, not human labels',
      'quantiles':'Linear interpolation at (n-1)*q over per-paper section metrics; complete sections only',
      'metric_definitions':'scripts/writing_metrics.py; passive and trailing-participial counts are lexical proxies',
      'coverage':coverage,'sections':{},'figure1':{'samples':figure_samples,'kind_counts':dict(Counter(x['kind'] for x in figure_samples)), 'caption_metrics':{key:wm.distribution([x['metrics'][key] for x in figure_samples]) for key in (figure_samples[0]['metrics'] if figure_samples else [])}}}
    for name,items in sections.items():
        numeric={key:wm.distribution([s['metrics'][key] for _,s in items]) for key in items[0][1]['metrics']}
        roles=Counter();proles=Counter();transitions=Counter();arcs=[]
        for paper_id,s in items:
            sequence=[]
            for p in s['paragraphs']:
                proles[p['role']]+=1
                sequence.extend(x['primary'] for x in p['sentences'])
            roles.update(sequence)
            transitions.update(a+' -> '+b for a,b in zip(sequence,sequence[1:]))
            collapsed=[x for i,x in enumerate(sequence) if i==0 or x!=sequence[i-1]]
            arcs.append({'paper_id':paper_id,'sentence_move_sequence':sequence,'collapsed_sequence':collapsed,
              'paragraph_roles':[p['role'] for p in s['paragraphs']]})
        stats['sections'][name]={'papers':len(items),'metrics':numeric,'samples':{pid:s['metrics'] for pid,s in items},'sentence_roles':dict(roles),
          'paragraph_roles':dict(proles),'move_transitions':dict(transitions),'paper_arcs':arcs}
    (repo/'data/corpus-stats.json').write_text(json.dumps(stats,indent=2)+'\n')
    return stats


def main():
    p=argparse.ArgumentParser(description=__doc__)
    mode=p.add_mutually_exclusive_group(required=True)
    mode.add_argument('--private-passages',type=Path)
    mode.add_argument('--from-public',action='store_true',help='Reproduce summaries from text-free published annotation records')
    p.add_argument('--repo',type=Path,default=Path(__file__).resolve().parents[1])
    a=p.parse_args()
    if a.from_public:
        ids=json.loads((a.repo/'data/splits.json').read_text())['development_ids']
        records=[json.loads((a.repo/'data/annotations'/(pid+'.json')).read_text()) for pid in sorted(ids)]
        s=summarize(records,a.repo)
    else:s=build(a.private_passages,a.repo)
    print(json.dumps({'papers':len({r['paper_id'] for r in s['coverage']}),'sections':{k:v['papers'] for k,v in s['sections'].items()}},indent=2))

if __name__=='__main__':main()
