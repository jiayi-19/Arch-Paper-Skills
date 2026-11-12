# micro-2024-nocap: Accelerating Zero-Knowledge Proofs Through Hardware-Algorithm Co-Design

### 0. Identity
- Title: Accelerating Zero-Knowledge Proofs Through Hardware-Algorithm Co-Design (the accelerator is called NoCap)
- Venue and year: MICRO 2024.
- Award: Best Paper Candidate.
- Contribution type: accelerator, built by hardware-algorithm co-design (it also selects and re-implements a new proof scheme for the hardware).
- Pages: 14 including references (about 13.6k words raw; body about 9.7k words).

### 1. Skeleton
Roman numerals, lettered subsections. Word counts approximate (two-column extraction interleaves text; the figure and abstract text on page 1 are mixed).

| Section | ~Words | Role | Figs/Tables |
|---|---|---|---|
| Abstract | 260 (11 sentences) | abstract | 0 |
| I Introduction | 1000 | intro with bold run-in labels | Fig 1 (page 1, above the abstract text) |
| II Background (A zk-SNARK structure and design space, B R1CS arithmetization) | 1800 | background | Fig 2 |
| III ZKP Algorithmic Tradeoffs | 1200 | motivation and insight (which proof scheme to accelerate) | Table I |
| IV NoCap Architecture (A vector ISA and data types, B pipeline and functional units, C memory system, D system integration, E generality) | 1300 | overview and design (hardware) | Fig 3 |
| V Mapping Spartan+Orion to NoCap (A key tasks, five task families) | 2150 | design (algorithm-to-hardware mapping) | Fig 4, Listing 1 |
| VI NoCap Implementation | 200 | implementation | Table II |
| VII Methodology (A parameters, B benchmarks) | 270 | methodology | Table III |
| VIII Evaluation (A performance, B breakdown, C effect of protocol optimizations, D sensitivity, E design space, F end-to-end) | 1500 | evaluation | Figs 5 to 8, Tables IV, V |
| IX Additional Related Work (A prior ZKP acceleration, B GPUs and FPGAs, C FHE accelerators) | 750 | related work | 0 |
| X Conclusion and Future Work | 230 | conclusion | 0 |
Totals: 8 figures, 5 tables, 1 code listing. Related work comes after the evaluation and is titled "Additional" because the Introduction and Section III already compare against prior accelerators.

### 2. Abstract
- 11 sentences, about 260 words, one paragraph plus Index Terms.
- Functions in order: (1) setting (what a ZKP is); (2) use case (delegating computation with secret data); (3) application list (ML, databases, auctions, voting, blockchains); (4) problem (proof generation is too costly, limiting proofs to very simple computations); (5) approach, with name: "We present a novel accelerator, NoCap, that leverages hardware-algorithm co-design"; (6) headline result (586x over a 32-core CPU, 41x over PipeZK); (7) insight and mechanism (combine two recent hash-based schemes, Orion and Spartan, that perform like prior schemes on a CPU but suit hardware); (8) the cost stated openly (larger proofs) with the counter-claim (end-to-end speedups include prover time, transmission and verification and still justify it); (9) contribution one, hardware organization; (10) contribution two, algorithm implementation; (11) scope and implication (new use cases).
- Numbers: 586x and 41x only. Each is bound to a named baseline ("32-core CPU", "PipeZK, a state-of-the-art ZKP accelerator"); the end-to-end scope is stated in a parenthesis in sentence 8.
- The system is named in sentence 5. Contributions are announced inside the abstract in sentences 9 and 10 ("We contribute ...").

### 3. Introduction
- About 1000 words, 6 prose paragraphs plus a 4-bullet contribution list. Three paragraphs have bold run-in labels.
- P1 definition: what a ZKP is, pointing to Fig 1.
- P2 value: ZKPs are powerful; examples of delegated computation, ML accuracy proofs, voting, auctions, blockchains. Ends with the application list.
- P3 problem and stakes: use is limited because proof generation is 5 to 6 orders of magnitude slower than running the computation; accelerator efforts exist (ASICs, FPGAs, GPUs) and over $100M has been invested. Ends by raising the stakes and leading into "In this paper".
- P4 (bold "A full-system approach to accelerate ZKPs:"): states the system and headline numbers (586x over a CPU, 41x over prior accelerators). Then positions against prior work: prior accelerators target curve-based schemes like Groth16 (tiny proofs, hard to accelerate; PipeZK only 5 to 15x over CPU). Then the insight: combine Spartan and Orion. Admits the cost (megabytes of proof) and argues it is the right tradeoff for many applications (Sec. III).
- P5 (bold "NoCap accelerator:"): the design (a programmable vector processor with units for modular arithmetic, number-theoretic transforms, hashing and shuffles), synthesis result (46 mm2, 62 W), evaluation scope, and the claim that it can accelerate all hash-based ZKPs.
- P6 (bold "NoCap enables new use cases for ZKPs:"): concrete before and after numbers (an image proof that takes over 12 minutes on a CPU takes about a second; a verified database goes from 2 to 1,142 transactions per second at 1-second latency; differentially private training verification from 100 hours to under 30 minutes). Ends with a growth-of-demand statement.
- Contributions (4 bullets, introduced by "In summary, our key contributions are:"): (1) an observation (the Spartan+Orion combination is highly accelerable), a finding; (2) a novel programmable accelerator, a component; (3) a high-performance implementation of the algorithm for this hardware, a mechanism; (4) a detailed synthesis and performance evaluation, a result ("transformative speedups", no number). Every bullet ends with a section reference. The numbers are in P4 to P6, not in the bullets.
- Problem posing: first the cost gap (orders of magnitude), then why prior accelerators fall short (the scheme they chose). The key insight (choose an accelerator-friendly scheme, accept bigger proofs) first appears in P4. Prior work is credited as an engineering step, then limited by the scheme it accelerated. There is no formal challenges list; the nearest is a paragraph in Section II ("Finding a zk-SNARK that is secure, performs well, and is amenable to hardware acceleration is challenging").
- The results-preview is spread across P4, P5 and P6 and always names the baseline and the scale.

### 4. Motivation and background
- Section II is background (tutorial on zk-SNARK structure with Fig 2, an anatomy diagram with numbered steps 0 to 3; R1CS). Section III ("ZKP Algorithmic Tradeoffs") is the motivation and holds the paper's key argument.
- Evidence in III is analytical plus measured: Table I compares end-to-end time (prover, send proof, verifier) for Groth16 and Spartan+Orion on a CPU and on their accelerators for a 16M-constraint proof. The table already includes NoCap's result (586x faster proof generation; end-to-end 7.4x better than PipeZK) so the reader sees the payoff of the choice.
- Observations end in explicit reasoning, not in boxes. The key passage is a bold run-in "Disentangling algorithmic efficiency, software efficiency, and acceleration potential:" followed by a numbered list of three factors with exact multiplication of ratios (4.94x fewer multiplies; the CPU version only 1/1.74 as efficient; PipeZK is CPU-bound and capped at 6.7x). The last point ends with an arithmetic closure that explains the 41x gap.
- Tie to design: Section III names what the architecture must exploit (the same primitives), and Section IV forward-references Section III, and Section V details the mapping.

### 5. Overview of the design
- Section IV opens with Fig 3 (NoCap architecture and physical organization: a wide vector processor with functional units, a banked register file, HBM) and a one-paragraph walk of the machine: wide-vector functional units, explicitly managed memory hierarchy, static scheduling.
- A roadmap sentence lists the subsections with section pointers ("We first describe NoCap's ISA and data types (Sec. IV-A), then its FUs ... (Sec. IV-B) ...").
- Generality is handled in a short subsection IV-E: all hash-based schemes share the same primitives, so NoCap should extend to others.
- The key insight (accelerator-friendly scheme) was already established in Section III, so Section IV is purely how the hardware realizes it.

### 6. Design sections
- Pattern in IV: define the data and operations, state a sizing rule (units sized by reuse and usage frequency; the hash and shuffle units sized to match HBM bandwidth), then give the cost that results. Static scheduling is justified by one property of the workload ("ZKPs are regular programs"), then its cost and benefit are stated.
- Section V uses a task taxonomy (Fig 4: algorithms to tasks to primitives, with CPU runtime percentages) and then one subsection per task family, each in the form: what the task is, why it is hard on hardware, how NoCap maps it, and the optimization (recomputation of sumcheck inputs reduces memory traffic by 31%).
- Worked example in the text: Listing 1 shows the sumcheck dynamic-programming algorithm, then the paragraph explains why it is memory-bound.
- Component names are stable (NoCap, FU, register file, Beneš network, Spartan+Orion, task names).
- Details moved: hash and cryptography details are explicitly skipped ("they are not needed to understand its performance"), instead of an appendix.
- Figures: block diagram, anatomy diagram with numbered steps, dependency graph of algorithms, power/area charts.

### 7. Evaluation
- Not organized by research questions but by analysis type: performance, breakdown, effect of protocol optimizations, sensitivity, design space, end-to-end.
- First result (VIII-A, Table IV): proof generation time for each benchmark vs CPU and PipeZK; gmean 586x (range 560x to 622x) vs the CPU and gmean 41x (25x to 53x) vs PipeZK.
- Claims are bounded by baseline (a 32-core Threadripper running Spartan+Orion enhanced by the authors, libsnark for Groth16, an iso-area scaled PipeZK) and by scale (benchmarks scaled up 100x to 1,000x from prior work, constraints up to 2^30). Baseline fairness is spelled out in Methodology: PipeZK is optimistically scaled, uses a faster curve than in its own paper, and the authors' CPU baseline already includes their optimizations (over 2x faster).
- Ablations: VIII-C reports three protocol optimizations, with CPU and NoCap effects given separately (the field change gives 1.7x on a CPU; Reed-Solomon codes 1.2x; recomputation helps NoCap 1.1x and slightly hurts the CPU by 1%, which is why it is NoCap-only). Sensitivity (Fig 7) sweeps each unit; design space (Fig 8) shows a Pareto frontier and argues the chosen point is where the curve flattens.
- Negative or weak results: the abstract and Section III say the proofs are larger; Section III states that for use cases with many verifiers (public blockchains) verification cost may be too high and defers a fix (recursive proofs) to future work.

### 8. Sentence and paragraph habits
- Mean sentence length about 26 words (median 22). Paragraphs 100 to 250 words. Present tense; "we" about 130 times, "our" about 23. The system name is the subject in design and evaluation text.
- Punctuation: 4 em dashes and 5 en dashes in the body (low), about 28 semicolons (higher than the other three papers), about 160 parentheses, about 76 colons (many from bold run-in labels with a colon, and numbered lists).
- Bold run-in headings in the Introduction and Section III. Numbered lists inside paragraphs. Footnote explains the name (a pun) and nothing else.
- Hedging is light ("may", "can" about 55). Numbers: multiplicative speedups with a named baseline ("586x faster than a 32-core CPU"), plus ranges ("from 560x to 622x").
- Patterns:
  1. "NAME generates proofs A faster than a B, and C faster than PRIOR, a state-of-the-art ... accelerator."
  2. "To achieve these speedups, we take an end-to-end systems design approach: instead of focusing on X accelerated by prior work, ..."
  3. "However, this comes at the expense of larger proofs. We show that for many applications ... trading A for B ..."
  4. "Finding a X that is secure, performs well, and is amenable to hardware acceleration is challenging. This is because ..."
  5. "To our knowledge, we are the first to ..."
  6. "Table N shows that ..., so it may seem puzzling why ... There are three key factors that contribute to ..."
  7. "We first describe A (Sec. N), then B (Sec. N) and C (Sec. N)."
  8. "In summary, our key contributions are: [bullets each ending with (Sec. N)]."

### 9. Figures and tables
- First figure (Fig 1) is a small concept diagram: prover, verifier, statement, a trust barrier, a small proof, and an accelerator icon beside the prover. It sits at the top of page 1, so the reader sees what a ZKP is before reading.
- Captions are descriptive ("Anatomy of a zk-SNARK", "Cryptographic components of Spartan+Orion, along with tasks (w/ CPU runtime percentages) and computational primitives"), with the legend for arrows spelled out; the takeaway goes in the text.
- Argument-carrying: Table I (end-to-end Groth16 vs Spartan+Orion on CPU and accelerators with proof size and verifier time shown, not only prover time), Fig 4 (algorithm to task to primitive graph with CPU percentages that show every task must be accelerated), Table IV (the headline speedups).
- Table design: columns for prover, send, verifier, total; baselines in rows; the proof sizes are in the caption.

### 10. Why it reads as strong, and what does not transfer
Moves to copy:
1. The abstract names the cost of the approach (larger proofs) and answers it with an end-to-end measure in the same sentence (Abstract, sentence 8; repeated in Introduction P4 and Section III).
2. Introduction P6 turns the speedup into concrete use-case numbers (12 minutes to about 1 second, 2 to 1,142 transactions per second), so "transformative" has a visible meaning.
3. Section III ("ZKP Algorithmic Tradeoffs") breaks the 41x gap over the prior accelerator into three numbered factors and multiplies them out, so the reader trusts the headline number before any hardware is described.
- Does not transfer: cryptography background (Section II) and the task-by-task mapping in Section V, which exist because the hardware needs this algorithm.
