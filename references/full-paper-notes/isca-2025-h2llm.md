# isca-2025-h2llm: H2-LLM: Hardware-Dataflow Co-Exploration for Heterogeneous Hybrid-Bonding-based Low-Batch LLM Inference

### 0. Identity
- Title: H2-LLM: Hardware-Dataflow Co-Exploration for Heterogeneous Hybrid-Bonding-based Low-Batch LLM Inference
- Venue and year: ISCA 2025 (52nd), Tokyo. Award: Best Paper.
- Contribution type: accelerator plus co-design plus automation (an architecture, a dataflow abstraction, and a design-space-exploration framework, code open-sourced). It is a co-design paper with a DSE tool, not a mechanism paper.
- Pages: 17 (body and conclusion end on page 13, artifact appendix on pages 13-14, references from page 14).
- Full text used: https://chenzhangsjtu.github.io//files/2025-H2_LLM_ISCA25.pdf (author-hosted ACM-format PDF). Text extracted with pdftotext and read in full (two-column layout, figure text is noisy, section word counts below are approximate and include some figure text).

### 1. Skeleton
| Section | Role | Approx words | Figures / tables |
|---|---|---|---|
| Abstract | abstract | about 210 | 0 |
| 1 Introduction | problem, gap, contributions | about 700 | 1 fig (edge LLM services, 3 use cases) |
| 2 Background (2.1 Transformer LLMs, 2.2 LLM inference on edge, 2.3 Heterogeneous NMP accelerators) | background | about 900 | 1 fig, 1 table (workload lengths of 4 datasets) |
| 3 Motivation (3.1 limits of in-die NMP, 3.2 "Hybrid Bonding to the Rescue?", 3.3 limits of existing dataflow designs) | motivation, ends with the "we propose" hand-off | about 1,200 | 2 figs (roofline, HB overview plus area overhead), 2 tables (commodity NMP specs, dataflow comparison) |
| 4 H2-LLM's Architecture (4.1 overview, 4.2 NMP operator execution flow, 4.3 command interface, 4.4 architecture design space) | design (hardware) | about 1,500 | 2 figs (architecture overview, intra-channel flow) |
| 5 Dataflow Abstraction (5.1 operator-channel binding, 5.2 computation-engine choice, 5.3 layer execution flow, 5.4 dataflow design space) | design (software/dataflow) | about 1,500 | 2 figs (binding example, decode timeline) |
| 6 DSE Framework (6.1 overview, 6.2 exploration engine (genetic algorithm), 6.3 compilation flow) | design (tool) | about 800 | 1 fig, 1 table (model configs) |
| 7 Evaluation (7.1 methodology, 7.2 comparison with baselines, 7.3 performance analysis, 7.4 DSE analysis) | methodology plus evaluation | about 2,900 | 12 figs (Figs 10-21), 3 tables |
| 8 Conclusion | conclusion (one paragraph) | about 115 | 0 |
| Appendix A | artifact description | about 480 | 0 |

Totals: 21 figures, 7 tables. There is NO separate Related Work section and NO Discussion or Limitations section. Prior work is credited and dismissed inside Section 2.3 and Section 3. Evaluation methodology is a subsection of Evaluation, not its own section.

### 2. Abstract
- About 9 sentences, about 210 words (one paragraph with two visual breaks in the PDF: setting plus problem, then solution).
- Sentence functions in order: (1) setting: low-batch LLM inference on edge, with four example applications; (2) prior approach: NMP heterogeneous computation handles prefill and decode; (3) gap: existing NMP puts engines inside DRAM dies, so computation capacity is low, so it cannot accelerate low-batch edge inference; (4) approach: "we propose H2-LLM", named here with an expansion of the acronym; (5) mechanism 1: architecture plus its design space, justified by the compute-vs-bandwidth trade-off of hybrid bonding; (6) mechanism 2: data-centric dataflow abstraction; (7) mechanism 3: DSE framework to find the optimal design; (8) result: 2.72x geomean speedup and 1.48x geomean energy efficiency; (9) artifact: open-source link.
- Numbers: two, both stated in sentence 8 with scope "compared with existing in-die NMP-based heterogeneous accelerators" and "geomean". No workload list or model list in the abstract.
- System named in sentence 4 (about the middle), after the gap, with the full phrase "Hybrid-bonding-based Heterogeneous accelerator for edge-side low-batch LLM inference".
- The abstract uses no motivating number; the problem is stated qualitatively.

### 3. Introduction
- 6 paragraphs plus a 4-item bullet list, about 700 words. Single problem-solution arc.
- P1 (setting): opens with "Generative LLMs ... have demonstrated outstanding ability"; says LLMs sink to the edge; defines the low-batch property (one to a few tens) and low latency. Ends with the property that sets up P2 (low batch plus low latency).
- P2 (background plus prior work credit): opens with "Performing efficient LLM inference requires the hardware to effectively handle its two stages"; explains prefill vs decode; says NMP heterogeneous designs (many citations) work well for cloud. Ends with credit ("notable performance improvements in cloud-level"), which sets up the "However" in P3.
- P3 (gap 1, in-die NMP): opens "However, existing NMP designs typically place NMP processing engines into DRAM dies", gives two numbered reasons ("First ... Second ..."): speedup shrinks with batch size; attention variants raise arithmetic intensity. Dismisses the closest prior work (Duplex) in one sentence for HBM power. Ends by naming HB as promising alternative (hand-off).
- P4 (opportunity and challenges): opens "The recent emerging hybrid bonding (HB) technology ... seems to be a promising alternative". Then "However, there are still several challenges" with two challenges, labeled by "For architecture design ... As to dataflow design ...": controller area vs bandwidth; fixed operator mapping and prefill-unaware exploration. Ends on the dataflow challenge, which sets up the solution paragraph.
- P5 (solution plus contributions): opens "To tackle these challenges, we propose H2-LLM"; says "first work aiming to comprehensively explore the computation-bandwidth trade-off"; then three-part solution; "To summarize, we have made the following contributions:".
- P6 (results preview): one sentence, "Extensive experiments demonstrate that H2-LLM outperforms ... by 2.72x (geomean) speed up and 1.48x (geomean) better energy efficiency." No roadmap paragraph at the end.
- Problem posing: workload property (edge, low-batch) leads to hardware mismatch (in-die NMP has low compute) leads to technology answer (hybrid bonding) leads to two open design problems. The key insight (compute-bandwidth trade-off of HB must be explored together with a data-centric dataflow) first appears in P4's challenge sentences, in plain form, and is named in P5.
- Prior work: credited for cloud success, dismissed by a specific limit (low compute capacity, fixed mappings, prefill-unaware), with citation numbers attached.
- "Challenges" device: yes, but embedded in P4 as "several challenges", two of them, headed by "For architecture design" and "As to dataflow design". Not a bulleted list.
- Contribution list: 4 bullets. (1) a characterization/finding ("We analyze the deficiencies of in-die NMP ... and pose the chances and challenges of hybrid bonding"); (2) a component plus design space (architecture); (3) a mechanism/abstraction (data-centric dataflow); (4) findings ("summarize several takeaways ... case studies"). None carries a number. The one result sentence follows the list.
- Results preview: one sentence, two geomean numbers, baseline named ("existing in-die NMP-based heterogeneous accelerators"), identical to the abstract.

### 4. Motivation and background
- Two separate sections: Background (Section 2) is textbook (transformer, edge inference, NMP) and ends with prior-work description. Motivation (Section 3) is separate.
- Evidence: Section 3.1 is a measured/analytical roofline of LLaMA3 8B on 8 LPDDR5-PIM channels (Fig. 3) plus a spec table of four commodity NMP products (Table 2). Section 3.2 uses the authors' own 40 nm implementation to show the controller takes about 40% of logic die area at 1024 pins (Fig. 4b). Section 3.3 uses a qualitative comparison table of prior dataflow designs (Table 3) and reasoning.
- Each sub-subsection ends by stating the conclusion in words, e.g. "Therefore, it is necessary to enhance NMP PE's computation capacity". No insight boxes. 3.2 ends with the unresolved trade-off ("which is still lack of discussion"), and 3.3 ends with the plan "In the following sections, we will introduce ...".
- Tie to design: loose forward mapping. Problem 1 (compute capacity) maps to architecture and its design space (Sec 4); Problem 2 (fixed mapping, prefill-unaware, fission) maps to dataflow abstraction (Sec 5); Sec 3.3 names "prefill-aware" and "operator fission", which are exactly the terms Sec 5 and Table 3 use. No explicit "Observation 1 / Insight 1" labels.

### 5. Overview of the design
- No Overview section. The design is introduced by (a) the last paragraph of Section 3 ("To tackle these challenges, we propose H2-LLM ... In the following sections ... architecture design, dataflow abstraction, and the DSE framework") and (b) Section 4.1 "Architecture Overview", about 350 words, with Figure 5 (a: overall system with a centralized processor and HB-NMP channels; b: memory die and logic die; c: PE architecture). The text walks the figure by component (centralized processor, memory system, memory die modes, logic die, PE).
- Section 6.1 gives a framework overview with Figure 9 (inputs, model parser, exploration engine, outputs) walked as three inputs then flow. The genetic-algorithm workflow in 6.2 is walked with circled step numbers.
- The key insight is not placed in a separate overview; it is carried by the section titles and by the contribution list.

### 6. Design sections
- Pattern: Section 4 (hardware) then Section 5 (dataflow) then Section 6 (the tool that searches both). Each section ends with a "design space" subsection (4.4 and 5.4): a list of knobs that the DSE then searches. This is the stable pattern: mechanism, then the knobs it exposes.
- Naming: acronyms are defined once and reused (MAG, MPG, GCMap, OCMap, HB-NMP, ID-NMP). Named steps ("Step 1: Memory Access Group Partition", "Step 2: Coarse-grain binding", "Step 3: Fine-grain binding") use bold run-in headings.
- Worked example: "Binding Example" paragraph walks a parallel transformer on 6 NMP channels plus 2 normal channels through the three steps (Fig. 7), then Fig. 8 shows its decode timeline. The example is attached directly after the formal definition.
- Moving between components: the execution model (offload: scatter inputs, compute, merge) is the thread; the architecture section ends with a command interface; the dataflow section decides which engine runs each operator; the DSE section samples both. Section 5 opens by saying the abstraction "is not constrained to H2-LLM's architecture" (generality claim).
- Left out: operator templates for NMP are admitted to be manual ("will be our future work"); simulator internals are one paragraph in the evaluation; artifact details go to Appendix A.
- Figure types: system block diagrams, an abstract operator-graph diagram with partition boxes, a timeline, and a flow diagram of the GA. Equations are used for the tiling model (Eq. 1) and for the formal MAG/GCMap/OCMap definitions.

### 7. Evaluation
- Not organized by research question. It is organized by subsection: 7.1 methodology (benchmarks, system configuration, baselines, simulation), 7.2 comparison with baselines, 7.3 performance analysis (vs. existing dataflow designs; architecture exploration; tiling overhead), 7.4 DSE analysis (each design dimension).
- Claims are bounded by naming the baseline and the aggregation: "(geomean)" after almost every number; normalization stated ("All results are normalized to ID-NMP+"). Scenario names (decode-heavy HE/SG, prefill-heavy LB/LG, mixed).
- First result: end-to-end latency and decoding energy vs. three baselines (CP only, ID-NMP, ID-NMP+) in Fig. 10, with the 2.71x headline stated against ID-NMP+.
- Ablations: the dataflow ablation compares against four prior dataflow designs on the same fixed H2-LLM hardware (Attn-NMP, Attn-NMP-Split, FC-NMP, CC-NMP). Architecture ablation is one-dimension-at-a-time sweeps in 7.4 with the other parameters fixed and stated.
- Negative or weak results: reported plainly and attributed; e.g. the in-die NMP (ID-NMP) falls below the centralized-only design at batch 16 (71%), and the prior compute-centric mapping is about 5% worse than FC-NMP in one case. Overhead of synchronization and data transfer is reported as a range (1.6% to 15.7%). The paper does not report cases where H2-LLM itself loses.
- Sweeps end with numbered "Takeaway" boxes (Takeaways 1-6), each a one-sentence design rule, which turns the sweep results into transferable statements and satisfies the fourth contribution bullet.

### 8. Sentence and paragraph habits
- Average sentence length: about 24 words in the design and evaluation text, about 30 in the introduction (script estimate on extracted text, rough).
- Paragraph length: long, 90-180 words in the body, with no one-sentence paragraphs except the results sentence in the intro.
- Person and tense: "we" about 80 times in the body; present tense for the design and for results ("H2-LLM achieves ..."); "we propose" repeated. "Our" is rare.
- Topic sentences: often a bold run-in heading ("Intra-Channel Execution:", "Comparison with Baselines:") then a plain statement.
- Emphasis: bold run-in headings; no italics for emphasis; boxed "Takeaway N:" lines.
- Lists: numbered inline "(1) ... (2) ..." and "First, ... Second, ..." inside paragraphs; one bullet list (contributions).
- Parentheticals: very heavy (about 180 in the body), mostly for definitions, citations, and "(i.e., ...)" clarifications.
- Semicolons: essentially none. Em dashes: none. En dashes: only in numeric ranges.
- Hedging: very low; "can" and "typically" are the main softeners. Claims are plain. The text has some non-native phrasing ("find out the optimal design"), and it still won.
- Numbers: stated as "X.XXx (geomean)" with the baseline right next to it; ranges with hyphens ("12%-26%").
- Eight sentence patterns:
  1. "However, existing [class of designs] typically [do X], providing [low Y] due to [reason]."
  2. "To tackle these challenges, we propose [name], a [one-line description]."
  3. "[Name] is the first work aiming to comprehensively explore [trade-off] for [workload]."
  4. "For [area A], [problem]. As to [area B], [problem]." (challenge pair)
  5. "Therefore, [balancing / enhancing X] is vital to [goal]."
  6. "We can find that [result], because [mechanism]." (result plus reason)
  7. "[Name] achieves [N]x (geomean) speedup under [scenario A] and [M]x under [scenario B]."
  8. "Takeaway N: With the increase of [variable], the [component] should be designed with [consequence]."

### 9. Figures and tables
- First figure (Fig. 1) shows three edge-side LLM services (personal chat, virtual assistant, reception bot) beside a cloud service, labeled with batch sizes "a few tens (10-20)" and "hundreds". It comes first because the whole paper rests on the claim that edge is low batch; it makes the setting concrete before any hardware appears.
- Captions are short descriptive labels ("Figure 5: H2-LLM's Architecture Overview"), not takeaway statements. The takeaway lives in the text.
- Carrier figures: Fig. 3 (roofline of in-die NMP with batch size and KV head count; shows the point where in-die NMP stops helping) and Fig. 4b (controller area versus pin count) carry the motivation with numbers. Fig. 7 (operator-channel binding example) carries the dataflow idea.
- Tables: Table 2 (spec of commodity NMP products with a computation-to-bandwidth ratio column), Table 3 (comparison of dataflow designs on two columns, "Mapping Decision" and "Operator Fission", with H2-LLM as the last row), Tables 5-7 (design-space parameters, FPU limits). The comparison table puts the paper's own row at the bottom with the distinguishing words "Data-centric, Prefill-aware, Flexible".

### 10. Why it reads as strong, and what does not transfer
Three moves worth copying:
1. Motivation by one measured counter-example per claim (Section 3.1, Fig. 3 and 4b): the "in-die NMP stops helping at batch 8" roofline and the "controller eats 40% of logic area" number make the two problems quantitative before the design appears.
2. Each design section ends with the list of knobs it exposes (Sections 4.4 and 5.4), so the DSE section is a natural consequence; the three-part design (architecture, dataflow, DSE) reads as one pipeline.
3. Sweeps end with numbered one-sentence Takeaways (Section 7.4), which turn plots into design rules and back up the last contribution bullet.

Particular to this topic, not to copy: hybrid-bonding area and pin arithmetic and the roofline of LPDDR NMP; the long formal MAG/GCMap/OCMap notation.
