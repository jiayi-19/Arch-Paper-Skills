# Full-paper corpus

24 papers with a full-paper note each. See `full-paper-notes/README.md` for the template and limits, `../data/full-paper-index.json` for metadata and `scripts/find_notes.py` for search. The first corpus (`corpus.md`, 24 papers, abstract and introduction annotated) and this one overlap in five papers (Centauri, Constable, DynamoLLM, PIM Pathfinding, NoCap).

| id | Venue and recognition | Type | Best move to copy | Prose rhythm |
|---|---|---|---|---|
| isca-2025-h2llm | ISCA 2025, best paper | co-design with exploration | each design section ends with the knobs it exposes, sweeps end with numbered Takeaways | clean |
| isca-2026-cerberus | ISCA 2026, best paper | mechanism | real configurations turned into a failure list before any design | heavy dashes, not a model |
| isca-2026-moe-patterns | ISCA 2026, best paper | characterization and design | counterfactual paragraph before the thesis, observation to insight numbering | clean, semicolons about 25 |
| isca2024-constable | ISCA 2024, best paper | mechanism | oracle headroom study first, "We conclude that" after each observation | clean |
| asplos-2026-pf-llm | ASPLOS 2026, best paper | LLM-assisted mechanism | insight as a question anchored by a tiny example, bounded-scope paragraph | clean |
| asplos-2026-vcxlgen | ASPLOS 2026, best paper | automated synthesis | one numbered frame reused for requirements, goals and evaluation dimensions, bold Takeaways | some dashes |
| asplos-2026-lifetime | ASPLOS 2026, best paper | benchmark, framework and co-design | one quantity as first-class parameter, hand-off sentences between sections, gap table | clean |
| asplos-2026-counterpoint | ASPLOS 2026, best paper | methodology | promise-versus-reality paragraphs, concrete refuted assumption in the opening | heavy dashes, not a model |
| asplos-2025-smoothe | ASPLOS 2025, best paper | algorithm for compilers and design | one tiny example reused three times, setups where the baseline wins shown | some dashes |
| asplos-2025-orion | ASPLOS 2025, best paper | framework | three bold challenges answered by three solution paragraphs with numbers, decomposition table | clean |
| asplos-2025-metasapiens | ASPLOS 2025, best paper | algorithm and accelerator | ingredient labels reused as paragraph labels, proposal framed between two named extremes | clean |
| asplos-2024-isaria | ASPLOS 2024, best paper | automation | a tiny failing baseline with numbers, research questions as headings | some dashes |
| asplos-2024-centauri | ASPLOS 2024, best paper | search space for scheduling | challenge answered by an insight in the same paragraph, one toy example reused, prior work as subsets table | clean |
| micro-2024-fusion3d | MICRO 2024, best paper | integrated accelerator | C and T tags carried from the Introduction to the ablations | some dashes |
| micro-2024-vnpu | MICRO 2024, best paper runner-up | system and ISA | three "Lack of X" gaps answered by three contributions and three evaluation claims | clean |
| micro-2024-mess | MICRO 2024, best paper runner-up | benchmark and simulator | one object (the curve family) carries the paper, existing tools measured first | clean |
| micro-2024-nocap | MICRO 2024, best paper candidate | co-design | decompose the baseline gap into named factors and multiply them out | clean, semicolons about 28 |
| hpca-2025-dynamollm | HPCA 2025, best paper | system | numbered list of variation reused as sections, insights and principles, cost next to each win | clean |
| hpca-2024-pim-pathfinding | HPCA 2024, best paper | tool and characterization | tool validated with correlation and error including where weak, Key takeaways per case study | clean, very long sentences |
| hpca-2020-sigma | HPCA 2020, best paper | accelerator | three requirements reused as table rows and ablation arms, losses reported | clean |
| isca-2020-mlperf-inference | ISCA 2020, benchmark read as a model, no award | benchmark | ownership boundary between evaluator and participant, blacklist with its reason, audit statistics | clean |
| mlsys-2020-mlperf-training | MLSys 2020, benchmark read as a model, no award | benchmark | each challenge answered by a named mechanism that cites the challenge section, reference defines the task and is not a performance baseline | clean |
| isca-2023-archgym | ISCA 2023, benchmark read as a model, no award | benchmark and framework | the first experiment proves the need, a three-part need answered by three insights in order | clean |
| arxiv-2023-robotperf | arXiv 2023, benchmark read as a model, no award | benchmark | comparison table of existing benchmarks with an honest cross. Weak: abstract with no problem and no number | clean |

Recognition sources are in the index. The benchmark papers were chosen as models for benchmark writing. No award is claimed for them.
