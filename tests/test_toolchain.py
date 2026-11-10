"""Functional contracts for the generic writing toolchain; synthetic fixtures only."""
import argparse
from copy import deepcopy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
sys.path.insert(0,str(ROOT/'evals'))
import writing_metrics as wm
import analyze_corpus
import check_manuscript
import check_figures
import intake_to_brief
import plot_results

class Toolchain(unittest.TestCase):
    def test_percentages_and_sentence_boundaries(self):
        text='We reduce latency by 30% under this setting. Fig. 2 shows a 3.5 ms observation. It applies to one regime.'
        self.assertIn('under this setting',wm.plain(text))
        self.assertEqual(len(wm.sentences(text)),3)
        self.assertEqual(wm.measure(text)['number_tokens'],3)

    def test_intake_preserves_planned_evidence(self):
        data=json.loads((ROOT/'assets/intake.example.json').read_text())
        data['evidence']=[{'id':'E1','claim':'Latency benefit','status':'planned','ours':None,'baseline':None,'source':'not collected'}]
        brief,ledger,missing=intake_to_brief.convert(data)
        self.assertFalse(missing);self.assertEqual(ledger['claims'][0]['status'],'planned')
        self.assertIsNone(ledger['claims'][0]['ours']);self.assertIn('planned',brief)
        data['research']['mechanism']='';self.assertIn('mechanism',intake_to_brief.convert(data)[2])

    def test_public_statistics_reproduce(self):
        expected=json.loads((ROOT/'data/corpus-stats.json').read_text())
        ids=json.loads((ROOT/'data/splits.json').read_text())['development_ids']
        records=[json.loads((ROOT/'data/annotations'/(pid+'.json')).read_text()) for pid in sorted(ids)]
        for record in records:
            for section in record['sections']:
                for paragraph in section['paragraphs']:
                    for sentence in paragraph['sentences']:self.assertNotIn('text',sentence)
        with tempfile.TemporaryDirectory() as directory:
            out=Path(directory);(out/'data').mkdir()
            actual=analyze_corpus.summarize(records,out)
        self.assertEqual(actual,expected)
        self.assertEqual(len(ids),24)

    def test_function_retrieval_and_split(self):
        result=json.loads(subprocess.check_output([sys.executable,str(ROOT/'scripts/find_exemplars.py'),'--function','limitation','--section','introduction','--format','json','--limit','100'],text=True))
        self.assertTrue(result)
        dev=set(json.loads((ROOT/'data/splits.json').read_text())['development_ids'])
        self.assertTrue(all(r['id'] in dev and r['annotation_matches'] for r in result))
        for row in result:
            for item in row['annotation_matches']:self.assertEqual(item['section'],'introduction')

    def test_source_checks_and_figure_assets(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory);(root/'body.tex').write_text(r'\section{Design}\label{sec:design}')
            (root/'refs.bib').write_text('@article{verified,title={Synthetic reference},author={Test Author},year={2026}}')
            (root/'plot.svg').write_text('<svg xmlns="http://www.w3.org/2000/svg"></svg>')
            main=root/'main.tex'
            main.write_text(r'''\input{body}\ref{sec:design}\cite{verified}\bibliography{refs}
\begin{figure}\includegraphics{plot.svg}\caption{Synthetic illustration.}\label{fig:one}\end{figure}\ref{fig:one}''')
            self.assertFalse(check_manuscript.inspect(main,root)['errors'])
            self.assertFalse(any(x['level']=='ERROR' for x in check_figures.inspect(main)['issues']))
            main.write_text(r'\input{missing}\cite{unknown}\ref{absent}\label{d}\label{d}')
            self.assertEqual(len(check_manuscript.inspect(main,root)['errors']),4)

    @unittest.skipUnless(importlib.util.find_spec('matplotlib'), 'Install requirements-figures.txt for plotting integration')
    def test_plot_data_status_and_normalization(self):
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/'input.csv'
            content='case,method,value,status\nA,Reference,10,valid\nA,Variant,8,valid\nB,Reference,12,valid\nB,Variant,,not_measured\n'
            path.write_text(content)
            args=argparse.Namespace(csv=path,out=Path(directory)/'plot.svg',kind='bars',y_label='Normalized latency (candidate/baseline)',x_label=None,width='column',data_kind='synthetic',normalize_to='Reference')
            report=plot_results.plot(args)
            self.assertEqual(path.read_text(),content)
            variant=next(r for r in report['plotted_rows'] if r['case']=='A' and r['method']=='Variant')
            self.assertEqual(variant['source_value'],8);self.assertAlmostEqual(variant['plotted_value'],.8)
            self.assertEqual(report['missing_results'],1)
            image=args.out.read_text();self.assertIn('SYNTHETIC EXAMPLE',image);self.assertIn('not_measured',image)
            path.write_text('case,method,value,status\nA,Reference,0,valid\nA,Variant,8,valid\n')
            with self.assertRaises(ValueError):plot_results.plot(args)
            path.write_text('case,method,value,status\nA,Reference,1,invalid\n')
            with self.assertRaises(ValueError):plot_results.load(path)

    def test_template_copy_isolation(self):
        with tempfile.TemporaryDirectory() as directory:
            base=Path(directory);source=base/'source';source.mkdir();(source/'main.tex').write_text('Synthetic template')
            target=base/'copy'
            subprocess.run([sys.executable,str(ROOT/'scripts/prepare_paper.py'),'--template',str(source),'--out',str(target)],check=True,stdout=subprocess.DEVNULL)
            (target/'main.tex').write_text('Changed copy')
            self.assertEqual((source/'main.tex').read_text(),'Synthetic template')
            again=subprocess.run([sys.executable,str(ROOT/'scripts/prepare_paper.py'),'--template',str(source),'--out',str(target)],capture_output=True)
            self.assertNotEqual(again.returncode,0)


class EvaluationContracts(unittest.TestCase):
    def test_weighted_coverage_and_capped_penalty(self):
        sys.path.insert(0,str(ROOT/'evals'))
        import score_outputs
        dimensions={'fact_fidelity':20,'unsupported_numbers':10,'baselines_scope':10,'argument':15,'mechanism':15,'evidence':10,'positioning':10,'economy':10}
        key={'rubric':[{'metric_id':k,'weight':v} for k,v in dimensions.items()],
             'penalty_rules':[{'rule_id':'invented','metric_id':'unsupported_numbers','points_per_occurrence':8,'metric_penalty_cap':10}]}
        case={'case_id':'synthetic','fact_coverage':[{'fact_id':'F1','coverage_weight':1},{'fact_id':'F2','coverage_weight':1}]}
        grade={'fact_coverage':[{'fact_id':'F1','coverage_level':1},{'fact_id':'F2','coverage_level':.5}],
          'metric_raw_scores':{k:5 for k in dimensions},'penalties':[{'rule_id':'invented','count':3,'evidence':'Synthetic candidate invented a result'}]}
        result=score_outputs.aggregate_grade(case,grade,key)
        self.assertEqual(result['metric_scores']['fact_fidelity'],15)
        self.assertEqual(result['metric_scores']['unsupported_numbers'],0)
        self.assertEqual(result['total'],85)
        grade['fact_coverage'].append(grade['fact_coverage'][0])
        with self.assertRaises(ValueError):score_outputs.aggregate_grade(case,grade,key)

    def test_numeric_audit_and_source_overlap_are_not_truth(self):
        import score_outputs
        brief={'case_id':'synthetic','task':{'abstract_words':[1,100],'introduction_paragraphs':3},
          'facts':['A simulation reports 2x kernel speedup.'],'bibliography':[]}
        output={'abstract':'We report 2x full-system speedup and 99% lower energy.',
          'introduction':['A synthetic example.','The mechanism changes a buffer.','The result needs independent validation.']}
        result=score_outputs.measure_case(brief,output,'We report 2x full-system speedup and 99% lower energy.')
        self.assertIn('99%',result['unverified_numeric_tokens'])
        self.assertNotIn('2x',result['unverified_numeric_tokens'])
        self.assertGreater(result['source_overlap']['longest_contiguous_word_run'],5)

if __name__=='__main__':unittest.main()
