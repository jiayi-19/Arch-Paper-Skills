# Reference workflow coverage

The reference is `gulucaptain/Best-Paper-Writing-Skill` at revision `b9eff99`.
This is an architecture-specific independent implementation of its reusable workflow,
not a claim to reproduce its exact research statistics or every command-line flag.

| Reference capability | Architecture implementation | Actual scope |
|---|---|---|
| Offline intake and conversion | `assets/intake_form.html`, `scripts/intake_to_brief.py` | Free text, source/draft or schema v2; planned results remain pending. |
| Type/motivation routing | `references/routing.md` | Eight contribution routes; empirical coverage limits identified. |
| Claim calibration and evidence map | `references/claim-calibration.md`, converter ledger | Source, basis, comparison, conditions and pending support. |
| Abstract/Introduction variants and skeletons | `references/abstract.md`, `references/introduction.md`, workflow | Direct/gap/insight variants adapted to research type, not required output multiplication. |
| Method and experiments | Dedicated references plus architecture evaluation guide | Mechanism/contract, setup, controls, costs, measurement stages and results. |
| Sentence/paragraph annotation | `data/annotations/`, annotation protocol | Complete Abstract/Introduction for 24 papers; text-free labels/offsets/lengths/paraphrases. |
| Functional example retrieval | `scripts/find_exemplars.py` | Topic/type/venue plus primary function, paragraph role and section; short quotes remain attributed. |
| Corpus/style statistics | `analyze_corpus.py`, `writing_metrics.py`, `style_metrics.py` | Development-only per-paper distributions, role transitions and first-figure captions. |
| Draft checking | `scripts/check_draft.py` | Transparent lexical proxies, corpus notes and potential numeric provenance issues; no truth certification. |
| Figure planning/checking | Structured plan, guide, `check_figures.py` | Literal captions/labels/references/assets and first-caption distribution; no rendered-layout claim. |
| Diagram/plot assets | TikZ/table fragments, style file, `plot_results.py` | Mechanism/contrast, qualification/setup, bars/lines/breakdowns/tradeoffs; missing data explicit. |
| LaTeX integration | `prepare_paper.py`, `check_manuscript.py`, output guide | Independent copy of author-provided current official template. No transplanted CVPR kit or automatic rendering. |
| Author report and revision | Report template and revision/delivery guide | Substantive change/evidence notes; scoped revisions and rebuttal support. |
| Held-out evaluation | Four new sources, two writer arms, blind judge, scorer | Actual Abstract/Introduction outputs, fact/rubric judgments and complete neutral/negative results retained. |

Differences deliberately retained: architecture-specific measurement/attribution rules;
no universal ban on scope qualifiers, hypotheses or punctuation; corpus outliers are
advisory; user rendering/publication preferences are respected. A complete workflow
does not imply measured writing superiority. The small held-out comparison did not
show an advantage for the skill; see the retained results and protocol.
