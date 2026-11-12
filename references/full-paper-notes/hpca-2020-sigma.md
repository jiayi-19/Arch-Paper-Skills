# hpca-2020-sigma: SIGMA: A Sparse and Irregular GEMM Accelerator with Flexible Interconnects for DNN Training

Word counts below come from pdftotext output with figure and table text still mixed in, so section sizes are approximate (plus or minus 15 percent). Sentence and paragraph statistics are from prose paragraphs only.

### 0. Identity
- Title: SIGMA: A Sparse and Irregular GEMM Accelerator with Flexible Interconnects for DNN Training
- Venue and year: HPCA 2020. Award: Best Paper.
- Contribution type: accelerator (microarchitecture plus a small interconnect mechanism, FAN), with a workload characterization section and a place-and-route implementation.
- Pages: 13 (including references). Authors: Qin, Samajdar, Kwon, Nadella, Srinivasan, Das, Kaul, Krishna (Georgia Tech and Intel).
- Full text used: https://bpb-us-e1.wpmucdn.com/sites.gatech.edu/dist/c/332/files/2020/01/sigma_hpca2020.pdf (author-hosted, Georgia Tech Synergy lab site)

### 1. Skeleton
| Section | Words (approx.) | Figs / tables | Role |
|---|---|---|---|
| Abstract | 206 | 0 | |
| I Introduction | 1000 | 1 fig | setting, requirements, key idea, contributions, roadmap |
| II DL Training Characterization | 700 | 1 fig (Fig 2; Fig 1b is cited) | motivation (measured workload facts) |
| III Inefficiency of GPUs and TPUs | 1200 | 2 figs, 1 table | motivation plus the conceptual overview of the design (III-C) |
| IV SIGMA Architecture | 2000 | 4 figs | design (A Flex-DPE, B NoC composition, C sparsity, D dataflows, E walkthrough) |
| V Implementation | 700 | 1 fig (plus the Fig 8 comparison) | cost analysis (area, power, design-space exploration) |
| VI Evaluation | 1000 | 5 figs, 1 table | methodology (A) then results (B, C, D) |
| VII Related Work | 400 | 1 table (Table III) | related work |
| VIII Conclusion | 90 | 0 | conclusion (carries the RTL link) |

There is no discussion or limitations section and no appendix.

### 2. Abstract
- 9 sentences, about 206 words. Average sentence length 23 words.
- Functions in order: (1) setting, DL has transformed computing; (2) setting, DL is a genre of workloads; (3) key kernel is GEMM; (4) prior work, GEMM suits systolic designs such as tensor cores and TPU; (5) problem and gap, emerging GEMMs are irregular and sparse and map poorly to systolic arrays; (6) approach, SIGMA, named here, a flexible scalable architecture with high PE utilization regardless of shape and sparsity; (7) mechanism, the Forwarding Adder Network; (8) results, 5.7x vs systolic arrays on irregular sparse matrices and roughly 3x vs state-of-the-art sparse accelerators; (9) scope, an instance at 10.8 TFLOPS efficiency, 65.10 mm2, 22.33 W at 28 nm.
- Four of nine sentences (about half the words) are setting. There is no separate insight sentence; the insight is folded into the approach sentence ("high utilization regardless of kernel shape and sparsity").
- Numbers: 5.7x is scoped by "irregular sparse matrices" and by baseline (systolic arrays); "roughly 3x" has a baseline (state-of-the-art sparse accelerators) but no workload scope; the TFLOPS figure is scoped "across arbitrary levels of sparsity" and tied to a stated area, power and process node.

### 3. Introduction
- About 10 prose paragraphs, two 3-item bullet lists, a 4-item numbered contribution list and a roadmap paragraph. About 1000 words.
- P1: setting, DL and the training/inference split. Opens with "Deep learning (DL) has emerged as the premier algorithmic technique". Ends by defining inference.
- P2: inference accelerators already exist (credit, with citations), so training is the open question. Last sentence states the paper's focus. This is how the problem is posed: by scoping to training.
- P3: training compute is huge (300,000x growth cited); GPUs and company platforms. Ends on platforms, which sets up GEMM.
- P4: GEMM is the core kernel; forward and backward pass shapes; points to Fig 1.
- P5: GEMM is about 70 percent of cycles; state of the art is systolic arrays from 4x4 to 128x128; why they are efficient.
- P6: "architects need to be cognizant of three trends", then bullets: irregular shapes, varying sparsity (10 to 90 percent), fast-changing models.
- P7: "we recommend three key requirements for future GEMM engines", then bullets with bold labels: Flexibility, Sparsity Support, Scalability. These three words are reused as Table I rows and as the ablation arms in Sec VI.
- P8: dismisses GPUs and TPUs against those requirements with specific mechanisms (CUDA libraries need FP32 for sparse; the TPU is a rigid 128x128 grid; load and collect time grows with array side). Last sentence on scaling leads straight into the proposal.
- P9: "In this work, we demonstrate the microarchitecture of ... SIGMA": handles arbitrary sparsity and irregularity near full utilization. Key insight first appears here: a flexible dot-product engine on tree interconnects giving O(1) distribution and O(log N) reduction. Ends with the morphing description.
- P10: contribution list (4): 1 analysis of training workloads (finding), 2 the SIGMA accelerator (capability), 3 the FAN reduction network (mechanism), 4 layout implementation for scalability and backend analysis (component). None carries a number. A roadmap paragraph follows.
- No "challenges" device; the "trends then requirements" pair plays that role. No results-preview paragraph; all numbers are left to the abstract and Sec VI. Prior work is credited in P2 and dismissed only for GPU and TPU in P8; other accelerators wait until Table III.

### 4. Motivation and background
- Two separate sections, II and III, both measured or worked analytically. Evidence: a time-breakdown on V100 for Transformer and GNMT (Fig 2, about 70 percent matrix multiply); GPU efficiency for dense irregular, FP16 tensor cores and cuSPARSE at 50 and 80 percent sparsity (Fig 3, about 4x efficiency drop with sparsity); real GEMM shapes (Fig 1b); sparsity levels from their own pruning runs.
- Observations end with an explicit "Thus," takeaway sentence ("Thus, MatMul is a key compute primitive to accelerate in hardware to speed-up training."). Sec III-C ends with a Summary paragraph pointing at Table I.
- Mapping to the design is one to one through Table I (Goal, systolic limitation, SIGMA structure, property) with forward references such as "as we describe later in Sec. IV".

### 5. Overview of the design
- No Overview section. Sec III-C plays that role: Fig 4 runs three tiny GEMMs (dense regular, dense irregular, sparse irregular) through a systolic array and a Flex-DPE side by side, with measured boxes for utilization, runtime, multicast and SRAM traffic. The text walks the figure case by case (bold run-in labels "Dense Regular Matrices", "Dense Irregular Matrices", "Sparse Irregular Matrices", "Distribution and Reduction Latency"), assuming "two specialized networks" whose details are deferred to Sec IV.
- Sec IV opens with one paragraph naming the hierarchy (Flex-DPE, NoC, Flex-DPU) and pointing at Fig 8. Key insight is handled by showing it work in Fig 4 before describing it.

### 6. Design sections
- Subsection pattern for the networks: role of the component, candidate options (spatio-temporal, temporal, spatial reduction; crossbar, bus, tree, butterfly, mesh, Benes), the chosen one, the specific problem it cannot solve alone (non-power-of-two dot-product groups), the fix (FAN with pseudocode and routing rule), then benefits and overhead with numbers (512-PE FAN costs 10 and 31 percent area and power over linear, versus 92 and 86 percent for the MAERI reduction tree).
- Worked example: Sec IV-E is a seven-step walkthrough (Step i to vii) of one sparse GEMM through bitmaps, counters and routing bits, keyed to Fig 5.
- Names stay stable (Flex-DPE, Flex-DPU, FAN, Benes, bitmap). What flows between components is stated in terms of what is stationary and what is streaming (dataflow labels like N-sta, M-str).
- Left out: Benes routing algorithms (cited), alternative compression formats ("only changing the front end controller"). Reference RTL link at the end.
- Figure types: toy-mapping diagrams, topology and pseudocode, block diagram with comparison table, design-space bar charts.

### 7. Evaluation
- Organized by what is measured, not by research question: A methodology (target GEMMs, baselines scaled to a constant 16384 PEs, cycle-accurate analytic model, Table II metrics), B characterizing SIGMA's features, C versus TPU, D versus sparse accelerators.
- First result: dataflow comparison (Fig 10), a design-point result, not the headline. The headline speedup arrives third.
- Ablation: Fig 11 adds the three features one at a time (SIGMA Fl, Fl+Sc, Fl+Sc+Sp) on top of a TPU; it reuses the flexibility, scalability, sparsity words of the intro.
- Claims are bounded by "on average", baseline (128x128 TPU at the same PE count) and workload class (dense or sparse). Headline numbers: 2x dense, about 6x sparse, 3x energy and 5x area efficiency for sparse workloads, 3x over other sparse accelerators.
- Negative results: stated and explained (SIGMA is slower than Eyeriss v2 on two GEMMs because Eyeriss buffers both operands; small GEMMs are bandwidth bound). Cost is stated in Sec V: 37.7 percent area overhead, offset by 3.2x effective TFLOPS per watt.

### 8. Sentence and paragraph habits
- Average sentence about 18 words (counted 17.7); prose paragraphs about 150 words (median about 125). Present tense for the design, active "we" about 12 per 1k words (the lowest of the four papers), many passives.
- Paragraph openers: topic sentence or bold run-in label. Bold labels in Sec II ("Target Workloads.", "Sparsity within GEMMs."), Sec IV ("Spatial Reduction:", "FAN Topology."), Sec VI ("Baseline Accelerators.").
- Roughly 17 semicolons, one dash (hyphen used as a dash a few times), about 20 parentheses per 1k words. Hedging is almost absent (2 hedge words in the whole paper). Numbers carry the multiplication sign and "on average".
- Eight patterns:
  1. "Based on our observations, we recommend [N] key requirements for future [X] engines."
  2. "Unfortunately, state-of-the-art [A] and [B] fare poorly on some of the requirements, as we discuss later in Sec. [N]."
  3. "In this work, we demonstrate the microarchitecture of a [adjective] and [adjective] [X] named [NAME] that can handle (a) [..], (b) [..], while guaranteeing close to full utilization."
  4. "[NAME]'s key novelty is a highly [adjective] [component] that can map [workload] via a rich [fabric]."
  5. "Thus, [X] accelerators need [capability] to handle both [A] and [B] efficiently."
  6. "The challenge with realizing this [property], however, is that [case] is hard to map over [traditional structure]."
  7. "To address this issue, we propose a novel [structure] named [NAME] that places [element] between [levels] over a traditional [base]."
  8. "Of all the [class], [NAME] is the only one that can [capability]."

### 9. Figures and tables
- Fig 1 shows the GEMM operation and a table of real M, N, K shapes from DL workloads. It comes first because the whole argument rests on shapes being irregular in real models; the caption is descriptive.
- Fig 4 (toy GEMMs through systolic array versus Flex-DPE with quantitative boxes) carries the argument; Fig 11 (progressive features) is the ablation.
- Captions: mostly descriptive; a few carry the takeaway ("Matrix Multiply consume around 70% of total runtime.").
- Table I is a four-column map from desired feature to systolic limitation to SIGMA structure to property. Table III repeats the pattern for each prior accelerator (limitation, SIGMA solution).

### 10. Why it reads as strong, and what does not transfer
1. Three named requirements set in the introduction (P7) and then reused unchanged as the Table I rows, the Sec III subsections and the ablation arms in Fig 11 (Sec VI-B). The reader sees one set of words from problem to proof.
2. A toy example before any design detail (Fig 4 in Sec III-C): the same three matrices run through a systolic array and through the proposed engine, so the gap is visible with numbers in boxes before the architecture is described.
3. Cost and losses stated openly: 37.7 percent area overhead (Sec V) tied to the 3.2x efficiency gain, and the two GEMMs where Eyeriss v2 wins (Sec VI-D).
- Not to copy: Benes and FAN topology detail, area and power tables, the idea that the key idea must be a hardware structure.

Quotations used (section): "is still an open question, which is the focus of this work" (I); "Based on our observations, we recommend three key requirements for future GEMM engines." (I); "Unfortunately, state-of-the-art GPUs and TPUs fare poorly on some of the requirements" (I); "Thus, MatMul is a key compute primitive to accelerate in hardware to speed-up training." (II); "is that non-powers of two sized reductions are hard to map" (IV-A).
