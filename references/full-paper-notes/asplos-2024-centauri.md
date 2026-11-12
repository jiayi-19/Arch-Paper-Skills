# asplos-2024-centauri: Centauri: Enabling Efficient Scheduling for Communication-Computation Overlap in Large Model Training via Communication Partitioning

Source read: the authors' ACM-format PDF (ASPLOS '24). Counts are estimates from pdftotext; figure text was noisy and excluded where possible.

## 0. Identity
- Title: Centauri: Enabling Efficient Scheduling for Communication-Computation Overlap in Large Model Training via Communication Partitioning
- Venue and year: ASPLOS 2024 (29th ASPLOS, Volume 3, La Jolla). Award: Best Paper.
- Contribution type: system or framework (a partition abstraction plus a hierarchical scheduler, implemented in Megatron-LM).
- Pages: 14 (about 11 pages of body and references to follow).
- Authors: Chen, Li, Zhu, Duan, Sun, Zhang, Yang (Peking University, CUHK, Shanghai AI Lab).
- Full text used: https://jf-d.github.io/files/Centauri.pdf

## 1. Skeleton
Numbered sections with numbered subsections (2.1, 3.1.1 etc). Body prose about 5,800 words.

| Section | Approx words | Figures / tables | Role |
|---|---|---|---|
| Abstract | ~165 | 0 | summary |
| 1 Introduction | ~1,100 (5 paragraphs + 4 bullets) | Fig 1, Table 1 | problem, challenges, insight, contributions |
| 2 Background (2.1 Collective Communication, 2.2 Hybrid Parallel Training, 2.3 Motivations) | ~1,100 | Fig 2 | background plus a short analytic motivation |
| 3 Overview (3.1 Communication Partition; 3.2 Hierarchical Scheduling) | ~3,000 | Fig 3 (overview), Tables 2-3, Figs 4-7, Algorithm 1 | overview text of about 250 words, then design |
| 4 Implementation | ~150 | 0 | methodology of the build |
| 5 Evaluation (5.1 Single Parallel, 5.2 Hybrid, 5.3 Scalability, 5.4 FSDP Case Study) | ~1,500 (excluding figure text) | Table 4, Figs 8-14 | methodology + results |
| 6 Related Work | ~220 | 0 | related work (two run-in paragraphs) |
| 7 Conclusions | ~140 | 0 | conclusion with future work |

Totals: 14 figures, 4 tables, 1 algorithm. Section 3 is more than half of the body. The Overview is the head of Section 3 and has no heading of its own below it.

## 2. Abstract
- 9 sentences, about 165 words, two paragraphs (the second begins at "This paper introduces Centauri").
- Functions: (1) setting, LLM training needs hybrid parallelism and many collectives; (2) problem, communication bottlenecks are crucial and are handled by overlap; (3) prior work and gap, "However, existing overlap methodologies tend to lean towards either fine-grained kernel fusion or limited operation scheduling"; (4) approach, "This paper introduces Centauri, an innovative framework..."; (5) mechanism one, a partition space of three dimensions (primitive substitution, topology-aware group partitioning, workload partitioning); (6) consequence, they "create a comprehensive optimization space"; (7) mechanism two, scheduling decomposed into three tiers (operation, layer, model); (8) effect, overlap hides communication latency and raises utilization; (9) result, "up to 1.49× speedup over prevalent methods across various parallel training configurations."
- One number only, 1.49x. Scope: "up to", "prevalent methods", "various parallel training configurations", with no hardware or model named.
- System named in sentence 4, after setting, problem and gap (three sentences).
- Quote (Abstract): "existing overlap methodologies tend to lean towards either fine-grained kernel fusion or limited operation scheduling"

## 3. Introduction
- 5 prose paragraphs plus lead-in and 4 bullets; about 1,100 words.
- P1: setting. Opens "Recent advancements in LLMs have brought about a revolution"; chain: scaling law, cost, parallelism methods (DP, TP, PP, FSDP, ZeRO). Ends "Thus, minimizing communication overheads is crucial for the efficient scaling-out", setting up overlap.
- P2: prior work in three buckets (single-method schedulers; multi-stream concurrent communications; kernel-fusion compilers), each dismissed with one limit and a pointer to Fig 1 (a) and (b). Opens "Simultaneous execution of computation and communication operations is vital". Ends with the Fig 1 example where fused kernel B finishes later than MatMul B.
- P3: "These limitations underscore two fundamental challenges in optimizing overlap in LLMs training." First challenge answered by "a key insight: communication inherently is a mapping transformation (primitive) of workload across a group of devices", yielding three dimensions. Second challenge answered by "the repetitive layer-wise architectures of LLMs" yielding three tiers. Table 1 compares frameworks by these dimensions and shows their spaces are subsets.
- P4: "This paper introduces Centauri, a training system..." two components, partitioning and scheduling; then each dimension in one sentence.
- P5: "With a comprehensive partition space, efficient scheduling... can unlock" the scheduling tiers one sentence each. Ends on "small searching overheads".
- Contributions: "This paper makes the following contributions:" 4 bullets. (1) abstraction (a capability or component: "novel communication partition abstraction"); (2) decoupling of the scheduling space into 3 tiers with a one-clause role per tier; (3) implementation in Megatron-LM (a system artifact, new reducer, optimizer, pipeline scheduler); (4) evaluation with two numbers, 1.45x single and 1.49x hybrid.
- Results preview is only in bullet 4 (no separate paragraph); stated with "up to" and the compared set ("prevalent methods").
- "Challenges" device: yes, two challenges, each immediately paired with its answer in the same paragraph ("The first challenge... To tackle this, we propose a key insight"). This is a challenge-answer pair, not a challenge list followed by solutions.
- Problem posed: overlap spaces in prior work are either too coarse or too fine; the paper widens the space with partitioning and then tames it with hierarchy.
- Insight first appears in the introduction (P3), not in the abstract.
- Intro contains Fig 1 (three timelines of the same FSDP layer) and Table 1.

## 4. Motivation and background
- Background Section 2 is separate, mostly terminology (collectives; hybrid parallelism with Fig 2 showing forward and backward workflow with all collectives).
- Motivation is a short subsection 2.3 "Motivations" of about 300 words. Evidence is analytic, not measured: two dependency types (sequential and non-sequential), each with an example read off the overview figure (Fig 3), then "partitioning significantly expands the optimization space".
- Observations end with a forward-looking sentence, not a takeaway box. There is no measured motivation figure.
- Tie to design: the numbered circles in Fig 3 (steps 1 to 6) are referenced inside the motivation text, so the motivation is a pre-walk of the overview figure.

## 5. Overview of the design
- Section 3 "Overview" begins with a short paragraph (about 150 words) stating the workflow: communication partition (three dimensions) and hierarchical scheduling (three tiers), and that each collective is assigned to a tier. The figure for the overview (Fig 3) appears earlier, at the end of Section 2.
- Fig 3 shows a worked DP plus FSDP training example as a before-and-after timeline: "Original scheduling pattern" versus hierarchical scheduling, with circled steps 1 to 6 (primitive substitution, group partition, workload partition, operation scheduling, layer scheduling, model scheduling). The caption explains all six steps in one sentence each, so the figure is self-contained.
- Text walks the figure in numbered steps; challenges map to techniques (challenge 1 to dimensions 1-3, challenge 2 to tiers 4-6).
- Forward references are explicit ("discussed in Section 3.2.1").
- The key insight is restated in the overview as "A collective operation fundamentally acts as a mapping transformation".

## 6. Design sections
- Subsection pattern: define the dimension or tier, give the space and a pruning rule ("Some substitutions... are pruned from partition space"), then the choice rule. In 3.2 each tier opens with its scope ("The operation level focuses on...") and ends with a cost equation or algorithm.
- Worked example: Figs 1, 3, 5 re-use the same FSDP layer with labeled chunks A, B, C, D; Fig 5 gives five scheduling variants (a-e) of the same case, showing coarse, over-fine, bad order, good order, selected. Fig 7 does the same for pipeline scheduling with memory cost labeled (4x, 8x, 16x).
- Names stay stable: primitive, group, workload (dimensions); operation, layer, model (tiers). Triplets are repeated in abstract, intro, overview, design headings, conclusion.
- Between components: partition output (the leaf of the partition tree with minimal scheduling cost) feeds the scheduling tiers; the text says the "execution cost of optimized forward and backward phases jointly influences the model-level scheduling".
- Left out: pruning rules and cost models are compact; Implementation is only 150 words.
- Figure types: timeline diagrams, a partition-tree workflow (Fig 4), an algorithm listing (Algorithm 1), three small equations.

## 7. Evaluation
- Not organized by research question. Organized by workload type. Opening says it has "four parts" in a single sentence: single parallel tasks, hybrid tasks (called an ablation study in the text), scalability, a case study.
- First result: Fig 8, FSDP/ZeRO3 throughput vs micro-batch size across four LLaMA sizes, with speedups labeled over the baseline on bars.
- Bounding: baselines named and ported to Megatron-LM "to neutralize the impact of unrelated frameworks' techniques"; metric defined (FLOPs per GPU over end-to-end time); testbed (two clusters A and B) in the first paragraph.
- Ablation: in Fig 10 the bars separate "Centauri FSDP", "Centauri DP" and "Centauri both", and Fig 11 separates PP+TP overlap, PP+DP direct overlap, and Centauri scheduling; the ablation is by overlap type, not by removing one component at a time.
- Weak results: small batch sizes give limited gain ("the scope for performance improvement is limited"); Cluster B "nearly 5%"; OOM cases of baselines "are omitted" from the figure. The text explains each weak case with a bandwidth-to-compute ratio.
- 5.4 gives a theoretical bound (speedup limit min(1/alpha, 1/(1-alpha))), an unusual closing move that explains the headline number.

## 8. Sentence and paragraph habits
- Average sentence length: about 25-27 words on prose (script: 26.8, rough).
- Paragraph length: 4-8 sentences; long design paragraphs.
- Person and tense: present tense; "we" about 29 times in 5,800 words; the system is the subject in many sentences ("Centauri leverages...").
- Topic sentences: stated; paragraphs often close with a "Therefore" or "Consequently" sentence.
- Bold run-in headings: few; used for "Testbed", "Model and Metric", "Baseline", and in Related Work.
- Lists: bullets for collectives, dependency types, dimension types, baselines, contributions.
- Parentheticals: about 50. Semicolons: about 2. Em dashes: none. En dashes: none in prose. Very plain punctuation; commas carry the sentences.
- Hedging: modest "may", "might", "potentially" in the prior-work critique ("Fine-grained kernel fusion may potentially overlook...").
- Numbers: speedups as "1.49x" with "up to"; Figure labels carry the per-bar speedup.
- Eight patterns:
  1. "However, existing ___ tend to lean towards either ___ or ___, constraining ___." (abstract gap)
  2. "These limitations underscore two fundamental challenges in ___." (challenge device)
  3. "The first challenge revolves around ___. To tackle this, we propose a key insight: ___." (challenge to insight)
  4. "This paper introduces ___, a ___ designed to ___ through ___." (naming)
  5. "We decouple ___ into 3 hierarchical tiers: ___, ___, and ___. They focus on ___, ___, and ___, respectively." (contribution item)
  6. "At the ___ level, ___ is essential to ___. At the ___ level, ___." (parallel tier walk)
  7. "In summary, the workflow abstraction of ___ is illustrated in Fig N." (closing a subsection)
  8. "Therefore, ___ with proper ___ is the key issue." (takeaway after a figure comparison)

## 9. Figures and tables
- First figure (Fig 1): three timelines (a direct scheduling, b kernel fusion, c Centauri) of the same FSDP layer with the same chunk labels. It comes first because it is both the problem (idle gaps in a, late fused kernel in b) and the solution (c). Caption is descriptive and defines a, b, c.
- Table 1 (second evidence object, in the intro): rows are prior frameworks, columns are the four dimensions (primitive, group, workload, scheduling), check marks; shows prior spaces are subsets. This gives novelty in one glance.
- Fig 3 (overview): before-and-after timeline with circled steps; carries the whole method. Fig 5: five variants of one scheduling decision. Fig 12: operator-level overlap patterns for three batch sizes.
- Table design: Table 2 lists primitives and sub-primitives with a scalability check, Table 3 lists operations by dimension types; both short reference tables.
- Captions: mostly descriptive, with long captions for Figs 3, 5 and 7 that spell out the sub-panels.

## 10. Why it reads as strong, and what does not transfer
Three writing moves to copy:
1. One toy example (a four-matmul FSDP layer) reused across Figs 1, 3, 5, 12, so each new idea is a change to a picture the reader already knows (Intro Fig 1 through Section 5.4).
2. Challenge-answer pairing in the intro (P3): each challenge is followed by its insight in the same paragraph, and each insight becomes a named triplet reused throughout.
3. The comparison Table 1 in the introduction that shows prior work as subsets of the proposed space, which turns "novelty" into a checkable statement.
Particular to this paper: the three-tier scheduling with closed-form cost equations (Eq 1 and 2) depends on GPU stream semantics and should not be copied.
