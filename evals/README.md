# Held-out writing evaluation

This is a procedural holdout from writing-rule/profile development, not a claim that
source papers were unseen during model pretraining. The original 24 exemplar papers
were already used to construct the skill and cannot serve as an honest new holdout.
Four additional papers, one per venue, were selected by a separate source researcher.

## Separation

- `data/splits.json` fixes the 24 development IDs and codebook stage.
- `writer-briefs.json` contains only the assignment, paraphrased factual research
  materials, author terminology, bibliography and actual missing quantities.
- `heldout-cases.json`, `heldout-key.json` and source notes are evaluation-only: paper
  identity, source locators, fact IDs, qualification checks, rubric and penalty rules.
- Full original text stays private for extraction/copy-overlap diagnostics.
- Development role/profile thresholds are frozen before generating candidate outputs.

Writers read only their assigned briefs. The control condition uses the common writing
request without the skill. The skill condition receives the same briefs and output
budgets plus the frozen skill/development references. Both use independent agent
contexts inheriting the same parent model/settings, one generation per case, no web
retrieval, experiments, manuscript rendering or source-paper lookup. This compares
instruction packages, not training algorithms. Model sampling/token/time budgets are
not uniformly instrumented; report that limit rather than inventing equal token cost.

## Artifacts and scoring

Each writer saves `<case_id>.json` containing `case_id`, an `abstract` string and
an `introduction` array of three paragraphs. Preserve every generated candidate.
Use `prepare_blind.py` to randomize A/B labels; withhold its mapping from the judge
until judgments are saved. Judge against the fact key and stable rubric, not resemblance
to the original author's prose or an imagined best-paper feel.

```bash
python3 evals/prepare_blind.py --control outputs/control --skill outputs/skill \
  --out blind-candidates --mapping mapping.json --seed 29
python3 evals/score_outputs.py --briefs evals/writer-briefs.json \
  --outputs evals/outputs/skill --out mechanical-skill.json
```

The mechanical script checks requested structure, unverified numeric tokens,
bibliography keys and optional source-overlap diagnostics. It cannot decide whether
an allowed number was assigned the wrong meaning; the independent semantic judge
must inspect that. Rubric aggregation is reproducible with `--key` and `--grades`.
Coverage is weighted; penalties require quoted candidate evidence and relevant fact
IDs. Do not punish the same erroneous claim twice under overlapping penalty rules.

A single judge and four cases provide a small auditable diagnostic, not a statistical
claim about general writing quality, productivity or conference acceptance. Report
negative/neutral outcomes and changed scopes. Do not tune the skill on these four
outputs and then continue calling them held out. Future iteration needs new cases
or a clearly labeled development reuse.
