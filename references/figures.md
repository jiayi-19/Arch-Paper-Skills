# Figure planning, templates and data checks

Plan question -> claim -> visual -> needed data -> conditions -> caption -> status.
Use `assets/figure-plan.template.json`. A first figure may expose a bottleneck,
contrast a mechanism, summarize a system or show an observation. Its placement and
width follow the argument and current template, not a transplanted CVPR teaser rule.
The development profile contains inspected first-figure categories and caption
statistics only; it does not claim a survey of every figure in every paper.

Templates in `assets/figures/`:

- `mechanism.tex`: event/state/action with explicit feedback; TikZ libraries are noted.
- `contrast.tex`: baseline/proposal schematic ordering, explicitly not timing data.
- `coverage-table.tex`, `setup-table.tex`: acceptance and comparison conditions.
- `architecture.mplstyle`: consistent vector plot typography and accessible colors.
- `example-synthetic.csv`: visibly synthetic integration input, not research evidence.

`plot_results.py` supports grouped bars, lines, stacked breakdowns and resource/performance
scatter (`pareto`). It requires data-kind, metric label and a tidy CSV with case,method,
value,status; optional resource supplies the scatter axis. Unavailable results have
empty values and explicit status. Normalization is candidate/baseline, not an implicitly
reversed speedup. The scatter does not itself certify a Pareto optimum. Record actual
units, scope, axis direction and aggregation in the caption and source table.

```bash
python3 scripts/plot_results.py results.csv --kind bars --out latency.svg \
  --data-kind measured --y-label 'Latency (ms)' --normalize-to Reference
```

If normalizing, update the y-label to explain the resulting dimensionless ratio.
Empirical figure content requires actual data. Schematics can be built once the
mechanism is specified. Preserve method colors/symbols and support grayscale reading;
show controlled conditions in ablations, not only the preferred result.

`check_figures.py main.tex` checks literal float captions, labels, references,
placeholders and asset paths without rendering. Macro-heavy sources, axis units,
scientific content and actual layout still require inspection. First-caption
percentile notes are development observations, not mandatory caption lengths.

## Practices seen in the full-paper sample

From the 24 full-paper notes (`full-paper-notes/`). These are observations, not rules.

### The first figure

In the 20 prize papers the first figure sets up the vocabulary or poses the gap. None puts the headline results
there. Kinds seen:

| Kind | Example |
|---|---|
| The setting made concrete | Fusion-3D (two users, a headset and 100 MB of photos), H2-LLM (edge LLM services with batch sizes) |
| The problem and the answer on one timeline | Centauri (three timelines of the same layer: direct, fused, proposed) |
| The central object of the paper | Mess (the family of bandwidth-latency curves, built and used in three panels) |
| The gap drawn as a map | MoE patterns (models by release date and size, zones "no study" and "first profiled in our work") |
| One tiny example that carries the insight | PF-LLM (a 20-line program with four accesses, each needing a different prefetch strategy) |
| The vocabulary of the machine | vNPU, Cerberus, PIM Pathfinding, NoCap |
| A table of real shapes or a regime comparison | SIGMA (real GEMM shapes), Lifetime (three regimes on four axes) |

Choose the first figure by the question "what must the reader see before anything else makes sense?".

### The overview figure

- Number the steps with circles and cite them in the text and in the caption (vCXLGen, Centauri, Cerberus,
  Constable, vNPU).
- Tag blocks with the frame items: Fusion-3D marks which challenge and which technique sit where, with
  section numbers on the blocks.
- Colour what is new against what is inherited: MoE patterns highlights the added units in orange,
  MetaSapiens colours baseline, foveation and load balance differently.
- Draw a worked example inside the figure (Lifetime Figure 4 draws a food spoilage example in the framework
  figure and shows the optimal core changing with shelf life).
- Keep one figure for the whole system and put detail in later figures.

### Comparison tables that carry novelty

- Prior work as subsets of the proposed space (Centauri Table 1, check marks over four dimensions).
- Industry practice, prior academic designs and the proposal in one grid of properties (Cerberus Table I).
- A gap table whose rows become the components (Lifetime Table 1, three rows).
- Desired feature, the limitation of the standard design, the proposed structure, the resulting property
  (SIGMA Table I, repeated per prior accelerator in Table III).
- Prior systems by one number that matters, with the paper's own row last (Fusion-3D Table I, off-chip
  bandwidth assumed against what a real port offers).

### Result figures

- Identical axes across panels when comparing sources (Mess).
- Failures and limits are drawn, not dropped: timeouts counted and shown in red (SmoothE), out-of-memory
  bars labeled with the limit (vCXLGen), empty gray cells for violated constraints (DynamoLLM).
- Per-bar numbers on the bars, a log axis stated in the caption, and the normalization baseline named.
- Ablations as a staircase that adds one component at a time (MetaSapiens, SIGMA).
- A decomposition table that splits a headline factor into named parts (Orion Table 4).
- A trace figure with marked regions used to explain why the result happens (PF-LLM Figure 9).

### Captions

- About three quarters of captions are descriptive: what is plotted, the panel keys, the units.
- Result captions often add the point: Mess "the simulator closely matches the actual curves", PF-LLM
  Figure 4 states the final accuracy, Isaria states the trade-off the plot shows.
- A long caption is acceptable when it makes the figure self-contained (Centauri Figure 3 explains all six
  circled steps).
- The takeaway for a figure usually appears in the text as a bold "Takeaway" line.

### The reused example

Draw one small example early and reuse it: Centauri reuses a four-matmul FSDP layer in Figures 1, 3, 5 and
12, SmoothE reuses one e-graph in Figures 1 to 3 (sum the costs 32, 27, 19), SIGMA runs three tiny GEMMs
through two designs. Each later idea then reads as a change to a picture the reader has seen.
