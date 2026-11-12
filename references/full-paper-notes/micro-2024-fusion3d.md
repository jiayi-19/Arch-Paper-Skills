# micro-2024-fusion3d: Fusion-3D: Integrated Acceleration for Instant 3D Reconstruction and Real-Time Rendering

Word counts below come from pdftotext output with figure and table text mixed in, so section sizes are approximate (plus or minus 15 percent, more for the experiments section). Sentence and paragraph statistics are from prose paragraphs only.

### 0. Identity
- Title: Fusion-3D: Integrated Acceleration for Instant 3D Reconstruction and Real-Time Rendering
- Contribution type: accelerator and system (end-to-end single chip, taped out in 28 nm, plus a four-chip PCB multi-chip system), with algorithm-hardware co-design.
- Pages: 14 (including references). Authors: Sixu Li and others, Yingyan (Celine) Lin's group, Georgia Tech.
- Full text used: https://par.nsf.gov/servlets/purl/10574254 (NSF Public Access Repository copy, the accepted manuscript; may differ slightly from the published version).

### 1. Skeleton
| Section | Words (approx.) | Figs / tables | Role |
|---|---|---|---|
| Abstract | 301 | 0 | |
| I Introduction | 1000 | 2 figs (Fig 1 application, Fig 2 pipeline) | setting, gap, approach, challenges, contributions |
| II Background, Motivations, and Challenges | 1500 | 1 fig (Fig 3), 2 tables | background (A), motivation 1 (B), challenges C1, C2 (C), motivation 2 (D), challenges C3, C4 (E) |
| III System Overview | 500 | 1 fig (Fig 4) | overview |
| IV Single-Chip End-to-End Acceleration | 1100 | 2 figs | design: techniques T1, T2 |
| V Multi-Chip for Enhanced Scalability | 900 | 2 figs | design: techniques T3, T4 |
| VI Experiments | 2000 prose | 5 figs, 4 tables | methodology and evaluation fused: A single chip, B multi-chip, C ablation, D integration |
| VII Related Works | 110 | 0 | related work (very short) |
| VIII Discussion and Future Work | 600 | 1 fig | discussion (chiplets, 3D stacked memory) |
| IX Conclusions | 85 | 0 | conclusion |

### 2. Abstract
- 10 sentences, about 300 words (the longest abstract of the four). Average 30 words per sentence.
- Functions in order: (1) setting, NeRF enables immersive AR/VR; (2) prior work gap, current NeRF acceleration is inadequate for two stated reasons (no end-to-end pipeline support causing impractical off-chip bandwidth; limited scalability); (3) approach, Fusion-3D named here, an end-to-end scalable framework; (4) mechanism, two key innovations spelled out as 1) and 2) in a 68-word sentence; (5) generic result claim; (6) evidence type, tape-out of a 28 nm prototype; (7) result, 2.5x training and 6x inference throughput versus state-of-the-art accelerators, "simulation based on on-silicon measurements"; (8) multi-chip evidence, four chips on a PCB; (9) result, 7.3x training and 6.5x inference throughput over an Nvidia 2080 Ti; (10) scope claim, first to achieve both instant reconstruction (2 seconds or less) and real-time rendering (30 FPS or more) at USB bandwidth (0.625 GB/s).
- Numbers: each speedup is scoped by baseline class and by evidence type (measured silicon versus simulation based on silicon). The last sentence carries three numbers and a first-ever claim. No energy numbers in the abstract (they appear in the introduction).

### 3. Introduction
- 4 prose paragraphs plus a 4-item contribution list; about 1000 words. Short compared with the others, because Section II does motivation.
- P1: setting. Opens "3D reconstruction from sparsely sampled 2D images" is a foundational AR/VR task; NeRF is state of the art, small storage, demand for instant training and real-time rendering at the edge. Ends with the trend to run NeRF at the edge.
- P2: edge devices cannot meet the requirements, so recent accelerators exist (credit: "These works propose tailored acceleration methods ... advancing the potential"). Ends crediting prior work, which makes the next "Despite" paragraph land.
- P3: problem posed as two requirements, 1) practical off-chip bandwidth and 2) scale-up strategy. Numbers make the gap concrete (prior accelerators assume 59 and 231 GB/s; common USB port is 0.625 GB/s; scaling up lowers yield).
- P4: "To overcome these challenges, we developed Fusion-3D": end-to-end accelerator that removes external memory access between stages, plus a multi-chip architecture as the alternative to a bigger chip. Then it says the two ideas alone do not solve the problem because of four challenges C1 to C4, introduced with a labeling convention for challenges and techniques (C1 to C4, T1 to T4). That label scheme is the setup for Sections II, IV, V.
- Contributions (4): 1 capability and number (first to support instant reconstruction and real-time rendering at 5 Gbps USB); 2 component and mechanism (first end-to-end single-chip NeRF accelerator, two techniques, taped out); 3 system and mechanism (multi-chip with three-level hierarchical tiling, four-chip PCB); 4 result with numbers (3.3x energy and 2.5x speedup training, 18.6x energy and 6x speedup inference for single chip; 304x/7.3x and 270x/6.5x for the multi-chip versus 2080 Ti). The results preview is item 4, not a separate paragraph. No roadmap paragraph.
- Key insight (the occupancy grid is a built-in gating function, so a mixture-of-experts split cuts chip-to-chip traffic) is not in the introduction; it first appears in II-A and V-A. Prior work is credited in P2 and dismissed by two quantified gaps in P3.
- Challenges device: yes, C1 inefficient sampling, C2 high precision requirements, C3 heavy chip-to-chip communication, C4 workload imbalance between chips. Phrased as noun-phrase labels.

### 4. Motivation and background
- Section II combines background (II-A), two numbered motivations ("Motivation 1: Bandwidth Limitation ...", "Motivation 2: Scalability Limitation ...") and challenge subsections.
- Evidence: measured data volumes per pipeline stage in training (Fig 3: 155 GB intermediate data per scene; bandwidth needed for a 2-second training), a table of prior accelerators' off-chip bandwidth next to three commercial edge platforms (Table I), a quantization experiment showing PSNR collapse (Table II), and a yield estimate (99 to 72 percent for a bigger chip, doubling cost per area).
- Observations end with a bridge sentence that turns the data into the design choice (only 700 MB of data is needed at the pipeline boundary, so process all stages on chip). Each challenge paragraph closes with a forward reference to the technique section.
- Mapping: one to one, C1 to T1, C2 to T2, C3 to T3, C4 to T4, repeated in Fig 4, in section headings and in the ablation.

### 5. Overview of the design
- Section III, about 500 words, with Fig 4: block diagram of (a) the single chip and (b) the multi-chip system, annotated with the challenges on the sides and techniques and section numbers on the blocks.
- The text walks the single-chip figure as a numbered list of six modules (Sampling, Feature Interpolation, Post Processing, Memory Clusters, Interface/Controller, NoC), tying each module to a challenge and technique and pointing to Sec IV, then the multi-chip system, pointing to Sec V.
- The key insight is deferred; the overview only says which technique answers which challenge.

### 6. Design sections
- Subsection pattern: technique heading with its label ("Technique T1: Optimized Sampling: ..."), what the challenge is, the mechanism with a figure, a consequence, and for T2 a local "Ablation Study for Technique T2" with area and power numbers. Sub-techniques are numbered T1-1, T1-2.
- Running examples are figures: Fig 5 normalizes a model into a unit cube and splits it into 8 cubes; Fig 7 shows three tiling levels (Level 1 expert per chip, Level 2 by offset group, Level 3 by address parity).
- Novelty claims are placed inline ("for the first time, finds and emphasizes that model normalization is vital ...").
- Details left out: hash function constants, controller thresholds; all stay in the text rather than an appendix.
- Figure types: block and dataflow diagrams, timing diagrams, tiling diagrams, a visual of which expert renders which pixels (Fig 8).

### 7. Evaluation
- Organized by platform, not by research question: VI-A single chip, VI-B multi-chip, VI-C ablation, VI-D integration. Bold run-in labels: "Evaluation Methodology", "Details of ...", "Evaluation Results of ...". Methodology is inside each subsection.
- First result: silicon measurement of the prototype (PSNR within 0.1 of the algorithm; 36 FPS rendering or 1.8 s training at 600 MHz; 1.21 W). The text then says that comparisons use a scaled-up simulated version calibrated on the chip.
- Claims bounded by baseline and kind of evidence. The abstract's 2.5x and 6x are against accelerators using the same algorithm; the body also gives 1.36x inference and 4.15x training against the best baseline of any algorithm, and 19x and 25x energy. Table III footnotes mark estimated, not reported (N/R) and not supported (N/S) cells.
- Ablations: T1 gives 5.4x to 20.2x per scene (Table VI); communication volume down 94 percent with Level 1; crossbar removed and feature-fetch latency variance becomes zero with Levels 2 and 3 (Fig 12); MoE PSNR and convergence matched against one large model (Fig 13); components reused on TensorRF.
- Weak points: the discussion admits that the I/O module area grows quickly with model size (Fig 14) and calls the best balance future work.

### 8. Sentence and paragraph habits
- Average sentence about 22 words (counted 22.3); prose paragraphs about 145 words (median 114). "We" about 14 per 1k words.
- Colons are frequent (about 8 per 1k) because of headings like "Technique T1:" and inline enumerations "1) ... 2) ... 3)" inside paragraphs. "Specifically," is the favorite connector (9 uses), then "Thus,".
- Parentheses about 18 per 1k; about 11 semicolons; about 6 em dashes. Hedging low. "To the best of our knowledge" and first-ever claims appear in the abstract, the first contribution, the conclusion and twice in the body.
- Numbers: with the multiplication sign, always with baseline named in the same sentence.
- Eight patterns:
  1. "Despite existing [X]'s promises, they still fall short in meeting two critical requirements imposed by real-world deployments: 1) [..] and 2) [..]."
  2. "It is worth noting that the aforementioned challenges cannot be effectively addressed by simply adopting [A] paired with [B]. The main reasons include [C1], [C2], [C3] and [C4]."
  3. "(here we use C1/2/3/4 for challenges and T1/2/3/4 for corresponding techniques)"
  4. "However, as indicated in Fig. [N], only [small number] of data transfer is required for [boundary]. Thus, to address the above issue, we propose ..."
  5. "Challenge C[N]: [Name]. [Recap from Sec. II]. To this end, we introduce [Technique T[N]] (see Sec. [N])."
  6. "We address this need from three perspectives: 1) ..., 2) ..., 3) ...."
  7. "To the best of our knowledge, [NAME] is the first to achieve both [A] and [B], while only requiring [C]."
  8. "Specifically, [NAME] achieves a [x]x energy saving and a [y]x speedup in [task], along with ..., compared to [baseline]."

### 9. Figures and tables
- Fig 1 shows the application scenario (user A's headset reconstructs from 100 MB of photos and sends a 10 MB model to user B, who renders it). It sits next to the abstract because it explains why bandwidth and edge-side reconstruction both matter, which the rest of the paper depends on.
- Captions are descriptive, except Fig 3 whose caption ends with the paper's position ("our work encompasses all stages to minimize inter-stage communication").
- Figures that carry the argument: Fig 3 (data volume per stage with prior design boundaries versus ours) and Fig 4 (challenge to technique to section map).
- Tables: Table I lines up prior accelerators and commercial edge platforms by off-chip bandwidth with the paper's own row last; Table III is a wide feature and efficiency comparison with seven system columns and the paper's last, with Yes/No cells for the claims (instant training, real-time inference, end-to-end).

### 10. Why it reads as strong, and what does not transfer
1. Full traceability labels: C1 to C4 in the introduction (P4), the Fig 4 map, headings "Technique T1" to "T4", and the ablation items in VI-C. A reader can find the evidence for each technique by its tag.
2. One table that frames the whole problem (Table I in Sec II-B): the bandwidth every prior accelerator needs against what real edge hardware offers.
3. Measured versus simulated is declared at the point of each result (Sec VI-A, VI-B method paragraphs; abstract sentences 6 to 9).
- Not to copy: the very long abstract, the unproved "first ever" density, tape-out specifics, 28 nm chip tables.

Quotations used (section): "Despite existing NeRF accelerators' promises, they still fall short in meeting two critical requirements imposed by real-world deployments" (I); "here we use C1/2/3/4 for challenges and T1/2/3/4 for corresponding techniques" (I); "only 700 MB of data transfer is required for the input and output of the entire pipeline" (II-B); "this work, for the first time, finds and emphasizes that model normalization is vital for end-to-end customized hardware" (IV-A); "integrates easily into existing AR/VR systems like a USB drive" (VI-D).
