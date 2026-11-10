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
