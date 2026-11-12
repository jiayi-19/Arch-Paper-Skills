# asplos-2026-lifetime: Lifetime-Aware Design for Item-Level Intelligence at the Extreme Edge

### 0. Identity
- Venue and year: ASPLOS 2026 (Pittsburgh). Award: Best Paper.
- Contribution type: benchmark plus system/framework plus co-design plus a tape-out. Three named artifacts: FlexiBench (benchmark suite), FlexiBits (processor family), FlexiFlow (lifetime-aware carbon design framework). It is the closest of the four papers to our "benchmark plus orchestration framework" paper.
- Pages: 24 total: 12 pages body (Sections 1 to 7), about 5 pages references, about 6 pages appendices (workload descriptions, memory profiling method, extended PPA and carbon results, tape-out details).
- Full text used: https://arxiv.org/pdf/2509.08193 (arXiv v2). Text extracted by cropping each page into two columns. Word counts are approximate (captions and table text are mixed in).

### 1. Skeleton
| Section | Role | Approx words | Figures / tables |
|---|---|---|---|
| Abstract | abstract | about 200 | 0 |
| 1 Introduction | setting, insight, framework, numbered contributions | about 860 | 1 fig (Fig. 1) |
| 2 Background, Motivation & Related Work (2.1 Flexible Electronics for ILI, 2.2 Sustainability Challenges, 2.3 Related Work) | background, motivation, related work in one section | about 780 | 1 table (Table 1, prior art vs. FlexiFlow) |
| 3 FlexiBench (3.1 The Benchmark Suite, 3.2 Workload Characterization: ISA, computational patterns, memory) | design/artifact 1 plus characterization | about 1,000 | 1 fig, 2 tables |
| 4 FlexiBits (4.1 Design Rationale, 4.2 Baseline Bit-Serial Processor Architecture, 4.3 Flexible Bitwidth Architectures, 4.4 Performance, Power, and Area Comparison) | design/artifact 2 plus evaluation of cores | about 1,200 | 1 fig (template microarchitecture), 1 table |
| 5 FlexiFlow (5.1 Modeling Scope and Assumptions, 5.2 Framework Inputs, 5.3 Profiling Data, 5.4 Sustainability Metrics, 5.5 Lifetime-Aware Design Model) | design/artifact 3 (the framework) | about 1,230 | 1 fig (Fig. 4, framework with worked example) |
| 6 Evaluation (6.1 setup, 6.2 lifetime-aware architecture selection, 6.3 algorithm selection, 6.4 at-scale sustainability, 6.5 open-source tape-out) | evaluation | about 1,300 | 3 figs (Fig. 5 selection map, Fig. 6 Pareto, Fig. 7 tape-out), 1 table |
| 7 Conclusion | conclusion | about 150 | 0 |
| Appendices A and B | workload details, methodology, extended results | about 2,000 | 7 more figs, 3 more tables |

Totals: 7 figures and 5 tables in the body (14 figures and 8 tables including the appendix). Related Work is merged into Section 2 and made the gap analysis (Table 1). There is no separate overview section and no separate methodology section: the method is spread through the three artifact sections, and the evaluation setup is the short 6.1.

### 2. Abstract
- 8 sentences, about 200 words, one paragraph, with an inline numbered list of the three components.
- Functions in order: (1) approach and name: "We present FlexiFlow, a lifetime-aware design framework for item-level intelligence" with a definition of the domain (disposable products); (2) technology and its limits: flexible electronics are cheap but kHz-speed and thousands of gates; (3) insight: lifetimes vary 1000x, which changes optimal architecture at trillion-item scale; (4) approach and mechanism: model embodied versus operational carbon by application lifetime, with the three components listed (1) FlexiBench, (2) FlexiBits (with a number 2.65x to 3.50x energy per workload), (3) the carbon-aware model; (5) results: 1.62x from microarchitecture, 14.5x from algorithms; (6) validation: the first tape-out with an open-source flow, 30.9 kHz; (7) scope/vision statement; (8) code link.
- Numbers: five (1000x, 2.65x to 3.50x, 1.62x, 14.5x, 30.9 kHz). Scope is stated only by the kind of decision ("lifetime-aware microarchitectural design can reduce carbon footprint by 1.62x, while algorithmic decisions can reduce it by 14.5x"); the specific workload behind each number is not in the abstract (Cardiotocography for 1.62x, food spoilage KNN versus LR for 14.5x).
- The system is named in the first sentence. The insight appears before the components, as "Our insight is ..." in sentence 3. No explicit prior-work or gap sentence; the problem is carried by "limited to kHz speeds and several thousands of gates".

### 3. Introduction
- 6 paragraphs plus 4 numbered contribution paragraphs, about 860 words, written in short, plain sentences (about 24 words each in the sample).
- P1 (setting): opens "Embedding intelligence into everyday items is the next frontier of ubiquitous computing"; gives three examples (food packaging, patches, textiles) and names item-level intelligence (ILI) and the Extreme Edge. Ends with "where traditional design considerations shift", which sets up P2.
- P2 (problem as contrast): "The characteristics of ILI are markedly different from conventional computing domains." Uses Fig. 1: trillions of units versus millions, microwatts versus watts, lifetimes of days to years, and the sustainability risk (Jevons' paradox). Ends "demanding we reevaluate design principles for ILI".
- P3 (use cases): UN Sustainable Development Goals with three concrete examples (food waste, medical patches, textiles).
- P4 (key insight, at about 40 percent of the intro): "Our key insight is that ILI applications exhibit extreme heterogeneity in operational characteristics, particularly deployment lifetime." One example (days versus years, a 1000x variation) and the claim "lifetime a first-class design parameter".
- P5 (approach and technology): "To this end, we present a lifetime-aware design framework that provides the first comprehensive methodology ..." Explains flexible electronics and states its limits ("kHz frequencies rather than GHz, thousands of transistors rather than billions").
- P6 (framework summary): says the framework models embodied versus operational carbon and has "three key components that each address gaps in the ILI design stack", then four numbered, bold-named paragraphs.
- The four numbered items: 1 FlexiBench (component, with numbers: 11 workloads, 0.3 KB to 240 KB, days to years); 2 FlexiBits (component: 1-, 4-, 8-bit bit-serial RISC-V cores; justified by "conventional 32-bit datapaths are prohibitively expensive"); 3 FlexiFlow (framework; number 1.62x versus one-size-fits-all); 4 "Our analysis shows the impact of lifetime-aware design" (findings: 14.5x, plus the open-source tape-out at 30.9 kHz). Three are named artifacts, one is findings plus validation.
- The last sentence of the intro states the achievement in one sentence ("we advance the primary components of the ILI design stack, proving flexible electronics as an accessible and sustainable technology"). There is no roadmap paragraph.
- Prior work: not discussed in the intro at all; it is deferred to Section 2.3 and Table 1.
- Challenges device: none. The structure is "gaps in the stack" (benchmark, processor, methodology), which maps to the three components. The problem is posed as a mismatch of scale, power and lifetime, not as a list of technical challenges.
- Results preview: embedded in the numbered contribution paragraphs (1.62x, 14.5x, 30.9 kHz), with the number attached to the thing that produced it.

### 4. Motivation and background
- A merged section: "Background, Motivation & Related Work". 2.1 explains flexible electronics (cost, no packaging, but tens of thousands of transistors, kHz clocks, KB memory) with Fig. 1b as the data. 2.2 develops the carbon argument: embodied versus operational carbon, then "FlexICs' extremely low manufacturing emissions make it less clear which component will dominate", which ends with the claim that lifetime must become a first-class design parameter. 2.3 states gaps by three bold run-in headings (Benchmarks, Processor Architectures, Design Methodologies) and Table 1.
- Evidence is analytical and cited, not measured in this section. Observations end with explicit statements ("Lifetime must become a first-class design parameter for architectural decisions"). The section closes by one-to-one mapping: "Our work addresses gaps in all three infrastructure components: FlexiBench ..., FlexiBits ..., and FlexiFlow ...".

### 5. Overview of the design
- No overview section. The introduction's numbered list (P6) is the overview, and Fig. 4 at the start of Section 5 is the framework picture: inputs (user specifications, architecture designs, foundry data), simulation and physical design, then the lifetime-aware model, with a food-spoilage example drawn inside the figure.
- The section chain is the overview: Section 3 ends by saying the lifetime heterogeneity "motivates our lifetime-aware design methodology"; Section 4 opens "These findings motivate FlexiBits"; Section 5 opens "The findings from FlexiBench and FlexiBits raise a key question: How should optimal design selection be guided ...". The key insight is carried by repeated phrases (first-class design parameter, one-size-fits-all, 1000x).

### 6. Design sections
- Pattern per artifact: what it is and why it is needed (tied to the previous section's finding), the design (template, inputs, equations), then a characterization (instruction mix, memory, PPA). FlexiFlow section: modeling scope and assumptions first (System Boundary, Device Power, with sentences like "We exclude components that remain constant"), then inputs, then the two carbon equations, then the lifetime-aware model with the worked example in Fig. 4.
- Running example: food spoilage detection runs through the intro, Fig. 4, Section 6.2, 6.3, and 6.4. Cardiotocography is the second example (one-week versus nine-month deployment).
- Naming: the Flexi- prefix (FlexiBench, FlexiBits, FlexiFlow) and processor names SERV, QERV, HERV (1-, 4-, 8-bit) stay constant throughout. Bold run-in labels start each sub-point: "System Boundary.", "User Specifications.", "Operational Carbon Footprint."
- Flow: output of each artifact is the input of the next (workload characteristics feed core design; core PPA and workload profile feed the carbon model).
- Left out: workload descriptions, memory profiling method, extended PPA, power breakdown, tape-out details all go to the appendices; the body points to them ("Deeper explanations of each workload are in Appendix A.1"). The embodied-carbon method is a short paragraph on the LCA standard and tool.
- Figure types: environment comparison chart, instruction-mix stacked bars, microarchitecture template with fixed versus width-varying blocks in two colors, framework flow, selection heat map, Pareto frontier, tape-out photos.

### 7. Evaluation
- Organized by guiding questions, not formal research questions: "How do we navigate architectural trade-offs for sustainable ILI?" (6.2), "Beyond hardware, what algorithmic trade-offs should be considered ...?" (6.3), "What sustainability benefits can potentially be realized ...?" (6.4), then validation (6.5). Within 6.2, bold run-in headings carry findings ("FlexiFlow Reveals Trade-offs Depend on Lifetime", "What Drives These Trade-offs?", "Model Sensitivities").
- Claims are bounded by naming the workload and condition: "Choosing SERV for this real-world scenario would increase carbon footprint by 1.62x"; US grid carbon intensity of 367 g CO2e/kWh stated in setup; Fig. 5 omits one workload for an explained reason.
- First result: the selection map across lifetime and execution frequency, with the finding "no single architecture is universally optimal", then a one-line example.
- Ablation: not a classic ablation; sensitivity to energy source and software choice is stated and sent to the appendix. The algorithm study is a Pareto frontier of accuracy versus carbon, with the comment that a bad algorithm outweighs a bad core.
- Negative or weak results: handled in plain words. Three of 11 workloads are orders of magnitude away from all cores today (Section 4.4); an ineffective silicon system could add about 6.9 million cars of emissions in the at-scale study; the study sweeps effectiveness rates and uses "conservative estimates" where life-cycle data is missing; memory subsystem design is left to future work.

### 8. Sentence and paragraph habits
- Average sentence length about 22 to 24 words; the body sentences are shorter than in h2llm and counterpoint. Paragraphs 60 to 140 words.
- Person and tense: "we" about 60 and "our" about 40 in the body; present tense for the framework ("FlexiFlow models ..."), past tense for tape-out and measurement.
- Topic sentences: often a claim sentence followed by a concrete example in the same paragraph; bold run-in headings with a period begin most sub-paragraphs.
- Emphasis: bold run-in headings, bold component names in the numbered contribution paragraphs, italics for key phrases.
- Lists: four numbered contribution paragraphs; inline "(1) ... (2) ... (3)" in the abstract; "First, ... Second, ..." in the FlexiBench section.
- Parentheticals: many (about 90 in the body), mostly "(e.g., ...)" and acronyms. Semicolons: about 3. Em dashes: about 3 in the body, so very low. En dashes only in ranges.
- Hedging: low; "likely" and "may" a few times, "potentially" in the at-scale section. Strong "first" claims are numerous ("the first comprehensive methodology", "the first benchmark suite", "the first successful tape-out ... with a non-silicon PDK").
- Numbers: with their reference point right next to them (1.62x "over one-size-fits-all designs", "QERV and HERV require 1.26x and 1.54x more area").
- Eight sentence patterns:
  1. "Embedding [X] into [Y] is the next frontier of [field]."
  2. "Our key insight is that [domain] applications exhibit [heterogeneity] in [parameter]. This makes [parameter] a first-class design parameter."
  3. "To this end, we present [Name], which provides the first [comprehensive thing] for [domain]."
  4. "[Name] provides the first benchmark suite of workloads specifically designed for [domain]. Unlike traditional benchmarks that focus on [A], [Name] comprises [N] workloads targeting [B]."
  5. "[Previous findings] motivate [Next component]." (section hand-off)
  6. "The findings from [A] and [B] raise a key question: How should [decision] be guided through [trade-off]?"
  7. "For all workloads, no single [choice] is universally optimal. Instead, distinct boundaries emerge where ..."
  8. "This case study shows us that [domain] requires co-design across the stack."

### 9. Figures and tables
- Fig. 1 compares ILI with mobile/edge and cloud on two axes (embeddedness and mobility) and on a table of volume, power, lifetime, cost. It comes first because the whole paper rests on the claim that ILI is a different regime of scale, power and lifetime. Captions are short and descriptive ("Item-level Intelligence (ILI) in comparison with traditional mobile/edge computing and cloud computing."); the interpretation is in the body text.
- Carrier figures: Fig. 4 (framework with a worked example of food-spoilage that shows the optimal core changing with shelf life) and Fig. 5 (a grid of carbon-optimal core per workload over lifetime and execution frequency, with real-world use cases marked as stars). Fig. 3 uses two colors to show which blocks are fixed and which scale with datapath width.
- Tables: Table 1 is a check-mark comparison of prior art against FlexiFlow along the three gaps (benchmarks, processors, methodology) and sustainability, with the paper's own column last; Table 2 lists all 11 workloads grouped by lifetime (days-weeks, months, years) with the SDG each addresses and the lifetime with a citation; Table 4 positions the three cores among prior flexible processors.

### 10. Why it reads as strong, and what does not transfer
Three moves to copy:
1. A single quantity does all the argumentative work: lifetime is named in the title, abstract (1000x), intro P4 ("first-class design parameter"), Table 2 grouping, Fig. 4 example, Fig. 5 axis and the evaluation question. A reader can say the paper's thesis in a phrase (Introduction P4, Section 2.2).
2. Three gaps map to three named components, and each section opens by citing the finding of the previous section that motivates it ("These findings motivate FlexiBits"; "The findings from FlexiBench and FlexiBits raise a key question") (Sections 2.3, 4, 5).
3. The contribution list is four short numbered paragraphs, each bold-named with its own number and its own "unlike prior X" contrast (Introduction P6).

Particular to this topic, not to copy: the sustainability rhetoric (Jevons' paradox, trillion units, UN goals, cars-equivalent savings) and the very large "first" claim count; the appendix-heavy structure (a third of the pages) fits a tape-out paper.
