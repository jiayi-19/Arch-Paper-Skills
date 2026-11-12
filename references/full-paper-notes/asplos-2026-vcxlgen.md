# asplos-2026-vcxlgen: vCXLGen: Automated Synthesis and Verification of CXL Bridges for Heterogeneous Architectures

Reading notes. Text extracted with pdftotext; word counts are approximate.

## 0. Identity
- Title: vCXLGen: Automated Synthesis and Verification of CXL Bridges for Heterogeneous Architectures
- Venue and year: ASPLOS 2026 (Volume 2, Pittsburgh). Award: ASPLOS 2026 Best Paper.
- Contribution type: automation (a generator) plus verification method, with a new abstraction (the CXL bridge) and a simulator backend. It is closest to 'system or framework'.
- Pages: 20 including references and an artifact appendix. About 11,000 words in the body (sections 1 to 11).
- Full text used: https://dhschall.github.io/assets/pdf/VCXLGEN_ASPLOS26.pdf (first author's site, open). DOI 10.1145/3779212.3790245.

## 1. Skeleton
| Sec | Heading | Role | Words | Figs / tables |
|---|---|---|---|---|
| Abstract | | | 180 | 0 |
| 1 | Introduction | | 860 | 0 |
| 2 | Background | background (CXL, MCMs, CC protocols) | 320 | Table 1 |
| 3 | Motivation (3.1 The Case for a CXL Bridge, 3.2 Design Goals, 3.3 Research gap) | motivation, goals, gap | 1,040 | Fig 1, Fig 2 (placed here, used in 4) |
| 4 | vCXLGen Overview | overview | 240 | Fig 2 (workflow) |
| 5 | CXL Bridge Architecture (5.1 System Model, 5.2 Operating Principles) | design (abstraction) | 510 | Figs 3, 4 |
| 6 | Automated Synthesis of CXL Bridges (6.1 to 6.8) | design (algorithm) | 2,700 | Alg 1, Figs 5, 6, 7 |
| 7 | CXL Bridge Memory Consistency Model | design (formal semantics) | 840 | Fig (execution graph) |
| 8 | Automatic Verification of CXL Bridges (8.1 to 8.3) | design (verification) | 1,350 | Figs 8, 9, 10 |
| 9 | Evaluation (9.1 to 9.6) | evaluation | 2,500 | Tables 2 to 5, Figs 11 to 15 |
| 10 | Related Work | related work | 290 | 0 |
| 11 | Conclusion | | 85 | 0 |
| A | Artifact Appendix | artifact | about 1,000 | 0 |
Total: about 15 figures, 5 tables, 1 algorithm. Section 6.8 'Discussions' holds limitations and design choices in the middle of the design section.

## 2. Abstract
- 9 sentences, about 180 words, in two paragraphs.
- Functions: (1) setting: CXL offers coherent remote memory; (2) problem: the spec lacks safe interoperability across heterogeneous protocols; (3) why it matters: semantic gap blocks adoption; (4) concept: CXL bridges; (5) system: vCXLGen, 'the first system' to synthesize and verify them; (6) announces two core contributions with (1) and (2) inline; (7) evaluation on generality and extensibility; (8) performance claim: comparable to manually designed homogeneous protocols; (9) correctness: proves safety and liveness, scalable.
- Numbers: none. All results are qualitative claims ('comparable', 'significant scalability').
- System named in sentence 5. The contribution count ('two core contributions') is already in the abstract, with the same wording as in the introduction.

## 3. Introduction
- 9 paragraphs, about 860 words, ending in a 2-item contribution list. Paragraphs are short (about 90 words).
- P1: data center heterogeneity, so a standard interconnect is needed. Ends on 'standardized interconnect', which opens P2.
- P2: CXL as the standard, v3.0 adds multi-host coherence. Ends on a benefit; 'Unfortunately' opens P3.
- P3: "Unfortunately, the CXL v3.0 specification lacks ..." states the problem as a semantic gap between protocols and consistency models. Ends by saying the gap blocks broader CXL adoption.
- P4: "This semantic gap manifests in two key dimensions" with Firstly (CC protocols differ from CXL.mem) and Secondly (vendors differ on consistency).
- P5: "To systematically address these challenges, we introduce the concept of a CXL bridge". Describes the abstraction, with a vision sentence (a drop-in component for any host).
- P6: "Realizing an effective CXL bridge entails addressing five key requirements" with five inline numbered items (generality, automated synthesis, consistency, correctness, performance).
- P7: 'To meet these requirements, we present vCXLGen, the first system ...' then 'Notably, vCXLGen tackles three key challenges' with numbered items (protocol combination, verification scalability, performance evaluation).
- P8: 'Our evaluation demonstrates the effectiveness of vCXLGen across several key dimensions', walking generality, extensibility, performance, verification in the same order as the evaluation. Counts appear (35 applications, 3 suites) but no performance numbers.
- P9: "Overall, our paper makes two core contributions:" followed by two items.
- Problem posed as a missing mechanism in a standard (spec lacks safe interoperability), not as a slow baseline.
- Key insight: not stated as a sentence. The concept (the bridge, and compositional verification) takes the insight's place. The phrase novel compositional approach marks it in P7.
- Prior work: credited and dismissed in Section 3.3 ('Research gap'), not in the introduction. The introduction has no related-work paragraph.
- Challenges device: yes, twice. Five requirements (P6) and three challenges (P7), each as inline numbered lists in running text. The requirements reappear as five design goals in 3.2 and as the five evaluation dimensions in Section 9. This is a closed loop.
- Contributions: 2 items, each with a bold lead-in: 'Automated synthesis of CXL bridges' (capability and component) and 'Automated verification of CXL bridges' (capability and method). Numbers appear in item 2 (216 litmus tests); no performance numbers.
- Results preview: P8 is a qualitative walk of the evaluation axes, not a number paragraph.

## 4. Motivation and background
- Yes: separate Section 2 Background (CXL, MCMs, CC protocols; with run-in bold terms) and Section 3 Motivation.
- Evidence is by example and analysis: Figure 1 shows an Intel x86 plus Arm system on shared CXL memory with local protocols (MESI, MOESI) and a global CXL.mem, with '???' between them. Section 3.1 gives concrete protocol differences (a BIConflict handshake in CXL MESI that textbook MESI lacks; release consistency requests that depend on a release event). No measured motivation.
- Section 3.1 ends with an explicit research question set off as a bold run-in ("Research question: How can we automatically synthesize and verify a CXL bridge for heterogeneous multi-host CC?"). 3.2 gives five numbered design goals, and 3.3 'Research gap' names Hieragen, HeteroGen and Compound MCMs one by one and says why each cannot serve CXL (MESI-only; needs prior knowledge of all protocols; state explosion above four cache controllers; abstracts away concurrency).
- Ties to design: one-to-one by numbering (five goals match five requirements). The proposed solution is paired with each failed prior approach in the final paragraph of 3.3.

## 5. Overview of the design
- Section 4 is short (about 240 words) and has a bold run-in 'System workflow.' Figure 2 is a left-to-right pipeline: inputs (specs of global and local protocols), the ProtoGen parser, bridge synthesis, outputs (gem5 SLICC controllers and verification models).
- The text walks Figure 2 through circled numbers 1 to 6, one clause per step. The caption restates the same numbers and mentions that pipelines run in parallel per local protocol.
- It names the generator's input format (ProtoGen DSL) and what it outputs (verifiable models, simulator implementations), then forward-references later sections by their contents. Section 5 then restates the architecture with another numbered figure (Figure 3, ten circled steps).

## 6. Design sections
- Subsection pattern in Section 6: Intuition (bold run-in), then the algorithm (Alg 1) with a running example (MESI + CXL store miss from Shared), then pass 1 (semantic translation), pass 2 (state space, propagation, nesting), then static analysis, transient states, discussion.
- A single running example ('store miss from a shared state') is reused in Figure 4, Figure 5, Figure 6 and in text with the same circled numbering. Every algorithm step is tied to a line number (for instance, a line number of Alg. 1 is cited for the equivalentAccess step).
- Three bridging rules are named and bolded as bullets (Delegation, Nesting atomicity, Selective stalling) and then reused every time a design step is justified (the text keeps saying a step satisfies the selective stalling rule).
- Section 6.8 'Discussions' uses bold run-in headings (Non-SWMR global protocol; Vendor-specific optimizations; Non-atomicity) to defend design choices and state limits, including a deadlock example for the alternative design.
- Section 7 (formal MCM) and Section 8 (verification) are separate design-level sections; the verification section states properties, rationale, challenge (full-system state explosion), then the compositional method in 8.3 with a cluster abstraction figure.
- Details left out: transient state generation details are only described in prose; implementation size is given in 9 (about 18,000 lines of Python).

## 7. Evaluation
- Organized by five dimensions announced in the first paragraph of Section 9 and matching the introduction: generality (9.1), extensibility (9.2), correctness (9.3), scalability of compositional verification (9.4), performance (9.5) and KVS (9.6). Not stated as numbered research questions.
- First result: generality (Table 2: which protocol combinations produce bridges, with state and transition counts).
- Each subsection ends with a bold 'Takeaways.' paragraph (9.3, 9.4, 9.5) or 'Takeaway.' (9.6) that restates the finding in one or two sentences and names the cause.
- Claim bounding: baseline is a hypothetical ideal system with a homogeneous modified gem5 MOESI protocol. Compositional verification is compared to full-system model checking; the 98% memory reduction is bounded by a note that the large baseline ran out of memory at 1.8 TB, so the true reduction is likely larger. Calibration of workloads (scaled inputs with matched miss ratios) is stated.
- Negative or weak results: CXL-Br is up to 20.3% slower in seven applications (mostly Phoenix). The text gives a mechanism for each, 6 remote message delays versus 3 for dirty owners, blocking states at the CXL directory, and says the cause is the protocol, independent of vCXLGen. Compositional verification is worse for small systems (two caches or fewer), and the paper says so. A good result is also explained away: fluidanimate is 20% faster only because gem5's MOESI lacks the E state.
- No ablation of the design. The ablation role is played by the three protocol combinations (MOESI baseline, MESI-Br, CXL-Br) that separate bridging cost from CXL protocol cost.

## 8. Sentence and paragraph habits
- Average sentence length about 23 to 26 words. Intro paragraphs about 90 words; design paragraphs 100 to 180.
- 'We' about 170 times in the full text. Present tense for design and for results (Figure 12 'presents' trends).
- Bold run-in headings are heavy: 'System workflow.', 'Intuition.', 'Example.', 'Bridging rules.', 'Methodology.', 'Memory usage.', 'Execution time.', 'Takeaways.'. Inline numbered lists '(1) ... (2) ...' are common inside paragraphs.
- Semicolons about 50 in the whole text including math; em dashes about 14; many parenthetical examples ('e.g., MESI, RCC').
- Hedging is light (intuitively, informally, we believe).
- Numbers: percentages with baseline and condition in the same sentence ("92% for the medium and over 98% for the large system").
- Sentence patterns:
  1. "Unfortunately, ___ lacks ___, creating a significant obstacle for ___."
  2. "___ manifests in two key dimensions. Firstly, ___. Secondly, ___."
  3. "To systematically address ___, we introduce the concept of ___: an abstraction that ___."
  4. "Realizing an effective ___ entails addressing five key requirements: (1) ___ (2) ___ ..."
  5. "Research question: How can we ___?"
  6. "Prior works on ___ all fail to cater to ___. X ___, but is limited to ___."
  7. "Takeaways. We find no ___ in ___ and no ___, confirming ___."
  8. "Our evaluation shows that ___ is general, i.e., it supports ___ and is easily extensible when ___."

## 9. Figures and tables
- First figure (Figure 1, in Section 3): the Intel and Arm heterogeneous system with a '???' marker between the two protocols. It poses the gap visually. It appears in Section 3, after text-only Sections 1 and 2.
- Caption style: descriptive for design figures (Figure 3: 'CXL bridges operating principle. Local flows (...) ... '), takeaway-leaning in results (Figure 12: names what is plotted). Several captions use circled step numbers that the text then cites.
- Carrying figures: Figure 2 (workflow), Figure 4/6 (same transaction at three levels), Figure 11 (memory and time for full-system versus compositional checks, with OOM bars labeled '>1.8 TB').
- Tables: Table 2 (protocol combinations, with state and transition counts), Table 3 and 4 (verification strategy and litmus tests as a grid of pass counts), Table 5 (simulator parameters).

## 10. Why it reads as strong, and what does not transfer
Three moves to copy:
1. A closed loop of lists: five requirements (Intro P6), five design goals (3.2), five evaluation dimensions (Section 9) and three challenges (Intro P7) are the same numbered frame reused. The reader can check each promise.
2. A 'Research gap' subsection (3.3) that names each prior system and states in one sentence why it fails on the target (limited to MESI family; needs all protocols known upfront; breaks beyond four caches). This sets up the contribution as the only thing that closes all gaps.
3. Bold 'Takeaways.' paragraphs at the end of every evaluation subsection, and honest bounding of the biggest numbers (the 98% claim carries a note that the baseline ran out of memory, so the real gain is larger).

Not to copy: the formal axiomatic memory-model section and the litmus-test machinery; they belong to a protocol-verification paper. Also the abstract has no numbers, which suits a 'first system' claim but is weaker than a numeric abstract.
