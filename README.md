# Computer Architecture Writing Skill

An evidence-led paper-writing skill for **HPCA, ASPLOS, ISCA, and MICRO**.
It helps develop a research argument, draft and revise paper sections, plan figures,
and connect quantitative claims to the mechanism and evidence that support them.

## What it includes

- A reusable workflow for storylines, abstracts, introductions, motivation, mechanisms,
  evaluation, related work, and rebuttals.
- Architecture-specific guidance on baseline fairness, resource and clock assumptions,
  mechanism attribution, model validation, PPA scope, and automated design agents.
- **24 source-located paper exemplars**, six from each of the four conferences.
- On-demand exemplar retrieval and a read-only LaTeX source checker.

The corpus contains **6 Best Papers, 5 candidates/nominees or designated Best Paper
Session papers, 9 Test of Time / named Influential Paper Award recipients, and
4 notable teaching selections**. Publication years and award years are recorded
separately. Each entry has a short excerpt, PDF page, source links, reading scope,
writing analysis, and a transfer caveat.

Browse the [corpus and paper list](references/corpus.md). The selection spans
processors, caches, memory, security, accelerators, compilers, datacenters, and
architectural modeling. It is a curated teaching collection, not a statistical
study of all award papers or a guarantee of acceptance.

## What the exemplars teach

These are qualitative interpretations of selected passages, not statistical claims
about every award paper. The source passages, locators, reading scope, and transfer
limits are recorded in the [corpus](references/corpus.md).

| Lesson | Representative papers | How the skill applies it |
|---|---|---|
| Turn a workload observation into a specific design intervention. | UCP distinguishes cache demand from utility; Adaptive Insertion Policies separates victim choice from insertion policy. | Connect the observed bottleneck, remaining cost, mechanism, and testable consequence before polishing prose. |
| Explain what a representation permits before claiming an optimizer is better. | Centauri expands communication partition choices; TensorIR exposes tensorized computation to transformations. | Separate search-space expansion, legal construction, search quality, and final design quality. |
| Make the baseline and accounting part of the argument. | Eyeriss compares dataflows under shared hardware constraints; NoCap gives a CPU baseline matching algorithmic improvements. | Check resource, precision, clock, workload, algorithm, and budget conditions before attributing a gain to the proposed mechanism. |
| Validate a fast model for its intended design decision. | Wattch separates several kinds of validation; McPAT identifies the measurement type available for its comparison. | Distinguish predictions, simulation, implementation-stage PPA, and hardware observations; state what each validation supports. |
| Put the relevant operating limit next to the claim. | Runahead explains architectural-state preservation; TALCO states its banding qualification; RowHammer reports the observed hardware population. | Preserve correctness assumptions and scope in the headline when omitting them would change its meaning. |

## Why use this skill

The skill turns these lessons into repeatable writing decisions:

- **Build a continuous argument.** Each motivation earns a design requirement, and
  each mechanism has an observable consequence and an evaluation obligation.
- **Expose missing experiments early.** A claim-to-evidence map makes absent controls,
  unmatched comparisons, or unsupported scope visible before the abstract is finalized.
- **Retrieve by writing purpose.** Find an example of a bottleneck argument, model
  validation, or qualified result without copying another paper's wording.
- **Keep revisions consistent.** Align terminology and claim strength across the
  abstract, introduction, contributions, figures, and results.
- **Catch source-level mistakes cheaply.** Check literal citations, labels, and draft
  markers without compiling or rendering the manuscript.

Its current validation covers corpus provenance, retrieval, source-checking behavior,
and a synthetic writing trial that preserved kernel scope and resource confounds.
It does not establish improved acceptance rates or measured author productivity.

## Install

For a fresh Codex installation, clone this repository directly to the skill folder:

```bash
git clone https://github.com/jiayi-19/Arch-Paper-Skills.git ~/.codex/skills/computer-architecture-writing
```

Alternatively, copy this repository's contents into:

```text
~/.codex/skills/computer-architecture-writing/
```

If `CODEX_HOME` is configured, use `$CODEX_HOME/skills/computer-architecture-writing/`
instead. Keep `SKILL.md`, `agents/`, `references/`, `scripts/`, and the license files
together; omit repository metadata (`.git/`) and caches. Preserve any existing skill
installation before replacing it.

The two helper scripts require **Python 3.10+** and use only the standard library.
No model API keys, TeX installation, or PDF rendering are required by these helpers.
Other skill-capable agents can load `SKILL.md` and its relative references; the
`agents/openai.yaml` file supplies Codex UI metadata.

## Use

Example requests:

```text
Use $computer-architecture-writing to turn this project outline and verified
results into a paper storyline and Introduction.

Use $computer-architecture-writing to revise this motivation section. Preserve
our terminology and identify claims that need additional evidence.

Use $computer-architecture-writing to review our evaluation for baseline fairness,
mechanism attribution, workload scope, and PPA qualification.
```

Chinese requests work too:

```text
用 $computer-architecture-writing，按我们的 outline 写 Background and Motivation，
保持术语一致，尚未完成的实验保留明确的待补位置。
```

The skill follows the manuscript language and the session's editing, rendering,
and publication preferences. Loading the skill does not itself authorize running
experiments or pushing changes to a remote repository.

## Retrieve writing examples

Run from the repository root:

```bash
python3 scripts/find_exemplars.py --list --limit 100
python3 scripts/find_exemplars.py --venue ISCA --topic memory
python3 scripts/find_exemplars.py --move "validation" --limit 3
python3 scripts/find_exemplars.py --id isca2016-eyeriss
python3 scripts/find_exemplars.py --recognition best_paper_candidate --limit 5
```

The finder returns the source-located excerpt and a writing card. Learn the
argument structure and information order; do not copy the excerpt into a new paper.
Use `--help` for filters and JSON output.

## Check LaTeX source

```bash
python3 scripts/check_manuscript.py /path/to/paper/main.tex
python3 scripts/check_manuscript.py /path/to/paper/main.tex --format json
```

The checker inspects ordinary literal inputs, bibliography keys, labels, references,
and drafting markers. It reports dynamic arguments as unverified where recognized.
It is a source heuristic, not a TeX interpreter or a scientific validity checker;
macro-heavy source and actual research claims still require inspection. It does not
compile, render, access the network, or execute manuscript code.

## Layout

```text
computer-architecture-writing/
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── argument-design.md
│   ├── architecture-evaluation.md
│   ├── sections-and-figures.md
│   ├── revision-and-delivery.md
│   ├── corpus-maintenance.md
│   ├── corpus.md
│   └── corpus.json
├── scripts/
│   ├── find_exemplars.py
│   └── check_manuscript.py
├── NOTICE.md
├── LICENSE
└── LICENSE-base-skill
```

## Sources, attribution, and license

This project adapts workflow ideas from
[Best-Paper-Writing-Skill](https://github.com/gulucaptain/Best-Paper-Writing-Skill),
inspected at revision `b9eff99`. The architecture corpus, analytical guidance, and
helper scripts were developed for this adaptation. See [NOTICE.md](NOTICE.md)
for the upstream lineage, modifications, and attribution.

Original adaptation content is **CC BY 4.0**; base-work MIT attribution is preserved
in [LICENSE-base-skill](LICENSE-base-skill). Short paper excerpts remain the property
of their respective rights holders and are included for commentary and instruction.
They are not relicensed as this project's original content. Full paper PDFs are not
distributed in this repository.
