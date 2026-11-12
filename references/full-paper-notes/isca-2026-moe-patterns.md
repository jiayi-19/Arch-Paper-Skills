# isca-2026-moe-patterns: Patterns Behind Chaos: Forecasting Data Movement for Efficient Large-Scale MoE LLM Inference

Source read: arXiv v5 (12 May 2026), "Accepted to ISCA 2026. This is the authors' preprint version." Earlier versions were titled "Orders in Chaos" with different numbers (v1 reported 6.3x and 4.0x); I read only v5. Counts are estimates from pdftotext of a two-column layout; figure text is excluded where I could.

## 0. Identity
- Title: Patterns behind Chaos: Forecasting Data Movement for Efficient Large-Scale MoE LLM Inference
- Venue and year: ISCA 2026. Award: Best Paper.
- Contribution type: characterization (data-movement profiling of MoE models) with two design case studies (a wafer-scale GPU architecture change and a software placement algorithm). Also a trace release.
- Pages: 17 in the arXiv PDF (body about 12 pages, then references and an artifact appendix).
- Authors: Yu, Guan, Yu, Zhou, Hu, Pei, Kang, Ding, Tsai (UCSD, Samsung, NVIDIA, others).
- Full text used: https://arxiv.org/pdf/2510.05497v5

## 1. Skeleton
Roman-numeral sections with lettered subsections. Body prose about 7,800 words.

| Section | Approx words | Figures / tables | Role |
|---|---|---|---|
| Abstract | 190 | 0 | summary |
| I Introduction | ~1,000 (6 paragraphs + 4 bullets) | Figs 1-2 | problem, gap, thesis, case-study preview, contributions |
| II Background (A model architecture, B prior serving systems) | ~580 | Fig 3 | background; B also frames "system-centric" vs "model-centric" |
| III MoE Profiling and System Insights (A categorization, B temporal, C spatial) | ~1,700 | Figs 4-9 | the characterization; seven observations (Ob1-Ob5 plus sub-views) and six insights |
| IV Case Study 1: Wafer-Scale GPU Architecture Design (A trend, B programming model, C challenges, D motivation and insights, E architecture design) | ~1,700 | Figs 10-11, Algorithm 1 | design |
| V Evaluation (A setup, B simulator validation, C throughput, D hop reduction, E DRAM breakdown, F host-CPU comparison, G area and power) | ~2,000 | Figs 12-15, Tables I-II | methodology + results for case study 1 |
| VI Case Study 2: Prefill-Guided Decode Expert Placement on Real GPU Clusters | ~490 | Figs 16-17, Algorithm 2 | design + methodology + results in one section |
| VII Discussion | ~130 | 0 | scope |
| VIII Related Work | ~510 | 0 | related work, two run-in paragraphs |
| IX Conclusion | ~110 | 0 | conclusion |
| Artifact Appendix | ~300 | 0 | reproducibility |

Totals: 17 figures, 2 tables, 2 algorithms. The profiling section and the first case study are of similar size; the second case study is short.

## 2. Abstract
- 9 sentences, 190 words, one paragraph, plus Index Terms.
- Functions: (1) setting, large-scale MoE LLMs are the frontier open-weight models; (2) problem, "But" random expert selection causes data movement that dominates multi-unit serving; (3) approach, to understand it, profiling of four 2025 models (200B-1000B) with over 24,000 requests; (4) insight or contribution, temporal and spatial analysis and "six key insights"; (5) scope of validation, on future wafer-scale GPUs and existing GPU systems; (6) result one, "6.6x average speedup across four 200B-1000B models" with "lightweight architectural modifications"; (7) result two, prefill-aware placement "up to 1.25x" on MoE computation; (8) claim, "the first comprehensive data-centric analysis" plus a concrete design study; (9) artifact, traces are public with a link.
- Numbers: 200B-1000B, 24,000 requests, six insights, 6.6x average (scope: four models, wafer-scale GPUs), 1.25x (scope: "up to", MoE computation only). The 6.6x is "average" across models; the 1.25x is "up to".
- The system has no name; the contribution is the profiling plus two unnamed case studies.
- Quote (Abstract): "Our work presents the first comprehensive data-centric analysis of large-scale MoE models together with a concrete design study applying the learned lessons."

## 3. Introduction
- 6 prose paragraphs plus a lead-in line and 4 bullets; about 1,000 words. Fig 1 and Fig 2 sit in the first two pages of the introduction.
- P1: setting. Opens "Large Language Models (LLMs) have demonstrated remarkable capabilities across diverse domains"; narrows to MoE as frontier models. Ends on MoE being the most widely used open-weight models.
- P2: problem. "Unlike dense LLMs that activate all model weights uniformly, MoE models dynamically route each token..." gives the first number: data movement above 50% of execution time for a small model on 2-4 GPUs; then size trend (DeepSeek V3 with 32x experts and 15x parameters). Ends on "making the associated data movement patterns ever more critical".
- P3: gap. "Yet as shown in Figure 1, no prior work has systematically investigated these patterns at scale." Prior work dismissed as "surface-level observations without system-level insights". Ends with "a fruitful opportunity".
- P4: a what-if paragraph. "If data movement in MoE models were fully unpredictable..." explains in temporal and spatial terms why unpredictability would hurt (4,426,165,368 combinations for DeepSeek V3). It makes the stake concrete before the thesis.
- P5: thesis and method. "Fortunately, as we later show in the paper, MoE expert selections indeed have predictability that designers can exploit to reduce data movement." Then profiling set-up (four models, 24,000 requests, over 2,000 GPU hours, 150 GB of traces), then three questions that the insights answer ("Is there a correlation between previously selected experts and those selected later?").
- P6: validation by case studies on future and existing systems; each ends with its number (6.6x, 1.25x). This is the results-preview paragraph and it is combined with the case-study description.
- Contribution list: "Our main contributions can be summarized as follows:" 4 bullets. (1) a profiling methodology and scope (a capability, with numbers: four models, 235B-1000B); (2) six key insights (a finding); (3) two case studies with results (6.6x and 1.25x, a result); (4) over 70,000 traces and a simulator released (an artifact). Three of four carry numbers.
- Problem posed: data movement dominates, and no one knows whether it is predictable.
- Key insight first appears in the abstract implicitly ("random" expert selection), explicitly in P5 ("Fortunately... predictability").
- No "challenges" device. The motivating structure is a counterfactual ("If... were fully unpredictable") followed by "Fortunately".
- Prior work credit: only in the Gap paragraph and Section II-B ("system-centric methodology" vs the paper's "model-centric").
- Quote (I, P4): "If data movement in MoE models were fully unpredictable, it would present significant challenges for deployments on multi-unit systems."

## 4. Motivation and background
- Section II is Background; motivation is mostly in the introduction (Fig 2 shows that MoE data movement is 60-90% of total latency for 4K sequence under three serving configurations) and in IV-C/D for the case study.
- II-B is a prior-work critique more than background. It reframes the paper as "flip the process and adopt a model-centric strategy", giving a conceptual contrast (system-centric vs model-centric).
- Evidence type: measured and modeled latency breakdown (Fig 2), a literature map (Fig 1 bubble chart with a "no study" region), and then the profile in III.
- Each observation in III is labeled Ob1 to Ob5 in the subsection title ("1) Layer-Level Correlation: (Ob1)"). III-B ends with a subsection "System Insights from Temporal Relation" holding starred boxes Insight 1-2; III-C ends with "System Insights from Spatial Relation" holding Insights 3-6. Each starred insight has a bold name, a parenthetical pointer to its observations, and one imperative sentence ("Leverage the expert selection trace from the prefill stage to predict...").
- Tie to design: the case-study sections open with "We follow Insight 3 to design a task allocation algorithm and leverage the temporal relation insights (Insight 1 and Insight ...", a one-to-one mapping by number. IV-D "Motivation and Insights" repeats the mapping before the design.
- The Discussion (VII) restates that the two case studies are "case studies demonstrating the practical applicability" and that the insights, not the designs, are the "primary contribution".

## 5. Overview of the design
- No separate Overview. IV-E "Architecture Design" opens with "1) Architecture Overview" (about 150 words) that points at Fig 10(a) and says modifications are highlighted in orange. Fig 10(a) shows the wafer-scale GPU with a two-level Command Processor and the added ATU and PDU units in orange, with (b) the SoW technology and (c) the data format.
- The text walks components, not numbered steps, in the overview; then "3) Workflow During Kernel Launch" walks numbered circles 1-5.
- Key insight handling: IV-D "Motivation and Insights" states the two strategies and which insight each follows. The design is introduced as "two strategies with architectural support".
- Case study 2 has no overview; it begins with "A. Introduction" posing a concrete practical question.

## 6. Design sections
- Pattern for IV: trend (why the hardware will exist), programming model (two candidates, why one was chosen), challenges (two named: "Simplistic Task Allocation", "Inadequate Local HBM Management"), motivation and insights, architecture design (overview, data structures, workflow, dataflow, algorithm).
- Running example: expert selection for a token (1, 4) with predicted popular experts (2, 4, 6) in Fig 11, followed in prose ("In this example, a die computes experts 1 and 4...").
- Component names: Global CP, Local CP, ATU (Address Translation Unit), PDU (Prediction Unit), Prediction Table, Expert Distribution Table; defined once and used consistently.
- Movement between components: kernel launch workflow in numbered circles; remote read non-duplicated vs duplicated, with colored lines in the figure.
- Detail deferred: simulator validation is in V-B; area and power in V-G with a table; host-CPU alternative in V-F.
- Figure types: heatmaps (profiling), bubble chart, block diagrams, algorithm boxes, bar charts, CDF plots.

## 7. Evaluation
- Not organized by research question. Section V is organized by metric and question implicit in the subsection titles (throughput, hop reduction, DRAM breakdown, host-CPU comparison, area and power). Case study 2 is a self-contained mini-evaluation.
- First result: V-B simulator validation (within 5% error of real 8xH100 measurements) before any speedup is shown; the first performance result is V-C throughput (Fig 12).
- Claim bounding: metric defined as decode-stage MoE-layer throughput and justified by disaggregation trends; baseline is "Base (w/o proposed HW)" on three chiplet configurations (Dojo, TSMC-SoW, Dojo-Enhanced in Table I); batch sizes 4096 to 16384.
- Ablation: Pred Only, Allo Only, Allo+Pred, and an EP baseline, in Fig 12; hop-count reduction analysis explains why gains saturate (hop reductions of 4.5x, 142x and 213x produce 3.0x, 6.3x and 6.6x, so "hop count is no longer a performance bottleneck").
- Weak or negative: at batch 4096 the proposed strategy "degenerates to EP"; the advantage over EP appears only at large batch (1.44x at 16,384); case study 2 gain is 12.5-15.5% with a stated reason, "our 8-GPU EP scale inherently limits the achievable improvement"; host-CPU overhead of 5.2-51.6% reported as the case for hardware.
- Quote (VI-C): "our 8-GPU EP scale inherently limits the achievable improvement"

## 8. Sentence and paragraph habits
- Average sentence length: about 26-28 words on prose (script: 28.5, rough).
- Paragraph length: long, 6-10 sentences in III and IV; shorter in V.
- Person and tense: present, "we" about 100 times and "our" about 38 in 7,800 words; more first person than the other three papers.
- Topic sentences present; bold run-in labels ("Comparison across models:", "Metric.", "Baselines.", "Methodology:").
- Lists: bullets for contributions; inline (a)(b)(c) panel references everywhere.
- Parentheticals about 146; semicolons about 25; en dashes about 19, used for numeric ranges only ("200B-1000B"); no em dashes in prose.
- Italic or bold: numbered "Insight" stars as boxed, bold names.
- Hedging: low; "indeed", "clearly", "strong" appear; the caveat is carried in a stated scope sentence ("We expect greater speedups at larger EP scales").
- Numbers: ratios with x, then percent; averages and "up to" distinguished; tables show config parameters.
- Eight patterns:
  1. "If ___ were fully unpredictable, it would ___ for ___. From a temporal perspective, ___. From a spatial perspective, ___." (counterfactual)
  2. "Fortunately, as we later show in the paper, ___ indeed ___ that designers can exploit to ___." (thesis)
  3. "Yet as shown in Figure N, no prior work has systematically investigated ___." (gap)
  4. "★Insight N: ___ (ObM). Leverage ___ to ___." (insight box)
  5. "We follow Insight N to design ___ and leverage ___ to build ___." (insight to design)
  6. "In this work, we flip the process and adopt a ___ strategy by ___ to extract ___ insights." (reframing)
  7. "___ achieves ___x on ___, ___x on ___, and ___x on ___, respectively." (model-by-model result)
  8. "We note that our ___ inherently limits ___: with ___, ___. We expect ___ at ___." (scope statement)

## 9. Figures and tables
- First figure (Fig 1): bubble chart of MoE models by release date and parameter size, with zones "no study", "limited prior study", "first profiled in our work", and "released after our work". It comes first because it proves the gap visually and dates the paper's claim of being first. Fig 2 (stacked latency breakdown for DeepSeek V3 in three serving configs) then shows the cost is real.
- Caption style: states a takeaway plus a scope ("while our work presents the first comprehensive analysis of multiple unstudied SOTA models"); profiling figure captions end with the observation ("top 20% of the next-token expert already covers most of probability mass").
- Figures that carry the argument: Figs 4-6 (heatmaps and conditional CDFs with consistent layout across four models) and Fig 12 (throughput of five arms across three batch sizes, two hardware configs, four models, with hop reduction below).
- Tables: Table I hardware configurations (X-die, Y-die, DRAM BW, D2D BW, compute) for Dojo, TSMC-SoW, Dojo-Enhanced; Table II area and power per added module with a "total < 0.04%" line.

## 10. Why it reads as strong, and what does not transfer
Three writing moves to copy:
1. A counterfactual paragraph before the thesis (Intro P4 "If ... were fully unpredictable"): it makes the stake explicit and makes "Fortunately" in P5 carry the weight.
2. Observations labeled Ob1-Ob5 inside subsection titles and insights labeled 1-6 with pointers back to observations, then insight numbers cited in the case-study openings (III-B, III-C, IV-D); a reviewer can audit the chain.
3. Evaluation opens with simulator validation (V-B) and explains a saturating result with a diagnosis (hop count vs speedup in V-D), so the weak case becomes a finding.
Particular to this paper: the six MoE-specific insights and the heatmap profiling method, plus the wafer-scale chiplet details; none transfer. Also the paper has no system name, and the benchmark paper does need one.
