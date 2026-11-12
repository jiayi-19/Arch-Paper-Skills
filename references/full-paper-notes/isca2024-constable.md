# isca2024-constable: Constable: Improving Performance and Power Efficiency by Safely Eliminating Load Instruction Execution

### 0. Identity
- Venue and year: ISCA 2024 (text used is the arXiv v1 of 26 Jun 2024, which carries the extended appendix).
- Award: Best Paper.
- Contribution type: mechanism (a purely microarchitectural technique), with a characterization and an open-source tool as secondary pieces.
- Pages: 17 including references and a 3-page appendix (about 18.3k words of raw text; references are about 4 pages).
- Full text: https://arxiv.org/pdf/2406.18786

### 1. Skeleton
Arabic-numbered sections, subsection numbering to three levels. Word counts are approximate (the two-column extraction interleaves a few boundaries).

| Section | ~Words | Role | Figs/Tables |
|---|---|---|---|
| Abstract | 290 (11 sentences) | abstract | 0 |
| 1 Introduction | 820 | intro | 0 |
| 2 Background | 340 | background, ends in a "we conclude" gap statement | Fig 1 |
| 3 Motivation and Goal (3.1 Our Goal) | 400 | motivation by a hand-built timeline example | Fig 2 |
| 4 Performance Headroom of Constable (4.1 global-stable loads, 4.1.1 characterization, 4.2 why they exist, 4.3 resource dependence, 4.4 headroom) | 1500 | measured motivation plus oracle limit study | Figs 3 to 7 (5 figure numbers; Fig 4 not found in captions) |
| 5 Constable: Key Insight | 340 | the insight stated alone, two conditions | 0 |
| 6 Microarchitecture Design (6.1 overview, 6.2 identify, 6.3 eliminate, 6.4 update, 6.5 disambiguation, 6.6 multi-core coherence, 6.7 other decisions, 6.8 illustrative example, 6.9 storage) | 3500 | design | Figs 8, 9, 10, Table 1 |
| 7 Differences from Related Prior Works | 750 | related work 1, four categories, before evaluation | 0 |
| 8 Methodology (performance, power, workloads, evaluated mechanisms, functional verification) | 1000 | methodology | Tables 2, 3, 4 |
| 9 Evaluation (9.1 performance, 9.2 vs prior works, 9.3 coverage, 9.4 pipeline resources, 9.5 power) | 2400 | evaluation | Figs 11 to 19 |
| 10 Other Related Works | 600 | related work 2 (broad areas) | 0 |
| 11 Conclusion | 180 | conclusion | 0 |
| Appendix A (sensitivity, disambiguation, lost opportunities), B (more architectural registers) | 1300 | extended evaluation | Figs 20 to 24 |
Totals: 24 figures, 4 tables. Related work is split in two (Section 7 before the evaluation, Section 10 after it).

### 2. Abstract
- 11 sentences, about 290 words, three short paragraphs (problem and gap; goal and mechanism; results).
- Functions in order: (1) setting and problem (loads limit ILP through data and resource dependences); (2) prior work (LVP, MRN reduce data dependence by value prediction); (3) gap (they still execute the load, so resource dependence stays); (4) goal (mitigate both dependences); (5) approach, named here ("a purely-microarchitectural technique called Constable"); (6) what it does, identify loads that fetched the same data from the same address; (7) coinage of the term "likely-stable"; (8) mechanism (track source registers and memory location, eliminate later instances until a write, store or snoop); (9) result 1: +5.1% performance and -3.4% dynamic power; (10) result 2: SMT gives +8.8%; (11) result 3: combined with the prior predictor EVES it adds 3.7% and 7.8%.
- Numbers: 5.1, 3.4, 8.8, 3.7, 7.8, plus "90 workloads". Scope is stated for each: "on average", "over a strong baseline system that implements MRN and other dynamic instruction optimizations", "in presence of 2-way SMT", "over the load value predictor alone, in the baseline system without and with 2-way SMT, respectively".
- The name appears in the title and in sentence 5.

### 3. Introduction
- About 820 words, 7 prose paragraphs, then a 7-bullet contribution list. Four paragraphs open with a bold run-in label.
- P1 setting: ILP is limited by data and resource dependences; loads cause both (compute address, then fetch data). Ends on the resource-dependence consequence.
- P2 prior work, credited: LVP and MRN are widely studied, they speculate on the value. Ends by saying they improve ILP, which sets up the limitation.
- P3 (bold "Key limitation."): the predicted load is still executed to verify, so resource dependence remains; points to a later section with the headroom number.
- P4 goal and approach: "Our goal in this work is to improve ILP by mitigating both load data dependence and resource dependence" (Introduction); introduces Constable as lightweight and purely microarchitectural.
- P5 key insight, as two numbered conditions (no source register written, no store or snoop to the address); each condition is tied to one eliminated operation (address computation, data fetch).
- P6 (bold "Key mechanism."): two steps, identify likely-stable loads, then track and eliminate.
- P7 (bold "Key results."): five results, "First ... Second ... Fifth" each with a number and a scope (90 workloads, 6-wide baseline already with memory renaming and other optimizations).
- Contributions (7 bullets): (1) finding with number (34.2% of loads global-stable, compilers miss them); (2) finding with number (headroom 9.1% vs 4.3%); (3) mechanism (the confidence-based idea); (4) component (practical microarchitecture under out-of-order and multi-core); (5) verification claim (3400 traces matched against a functional model); (6) result with numbers (5.1%, 3.4%, 12.4 KB); (7) tool, open-sourced. Every bullet ends with a section pointer in parentheses.
- Problem posing: two dependences, one diagram later. The insight appears at P4 to P5, about halfway through the Introduction. Prior work is credited and then given a single "key limitation". There is no "challenges" list; challenges (coherence, out-of-order loads) appear inside the design sections instead.

### 4. Motivation and background
- Background (Section 2, 340 words) is short and ends with an explicit conclusion sentence that names the gap. Section 3 (Motivation and Goal) walks Fig 2, a three-panel pipeline timeline of a tiny code example without LVP, with LVP, and with LVP plus load elimination (4 cycles saved, then 2 more).
- Section 4 is measured: a binary-instrumentation study (their Load Inspector tool) shows global-stable loads, why compilers miss them (two disassembled code examples), how often they sit in a load port when a non-stable load waits (23.0% of load-utilized cycles), and an oracle limit study (4.4).
- Each observation ends with a takeaway sentence beginning "We conclude that" or "The key takeaway is that", sometimes in a count ("We conclude with three key takeaways"). No boxes.
- Mapping to design: forward references by section number; the third takeaway of 4.1.1 (capture both short and long reuse distance) leads to the PC-indexed table design; the two conditions of Section 5 map one to one to two monitor tables in Section 6.

### 5. Overview of the design
- Section 5 is a stand-alone insight section; 6.1 Design Overview is the structure overview (about 350 words) with Fig 8, a pipeline diagram with the three new structures (a) and numbered circles for key operations (b).
- Walk: three structures introduced with bold run-in names (Stable Load Detector, Register Monitor Table, Address Monitor Table), each given three sentences, and the last sentence of the RMT and AMT paragraphs says it "enforces Condition 1" (or 2). Section 6.3 then walks the circled steps 1 to 3.
- Forward references: "(see §6.4.1)", "(see §8.5)".
- The key insight is handled by being given its own numbered-section title before the design starts.

### 6. Design sections
- Pattern in 6.2 to 6.6: what the step does, a sequence of numbered steps tied to circles in Fig 8, then a "challenge" followed by a proposal ("poses two key drawbacks ... To address these drawbacks, we propose to pin the CV-bit"). Costs and negative effects are quantified inline (for example 0.4% lower performance with cacheline-granularity tracking; 0.2% xPRF stalls).
- Section 6.7 "Other Design Decisions" gathers read ports, wrong-path handling and address remapping, each justified by a measured statistic (1.93 loads per rename group, 0.28 SLD updates per cycle).
- 6.8 is a worked example (Fig 10, steps A to G) that includes a deliberate failure: a younger load is incorrectly eliminated and caught by existing disambiguation logic. It teaches the safety argument.
- Component names stay constant (SLD, RMT, AMT, xPRF, can_eliminate flag, "likely-stable" vs "global-stable").
- Details moved to the appendix: sensitivity to width and depth, disambiguation cost, more architectural registers.
- Figures: pipeline diagram, timeline, box-and-whiskers measurement plots, a table of storage.

### 7. Evaluation
- Organized by topic (performance, prior works, coverage, resources, power), not by research question. First result: geomean speedup of EVES, Constable and the combination per workload category, noSMT.
- Each subsection says "We make N key observations. First ..." and closes "We conclude that ...". Claims are bounded by baseline (a Golden Cove-like 6-wide core with memory renaming), workload set (90 traces, 58 workloads) and configuration (noSMT or SMT2).
- Ablations: load-type breakdown (PC, stack, register relative), coverage of global-stable loads, and the appendix sensitivity runs.
- Negative results are shown: in 30 of 90 workloads EVES beats Constable by 9.2% on average (marked in red in the per-workload plot); Constable misses 43.6% of global-stable loads and the paper lists three causes with percentages, then says opportunities remain for future work.
- Correctness is a methodology subsection with a hard claim (3400 traces, no mismatches).

### 8. Sentence and paragraph habits
- Body: about 10.4k words, mean sentence length about 26 words (median 22).
- Paragraphs 100 to 220 words. Present tense, "we" about 98 times plus "our" 15. Bold run-in headings in the Introduction and design. Italics are rare.
- Zero em dashes in the body; 6 en dashes (ranges); 5 semicolons; about 270 parentheses (section pointers, citations, examples). Colon about 50.
- "key" is a recurring marker: "key takeaway", "key observation", "key insight", "key limitation", "key results". "We conclude" appears 12 times. Hedging is light ("can", "may" about 45).
- Numbers come with scope and are often given as "average (up to)" pairs: "on average by (up to) 5.1% (31.2%)".
- Patterns:
  1. "X often limits ILP in modern processors due to A and B."
  2. "Prior works propose many techniques to mitigate A. ... However, they fail to mitigate B as ..."
  3. "Key limitation. Even though X provide benefit by A, they still need to ... which leaves ... on the table (see §N)."
  4. "Our goal in this work is to ... To this end, we propose a lightweight, purely-microarchitectural technique called NAME, which ..."
  5. "The key insight behind NAME is that ... when the following two conditions are satisfied."
  6. "We make N key observations from Fig. M. First, ... Second, ... We conclude that ..."
  7. "To address these drawbacks, we propose to ..." (after a stated problem)
  8. "NAME differs from these works in one major way. These prior works ..."

### 9. Figures and tables
- First figure (Fig 1) shows the two component operations of a load and the hardware resources each consumes in a nine-stage pipeline; it defines the two dependence types that the whole paper is built on.
- Captions are descriptive and often include (a)(b)(c) panel keys; takeaways are in the text, not the caption.
- Argument-carrying figures: Fig 2 (timeline with cycle savings), Fig 7 (oracle comparison: Ideal Constable vs Ideal Stable LVP vs doubled load width), Fig 8 (overview), Fig 10 (worked example). Table 1 (storage per structure) and Table 2 (core parameters, with already-implemented baseline optimizations in bold).
- Table design: sizes in the form "512 entries, tag 24b + addr 32b + ..." so the 12.4 KB headline can be checked.

### 10. Why it reads as strong, and what does not transfer
Moves to copy:
1. Abstract and Introduction use the same chain (limitation, goal, mechanism, numbers), and the Introduction labels it with bold run-ins "Key limitation", "Key mechanism", "Key results", so the argument can be skimmed (Introduction, P3 to P7).
2. An oracle headroom study in the motivation (Section 4.4: Ideal Constable 9.1% vs ideal load value prediction 4.3% vs doubled load ports) proves that the unexploited gap is real before any design appears.
3. Every observation block closes with a one-line "We conclude that" sentence and every result block starts with "We make N key observations", so claims are located and countable (Sections 4 and 9).
- Does not transfer: the large body of microarchitecture detail in 6.4 to 6.7 and the pipeline-stage walk.
