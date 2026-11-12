# asplos-2026-counterpoint: CounterPoint: Using Hardware Event Counters to Refute and Refine Microarchitectural Assumptions

### 0. Identity
- Title: CounterPoint: Using Hardware Event Counters to Refute and Refine Microarchitectural Assumptions
- Venue and year: ASPLOS 2026 (31st ASPLOS, Pittsburgh, March 2026). Award: Best Paper.
- Contribution type: tool and methodology (a framework that tests user-written microarchitectural models against hardware counter data), plus a characterization case study (Intel Haswell MMU) whose findings are the evidence. It is a "framework + discoveries" paper, with no accelerator or mechanism of its own.
- Pages: 17 including references (body about 12.5 pages, references about 4 pages). An extended version is on arXiv (2601.01265); I used the ASPLOS-format PDF.
- Full text used: https://cs.stanford.edu/people/trippel/pubs/lindsay_ASPLOS26.pdf (author copy of the ACM paper, DOI 10.1145/3779212.3790145). Text extracted by cropping into two columns. Word counts are approximate because captions and math are mixed in.

### 1. Skeleton
| Section | Role | Approx words | Figures / tables |
|---|---|---|---|
| Abstract | abstract | about 190 | 0 |
| 1 Introduction | setting, promise vs. reality, solution, contributions | about 1,900 | 1 fig with 3 panels (Fig. 1: growth of counters, constraints, noise) |
| 2 CounterPoint: A Bird's-Eye Overview | overview (pros and cons of constraints, geometry, confidence regions, feasibility testing) | about 1,500 | Fig. 2 (pipeline), Fig. 3 (4-panel geometry), Table 1 (example constraints) |
| 3 From Diagrams to Model Cones | design, part 1 (the diagram language and the cone) | about 800 | Figs. 4, 5 |
| 4 Feasibility Testing with Noise | design, part 2 (confidence regions, LP) | about 700 | Fig. 5 continued |
| 5 Guided Model Exploration | design, part 3 (feature discovery, classification, search) | about 1,050 | Figs. 6, 7, 8 |
| 6 Implementing CounterPoint | implementation | about 350 | 0 |
| 7 A Case Study: The Intel Haswell MMU (7.1 guided model exploration, 7.2 performance characterization) | evaluation | about 2,000 | Fig. 9 |
| 8 Related Work | related work, late and short | about 270 | 0 |
| 9 Conclusion & Future Work | conclusion plus explicit limits | about 245 | 0 |

Totals: 9 figures, 1 table. There is no Motivation section (motivation is inside the introduction), no standalone Methodology section (setup is the first part of 7.1), and no appendix; the full linear program and refinement trail are in a cited technical report.

### 2. Abstract
- 7 sentences, about 190 words, one paragraph.
- Functions in order: (1) setting plus promise: counters could reveal bottlenecks and detailed behavior; (2) problem: vague specs, opaque designs, multiplexing noise make data hard to interpret; (3) approach: "We introduce CounterPoint, a framework that tests user-specified models ... for consistency with counter data"; (4) mechanism: it pinpoints plausible features when mismatches occur, using multi-dimensional confidence regions against noise; (5) scope/case study: Haswell MMU; (6) results as a list of discovered features (a load-store-queue-side TLB prefetcher, merging page table walkers, abortable page walks, and a further feature); (7) one-sentence value statement ("helps experts reconcile noisy ... with their mental model").
- Numbers: none at all. The results are named discoveries, not metrics. Scope is "a case study" on one component of one processor. System named in sentence 3, right after the problem, with its formal term (the model notation) introduced in the same sentence.

### 3. Introduction
- About 10 paragraphs and a 6-bullet list, about 1,900 words, with six bold run-in headings. The shape is promise, then reality, then answer.
- P1 (setting, history): opens "Hardware event counters (HECs) are specialized registers ..."; gives the 1980s origin; ends with their original use, which sets up "Since then, their role has expanded".
- P2 (setting, growth): the list of uses; "thousands of HECs, more than a 10x increase since 2009" (Fig. 1a). Ends on growth, which sets up the "promise" paragraph.
- P3 "The promise of a broad set of HECs." (bold run-in): in principle, many counters let experts test their mental model without RTL. Ends with the contrast with traditional broad metrics.
- P4 "Address translation provides a prime example.": a concrete assumption in prior research (the PDE cache is accessed once per walk) written as an inequality; "Surprisingly, our measurements on Intel Haswell show that this expected relationship ... does not always hold." Defines the term model constraint on the spot. Then two numbered benefits ("First ... Second ...") of having many counters. Ends by stating what the full counter set revealed (merged walks, aborted requests).
- P5 "The reality of a broad set of HECs.": "The PDE cache example is an ideal case ... In practice, however, experts are rarely able to ..." Poses the problem as two challenges, "First" (constraints grow super-linearly) and "Second" (counters are multiplexed, so noise grows). Ends with Fig. 1c and the statement that violations become undetectable.
- P6 "Extracting the promise of HECs with CounterPoint.": "To bridge the gap between the promise and reality of HECs, we invent CounterPoint ..."; "centered around three key insights" (First, Second, Third), where insight 1 maps to challenge 1 and insight 3 maps to challenge 2.
- P7 "The CounterPoint approach.": the pipeline in prose (write a model in a DSL, derive the cone, build confidence regions, feasibility test), Fig. 2.
- P8 "Evaluating CounterPoint via a case study.": names the Haswell MMU findings and why Haswell is a good test.
- P9 "Technical contributions. Overall, this work:" followed by 6 bullets.
- P10 "In sum, ..." closes with value statement and the public release.
- Problem posing: a concrete refuted assumption comes before any definition, so the reader sees the payoff first and then the difficulty. The key insight (write the model as a diagram of micro-op paths and let math derive constraints; use correlations for noise) first appears in P6, mapped to the two challenges of P5.
- Prior work: credited only lightly in the intro (uses of counters in P2, "prior ad hoc approaches" in P5). The detailed comparison is in Section 8. Dismissal is by capability: "Compared to traditional methods that treat counter noise independently ..., this approach substantially reduces the impact of noise".
- Challenges device: yes, two challenges with "First ... Second" inside P5, followed by three insights with "First ... Second ... Third" inside P6. No bullets for either.
- Contribution list: 6 bullets, all start with a verb ("Defines", "Introduces", "Defines", "Applies", "Develops", "Reveals"). Item types: concept/finding (model constraints), component (the diagram), component plus theory (model cone, with an equivalence proof), mechanism (confidence regions), capability (feasibility testing), result (discovered features). No numbers in any bullet.
- Results preview: there is no numeric preview anywhere in the intro. The case-study paragraph lists discoveries qualitatively (features by name, with trigger conditions).

### 4. Motivation and background
- No separate section; the motivation is P3-P5 of the introduction, supported by Fig. 1 (three panels: counters per microarchitecture over time, constraints growing with counter count, noise growing with counter count). Evidence is mixed: counted from the Linux perf event database (footnote says how), derived analytically (super-linear constraints), and measured on Haswell (noise vs. number of counters).
- Observations end with plain takeaway sentences ("... it becomes impossible to determine whether ... is violated"), no insight boxes. Section 2 opens with a short "pros and cons of model constraints" subsection that restates why constraints are useful and hard to derive by hand, with Table 1 and Fig. 3 as examples. It works as a second, more technical motivation.
- Tie to design: the two challenges in P5 map one to one to the three insights in P6 and then to the next sections (Section 3 for constraints, Section 4 for noise, Section 5 for exploration).

### 5. Overview of the design
- Yes: Section 2 "A Bird's-Eye Overview", about 1,500 words, with Fig. 2 (the whole pipeline: DSL to micro-path decision diagram, model cone; noisy counter data to confidence regions; feasibility test) and Fig. 3 (4-panel pictorial geometry), plus Table 1.
- The text walks by concern with bold run-in headings: "The pros and cons of model constraints", "The geometry underlying model constraints", "Generating tight confidence regions of HEC observations", "Feasibility testing for guided model exploration". Each ends with a forward pointer ("as described in Section 6").
- The key insight is repeated here in more precise form (groups of events counted together are the natural unit; the cone is the dual of the constraints) and then pushed into the later sections.

### 6. Design sections
- Pattern: define the object (micro-path, counter signature, flow equation), define the derived object (model cone), prove or state the property, then say how it is computed. Section 4 follows need (noise gives false violations), mechanism (confidence regions), approximation (bounding box, with the honest note "We leave alternatives like quadratic programming for future work"), and then the feasibility LP.
- Worked example: Fig. 6 walks one violated constraint (PDE cache misses exceed walks) through the exact diagram change that removes it; Figs. 7 and 8 show a four-model toy lattice and a search graph.
- Naming: the same terms (model constraint, model cone, counter confidence region, micro-path) are used with identical wording throughout, and the footnotes give the geometric definitions (convex, polyhedral, cone).
- Flow between components: diagram to cone (geometry), cone and confidence region to feasibility (LP), violated constraints to feature suggestions (expert in the loop), then back to a revised diagram. The text names this loop explicitly ("This enables iterative exploration").
- Left out: the full linear program and the detailed refinement history go to a technical report; the DSL gets only a short paragraph; implementation is 3K lines of Python and one paragraph.
- Figure types: example diagram with node types, geometric pictures (cones, boxes), a pipeline, a search tree, and scaling plots.

### 7. Evaluation
- Not by research question. One case study, organized as (7.1) guided model exploration with setup, then discovery paragraphs under bold run-in headings (Address translation prefetchers, Page table walk merging, Root-level MMU cache, Aborted page table walks, Page table walk replays), and (7.2) tool performance.
- Claims are bounded in plain words: "we focus specifically on data-side activity in native execution"; "full confirmation ... would require proprietary RTL" while CounterPoint "enables high confidence conclusions". Each discovery says what evidence is used (feasible with a diagram that includes the feature but infeasible without it).
- Ablation: two. Counter confidence regions that use correlations detect over 24% more violations than regions that assume independent counters (up to over 75% for some models); removing two microbenchmarks makes key violations disappear.
- Weak results: stated directly with hedged verbs. For aborted walks, "more detailed study is necessary"; for page-walk replays, "We hypothesize" with an alternative explanation. The conclusion says this is a first proof of concept and lists what is missing (multicore, multi-socket, hyperthreading, kernel activity, accelerators).
- First result shown: the data set size (about 20 million samples), then the statistical gain from correlations, then the discoveries. Runtime comes last: about 213 seconds per model on average, about 200 ms per observation; constraint deduction scales exponentially but is only needed for feedback.

### 8. Sentence and paragraph habits
- Average sentence length: about 25 words in the body, about 30 in the introduction (script estimate on extracted text).
- Paragraph length: medium-long, 90-170 words; in the intro each bold run-in paragraph is one idea.
- Person and tense: "we" about 65 in the body, "our" about 30; present tense for the tool, past tense for what was found ("we uncovered").
- Topic sentences: often a bold run-in heading, followed by a plain claim sentence.
- Emphasis: bold run-in headings, italic for first use of terms; no boxed takeaways.
- Lists: contribution bullet list (6 items, verb first); inline "First/Second/Third" appears in at least three places.
- Parentheticals: moderate (about 120 in the body, mostly examples with "e.g.," and citations).
- Dashes: heavy use of the em dash (about 18 in the introduction alone and about 23 in the sampled body), mostly to set off a definition or an aside. Semicolons about 19 in the body, so a mid level.
- Hedging: "likely", "plausible", "suggests", "we hypothesize" where the evidence is indirect; plain assertion for derived facts ("proves its equivalence").
- Numbers: counts and percentages with the thing counted ("over 25% of counter pairs have a Pearson correlation coefficient that exceeds 0.9").
- Eight sentence patterns:
  1. "The promise of [X]. In principle, [X] should allow experts to [benefit] even without [barrier]."
  2. "The reality of [X]. In practice, however, experts are rarely able to [do it] because [cause]. In particular, they face two challenges."
  3. "Surprisingly, our measurements on [platform] show that this expected relationship does not always hold."
  4. "To bridge the gap between the promise and reality of [X], we invent [Name], a framework that [verb]."
  5. "[Name] is centered around three key insights. First, ... Second, ... Third, ..."
  6. "Using [Name], we uncovered [feature]. Our analysis revealed [N] key aspects: First, ..."
  7. "This overturns the prevailing model in prior work, which assumed [old belief]."
  8. "Intuitively, [one-sentence plain-language reading of the formal object]."

### 9. Figures and tables
- Fig. 1 (three panels) shows counters growing 10x since 2009, the number of model constraints growing super-linearly with counters, and multiplexing noise growing with counters until a real violation is no longer detectable. It comes first because it is the whole motivation in one picture: more counters are an opportunity and a burden. Its caption is long and explains each panel and how data was counted (descriptive plus takeaway).
- Carrier figures: Fig. 2 (pipeline with the model cone and the confidence regions) and Fig. 3 (four geometric panels showing why dropping a counter, or substituting a similar-but-different counter, hides a violation; the panels turn an abstract claim into a picture one can check by eye).
- Table 1: three example constraints from the Haswell MMU with their counter counts (2, 12, 8 counters) showing that even "simple" constraints are intricate; the Count column is the evidence for the "constraints are hard by hand" claim.

### 10. Why it reads as strong, and what does not transfer
Three moves to copy:
1. Open the introduction with a concrete refuted assumption (Intro P4: a widely held inequality fails on real hardware) before any definition, so the reader wants the tool (Section 1, "Address translation provides a prime example").
2. The promise-versus-reality pair of bold run-in paragraphs, whose two challenges map one to one onto the three insights that follow (Intro P3, P5, P6).
3. Honest scoping: the paper says what is not established ("full confirmation would require proprietary RTL"; "a first proof-of-concept study"), and still keeps strong verbs where evidence is direct (Section 7 and Section 9).

Particular to this topic, not to copy: the convex-geometry vocabulary and the page-walk detail; also the lack of any number in the abstract and contributions works for a discovery paper, but a benchmark paper has numbers to show.
