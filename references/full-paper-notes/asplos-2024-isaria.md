# asplos-2024-isaria: Automatic Generation of Vectorizing Compilers for Customizable Digital Signal Processors

Reading notes. Text extracted with pdftotext; word counts are approximate.

## 0. Identity
- Title: Automatic Generation of Vectorizing Compilers for Customizable Digital Signal Processors
- Venue and year: ASPLOS 2024 (Volume 1, La Jolla). Award: ASPLOS 2024 Best Paper.
- Contribution type: automation (a framework that generates compilers) with a new technique (phase-oriented rule application). It is a compiler paper whose target is ISA customization, so it shares the 'automate the design loop' theme.
- Pages: 16 including references. About 8,000 words in the body.
- Full text used: https://sgt-pl.com/papers/compgen.pdf (the author's site; the cs.utexas.edu link redirected to this host through a broken address, and the slides are on the same site). DOI 10.1145/3617232.3624873.

## 1. Skeleton
| Sec | Heading | Role | Words | Figs / tables |
|---|---|---|---|---|
| Abstract | | | 185 | 0 |
| 1 | Introduction | | 1,130 | 0 |
| 2 | Rewriting for Vectorization (2.1 Vectorization via Equality Saturation, 2.2 Synthesizing Rewrite Rules, 2.3 E-graph Explosion) | background plus problem exposition | 1,730 | Fig 1 (DSL grammar) |
| 3 | Phase-Oriented Rule Synthesis (3.1 Rewrite Rule Generation, 3.2 Discovering Rule Phases, 3.3 Scheduling Rule Phases at Compile Time) | overview and design | 2,575 | Fig 2 (workflow), Fig 3 (compile algorithm) |
| 4 | Implementation | methodology | 200 | Table 1 (lines of code) |
| 5 | Evaluation (5.1 to 5.5, each titled by a research question) | evaluation | 2,360 | Figs 4 to 9, Table 2 |
| 6 | Related Work | related work | 680 | 0 |
| 7 | Conclusion (7.1 Future Work) | conclusion and discussion | 410 | 0 |
No separate Motivation section; Section 2 does that job. Totals: 9 figures, 2 tables.

## 2. Abstract
- 8 sentences, about 185 words, in two paragraphs.
- Functions: (1) setting: DSPs and vectorized execution; (2) practice: engineers rely on auto-vectorizing compilers; (3) problem: building them is a large, error-prone investment repeated for each new ISA; (4) 'We present Isaria, a framework ...' (approach); (5) mechanism: equality saturation over rewrite rules; (6) insight and mechanism in one long sentence: rather than hand-crafting rules, synthesize them from an ISA spec, discover phase structure, and schedule with pruning; (7) result: kernels beat DSP libraries by up to 6.9x and are competitive with expert-built compilers; (8) scope: also speeds up exploration of ISA customizations.
- Numbers: one (6.9x), scoped as 'up to' and as versus existing DSP libraries, on an industrial DSP architecture.
- System named in sentence 4. The word "Rather than" appears twice, in sentences 2 and 6, setting up the contrast between manual and automatic.

## 3. Introduction
- 7 paragraphs plus a 3-bullet contribution list, about 1,130 words (paragraphs about 150 words).
- P1: setting (low-power embedded apps, DSPs, long tail of custom kernels that libraries do not cover). Ends by naming the compilation challenge, 'amplified' by many ISAs and customizations.
- P2: 'To address this problem, recent work ...' lists program synthesis, pattern matching, autotuning; then focuses on equality saturation as pioneered by Diospyros, explains it in four sentences, and ends with its strong result (3.1x faster than libraries).
- P3: "While these results are encouraging, the equality saturation approach places several burdens ..." then First (rule writing is a delicate balancing act, error means hours-long timeouts), Second (soundness bugs), Finally (ISA-specific, slows exploration). Ends with an 'In short' sentence: DSP applications need not one good compiler but a productive way to design and evolve compilers. This is the problem statement in one sentence.
- P4: 'This paper introduces the Isaria framework'. High-level: generate rules offline, schedule at compile time; 'radically different approach'. States inputs (ISA interpreter in Rosette and an abstract cost model).
- P5: "Isaria's key insight is that rewrite rules for vectorization fall into natural phases" with three kinds (expand, simplify, vectorize). It then says the insight seems to contradict the usual motivation for equality saturation (phase ordering) and resolves that.
- P6: "The Isaria workflow comprises three parts" and walks generate, analyze and phase, apply. Includes the key design nuance (cost-increasing rules are useful) and the pruning trade-off ('sacrifices completeness').
- P7: 'We evaluate Isaria ...' results preview: up to 6.9x over Tensilica SDK libraries, up to 25x over the Clang auto-vectorizer, 34% faster than Diospyros on average (with a caveat), compile 2.1x slower, plus two custom instructions explored.
- P8 (list): "In summary, this paper makes the following contributions:" three bullets.
- Problem posing: a long-tail kernel gap, then the cost of building a compiler per ISA. It is framed as developer productivity, not only speed.
- Key insight: stated in its own paragraph (P5) with the label 'key insight'.
- Prior work: credited generously (Diospyros 'pioneered', excellent performance), then given three numbered burdens. Dismissal is by what the credited approach forces on the human.
- Challenges device: three burdens in P3 with First, Second, Finally.
- Contributions: 3 bullets: (1) the approach (a framework); (2) a technique (phase-oriented selection and application); (3) an evaluation result (outperform commercial tools, match state of the art in manually crafted ones, no numbers in the bullet).
- Results paragraph: P7 has numbers and bounds; it includes an unfavorable number (2.1x slower compile) and a caveat on the 34% average.

## 4. Motivation and background
- No separate Motivation section. Section 2 'Rewriting for Vectorization' gives background (2.1), the burden of hand-crafting (2.2), and a failed attempt using an off-the-shelf rule synthesizer (2.3).
- Evidence: a running example (a 4-wide vector addition with one lane lacking a partner; three rewrite rules that undo vectorization). It is concrete, small and can be read line by line. One measured motivation number in 2.3: Ruler produced 300 rules and equality saturation exhausted 64 GiB on a small 2x2 convolution, while Isaria finds a solution in 3 seconds using 0.2 GiB.
- The section ends in an explicit takeaway sentence introduced as "The key insight from this example": to make synthesized rules scale, avoid the E-graph explosion by controlling which rules are applied and when. It then says the paper automates what Diospyros did by hand.
- Tie to design: Section 2.3 names two problems (rules go backwards; rules are redundant) and Section 3 solves them with phases and pruning; the text points back ('two problems in Section 2.3').

## 5. Overview of the design
- Section 3 opens with a short overview paragraph (inputs: ISA interpreter and abstract cost model; three parts; the idea of subsetting rules into coarse phases). Figure 2 shows the offline stage (candidate rule generation, phase selection into expansion, compilation and optimization rules) and the compile-time stage, with shaded boxes for inputs and outputs. Subsection numbers appear in the figure boxes (for example '§3.2').
- The text does not walk the figure box by box; it names the three parts and each part gets a subsection (3.1, 3.2, 3.3). The key insight (phases) is the section's title word: Phase-Oriented Rule Synthesis.
- Forward reference to scalability appears as 'a scalability challenge we address in Section 3.2'.

## 6. Design sections
- Pattern: the need (a short motivating paragraph), then the mechanism with definitions (Definitions 1 to 4 for cost function, monotonicity, cost differential, aggregate cost), then a worked rule example (the VecAdd rule has higher cost on the left than the right), then an alternative that was rejected (a purely syntactic strawman) with the two reasons it fails, then cost and risk (vector lane generalization risks unsound rules, which are checked).
- Running example reused between Section 2 and Section 3 (the same three rules are assigned to different phases so they cannot undo each other).
- Components stay stable: expansion, compilation, optimization (rules); EqSat, Extract, Compile (algorithm). A sentence says the phase names carry no semantic meaning but are labels for typical rules.
- Flow: ISA spec and cost model go into candidate rules, then rules into phases, then phases into scheduled equality saturation with pruning between iterations.
- Algorithm shown as code (Figure 3, 14 lines). The explanation names two elements ('phase scheduling' and 'pruning') in bold run-in headings. It states the cost honestly: pruning is greedy and sacrifices completeness.
- Implementation (Section 4) is short: reuse of Diospyros front end and back end, lines of code per component.

## 7. Evaluation
- Organized by five research questions, each of which is a section heading in question form: comparison with existing compilers and hand-written kernels (5.1), whether phasing and pruning make compilation tractable (5.2), how offline rule-generation time affects quality (5.3), how Isaria helps explore ISA customizations (5.4), and sensitivity to the phase assignment (5.5). The five questions are listed at the start of Section 5 with section pointers.
- First result: Figure 4, speed-up over unvectorized code for Clang auto-vectorization, hand-written Nature kernels, Diospyros and Isaria.
- Bounding: baselines named with versions, benchmark sizes listed, a measurement by cycle-level simulator, timeouts stated (one day offline, 180 s per saturation call).
- Ablations: remove phases (even the smallest benchmark runs out of memory and no solution uses vector instructions); remove pruning (most large cases run out of memory; small cases get slightly better kernels); rule-generation timeout sweep; alpha/beta sweep (Figure 9 heat map).
- Negative or weak results: compile time is 2.1x slower than Diospyros; '34% faster on average' is called skewed; larger kernels fall behind the hand-written Nature kernels because they unroll loops (77K lines of C); more rule-generation time does not always help; the custom instruction study yields only 1.7%, 0.5%, 2%. Each is stated and then explained or tied to a future-work item. The compile time slowdown is justified with a productivity argument in the figure caption.

## 8. Sentence and paragraph habits
- Average sentence length about 24 words overall; the introduction and background run longer (31 to 34 words); related work about 19.
- Paragraphs 100 to 200 words. Person: 'we' for the authors' own steps and the reader ('To see how this approach works, consider ...'), 'Isaria' as subject in design ('Isaria assigns ...', 'Isaria extends Ruler'). Present tense for the design; past for experiments.
- Bold run-in headings in design and results ('Three rule phases.', 'Cost-based phase assignment.', 'Phase scheduling.', 'Pruning.', 'Compile times.', 'Scalability to larger kernels.', 'Rule phases.').
- Semicolons few (about 14 in the text); em dashes about 10; numbered and bulleted lists for rules, phases, RQs, contributions.
- Hedging: 'in principle', 'empirically we have observed', 'we expect'.
- Numbers: 'up to' with the baseline named, plus mean and median together ('mean of 3.5x and median of 4.8x') and range ('1.0 to 6.9x').
- Sentence patterns:
  1. "While these results are encouraging, ___ places several burdens on ___. First, ___. Second, ___. Finally, ___."
  2. "In short, ___ require not just ___, but a productive approach to ___."
  3. "___'s key insight is that ___ fall into natural phases: some ___, others ___, and still others ___."
  4. "On the surface, this insight contradicts ___. But unlike ___, ___ discovers ___ automatically."
  5. "The key insight from this example is that to make ___ scale, we must avoid ___ by carefully controlling ___."
  6. "An alternative strawman approach would be ___. While this approach is simple, it fails in practice for two reasons."
  7. "We evaluate ___ by addressing five research questions: 1. How does ___? (Section ___)"
  8. "Overall, while ___ are worse than ___, we believe the productivity gain from ___ is worth the trade-off."

## 9. Figures and tables
- First figure (Figure 1) is the DSL grammar, a small reference exhibit rather than a result. The first conceptual figure is Figure 2 (workflow), placed at the start of the design section. The paper has no teaser figure on page 1.
- Caption style: descriptive plus a short takeaway ("Striped bars indicate ... Isaria-based compilers are slower, but the process ... is far more automated"; "Pruning gives up completeness on smaller kernels ..., but enables compiling much larger kernels").
- Carrying figures: Figure 4 (per-kernel speedup across four tools, y-axis log), Figure 8 (scatter of the 294 rules by cost differential and aggregate cost, colored by phase, showing clear clusters), Figure 9 (heat map of alpha and beta).
- Tables: Table 1 (lines of code by component, 2,095 in total, which supports 'the framework is small'), Table 2 (4-way grid for two custom instructions).

## 10. Why it reads as strong, and what does not transfer
Three moves to copy:
1. A tiny failed baseline with numbers (Section 2.3): 'we applied the off-the-shelf synthesizer, got 300 rules, ran out of 64 GiB, whereas Isaria finishes in 3 seconds using 0.2 GiB'. It justifies the whole design before any design is shown.
2. Research questions as section headings (Section 5) and a stated list up front, so each answer is easy to find and each claim carries its own baseline.
3. The key-insight paragraph in the introduction (P5) that raises the objection to its own insight (phases seem to contradict the phase-ordering motivation of equality saturation) and answers it in the same paragraph.

Not to copy: the heavy rewrite-rule notation in Sections 2 and 3, and the 'up to 25x over Clang' style bound, which the authors partly undercut by noting the Clang auto-vectorizer improved since earlier work. The absence of an abstract-level insight sentence is typical of PL-style abstracts.
