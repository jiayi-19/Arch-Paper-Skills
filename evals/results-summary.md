# Held-out writing results

Frozen development version: `9dc333b`. Four new source-paper briefs, one per venue; two independent writer contexts with the same parent settings and common tasks, one generation per condition/case. A separate judge received randomized A/B candidates and the fact key, with the condition mapping withheld until its grades were saved. See [run record](run-record.json) and [protocol](README.md).

## Descriptive scores

| Case | Control | Frozen skill | Skill − control |
|---|---:|---:|---:|
| heldout-asplos-01 | 99.00 | 98.00 | -1.00 |
| heldout-hpca-01 | 99.00 | 99.00 | +0.00 |
| heldout-isca-01 | 97.50 | 97.50 | +0.00 |
| heldout-micro-01 | 99.00 | 99.00 | +0.00 |

Mean: control **98.62/100**, skill **98.38/100**, paired difference **-0.25**. Skill wins 0, ties 3, control wins 1. These are rubric observations, not a statistical superiority result.

## Integrity and interpretation

All eight candidates meet requested form constraints. Mechanical numeric audit found no tokens absent from their briefs; original-source overlap diagnostics found no 8-gram overlaps outside the brief. These mechanical checks cannot detect misuse of a number already present in the brief. The independent semantic judge identified no factual penalties or fatal fabrication triggers. Its per-fact evidence and quality differences are preserved, rather than replaced with an aggregate claim.

The control condition already produced strong drafts, so this small comparison should not be used to claim the skill is generally superior. The observed score differences reflect one judge on one output per condition. They do not measure author productivity, repeatability across model samples, or paper acceptance. Model pretraining exposure to the original publications cannot be excluded. Context length and token/time cost were not equalized or instrumented.

No writing rule, percentile profile or candidate was revised in response to these scores. A source-map type check was improved in the evaluation harness after writer freeze; it changes diagnostics, not the drafts or rubric. Future optimization on these cases turns them into development cases and requires a fresh holdout.

## Reproduction and artifacts

Generated [control drafts](outputs/control/), [skill drafts](outputs/skill/), [blind candidates](blind-candidates/), [blind judgments](blind-grades.json), [revealed mapping](blind-mapping.json), [control results](control-results.json), and [skill results](skill-results.json) are retained.

```bash
python3 evals/score_outputs.py --briefs evals/writer-briefs.json --outputs evals/outputs/control \
  --key evals/heldout-key.json --grades evals/grades/control.json --out control-reproduced.json
python3 evals/score_outputs.py --briefs evals/writer-briefs.json --outputs evals/outputs/skill \
  --key evals/heldout-key.json --grades evals/grades/skill.json --out skill-reproduced.json
```

This reproduces structural/numeric checks and exact rubric aggregation from saved judgments. Repeating the model generations or semantic judgment may change the scores. Source-overlap diagnostics additionally require privately obtained original paper text in the documented case-to-path map; full originals are not redistributed.
