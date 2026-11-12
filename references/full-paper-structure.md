# Whole-paper structure: length, chain and moves in the second sample

These counts come from the 24 papers with full-paper notes (20 prize papers and 4 benchmark papers, `full-paper-notes/`). "About half" means 8 to 12 papers. They complement `corpus-profile.md`, which measures the Abstract and Introduction of the first 24 papers. The two samples differ (the first has many test-of-time papers, the second is recent systems, accelerator and framework work), so quote both when a number matters. Abstract median 226 words (first sample) against about 200 (second). Introduction median 762 against about 900.

## Abstract

- 6 to 14 sentences, 158 to 301 words, median about 200. One paragraph in most, two in about a quarter.
- Common chain: setting, the problem or gap, the approach with the system name (sentence 3 to 5 in most,
  sentence 1 in Lifetime), the mechanism or components, results with the baseline named, scope.
- Several abstracts have no result number (Cerberus, PIM Pathfinding, Mess, CounterPoint, vCXLGen), so a
  number is not required. When a number is present, the baseline is in the same sentence.
- NoCap's abstract states the cost of its approach (larger proofs) and answers it with an end-to-end
  measure in the same sentence.
- An inline numbered list of the components inside one sentence appears in Lifetime and SmoothE.

## Introduction

- 700 to 1350 words, 4 to 12 paragraphs, median about 900 words. Paragraphs are 90 to 170 words.
- Typical chain, with the number of papers that follow it closely in parentheses (the other papers vary
  this, none skips the problem paragraph):
  1. Setting and why it matters, one or two paragraphs. The last sentence prepares the problem.
  2. Existing work credited and its residual cost. The credit sentence makes the next "However" land
     (Fusion-3D, MetaSapiens, Orion).
  3. The challenges, as bold run-in paragraphs (vNPU, Orion, CounterPoint, Constable, NoCap) or as one
     sentence with inline numbering (SmoothE, Lifetime, DynamoLLM).
  4. The key insight. It is at about 30 to 40 percent of the Introduction in Lifetime (P4 of 6 plus
     contributions) and at paragraph 3 to 5 in most others. One sentence states it, one example makes it
     concrete.
  5. The system is named in the answer paragraph, in a sentence of the form "To address these challenges,
     we present [Name], a [type] that [verb]". Then one paragraph per challenge, each with one number.
  6. A results paragraph with headline numbers (about half).
  7. The contribution list (see `contributions.md`).
  8. A roadmap paragraph appears in only a few (SIGMA, SmoothE). It is not required.
- Opening devices that work in the sample: a concrete refuted assumption (CounterPoint), a counterfactual
  "if this were fully unpredictable" before the thesis "Fortunately" (MoE patterns), the question form of
  the insight anchored by a tiny example (PF-LLM), an oracle study previewed (Constable).
- No Introduction in the four system papers puts a results figure on the first two pages. The first
  figure shows the problem, the gap or the central object.
- Related work is not discussed in the Introduction in Lifetime. Others credit and dismiss prior work in
  one or two sentences inside the problem paragraphs, and put the full comparison in a table or a late
  section.

## Background and motivation

- Present as its own section in most papers. Absent in Orion (the Introduction does the job) and merged
  with related work in Lifetime (a gap table with three rows that become the three components).
- Evidence is measured on a real platform or a trusted model in most: vNPU measured TPUv4 for 11 models,
  DynamoLLM a characterization of variation, Constable an oracle headroom study (ideal Constable 9.1
  percent against ideal value prediction 4.3 percent), H2-LLM a roofline and a measured controller area
  share, Fusion-3D a table of bandwidth needed against what a real port offers.
- Each observation ends with a sentence that turns it into a requirement: a boxed "Insight #N" with the
  observation then what the system must do (DynamoLLM), "We conclude that ..." (Constable), a numbered
  "Takeaway" line (H2-LLM), a "we need to ..." sentence (vNPU).
- The observations are tied to the design one to one, by section pointers inside the text.
- Cheap failing baselines make the strongest motivation: Isaria's off-the-shelf tool, Mess's measurement of
  every existing simulator against real hardware (Section IV before the new simulator in Section V).

## Overview of the design

- About half of the papers have a labeled overview or architecture subsection. Its length is 150 to 500
  words (CounterPoint's is 1,500). The rest use the Introduction answer paragraphs plus a roadmap paragraph
  at the start of each design section (Orion, MetaSapiens, SIGMA, SmoothE).
- It carries one figure. The text walks the figure by numbered circles (vCXLGen, Centauri, Cerberus,
  Constable, vNPU) or by component (H2-LLM, MoE patterns, Fusion-3D). Each step says what is received and
  what is produced.
- It maps frame items to components: Fusion-3D tags the blocks of the figure with C and T labels, Centauri
  maps challenge one to dimensions 1 to 3 and challenge two to tiers 4 to 6.
- It carries forward references with section numbers and defers detail. It does not restate the key
  insight at length (Fusion-3D defers it, Constable gives the insight its own section before the design).
- A roadmap sentence of the form "We first present A (Sec. X). Based on this, we enable B (Sec. Y) and C
  (Sec. Z)" opens the design in vNPU, NoCap and others.
- A bounded-scope paragraph at the start of the design ("Domain of ...: L1D, single core, x86-64") takes the
  sting out of later limits (PF-LLM).

## Design sections

- Subsection pattern: need, then mechanism, then expected consequence, then cost or constraint.
- Bold run-in labels with a period start most sub-paragraphs (vNPU, Lifetime, Orion).
- A worked example or a toy example is reused (Centauri, SmoothE, vNPU Figures 8 and 18).
- Components keep one name each, from the Introduction to the last result.
- Each design section can end with the list of knobs it exposes, so the exploration section reads as a
  consequence (H2-LLM).
- Out-of-scope items are named and deferred in one sentence ("We leave side-channel mitigation to future
  work").
- Orion marks "Orion:" and "Takeaway:" inside sections that are mostly prior work, so credit and
  contribution never blur.

## Evaluation

- Opens with a list of the claims or the research questions, in the order of the frame (vNPU: four
  numbered claims with subsection pointers; Isaria: five research questions that are also headings).
- The first result is the headline number, or the validation of the simulator when the paper rests on one
  (MoE patterns, PIM Pathfinding).
- Baselines are listed with one line of mechanism each. The proposed design is sometimes framed as the
  middle of a spectrum between two named extremes (MetaSapiens: SMFR and MMFR).
- Ablations are cumulative (a staircase of adding one component at a time: MetaSapiens, SIGMA) or
  remove one component at a time in other work.
- Decomposition tables split a headline factor into named parts with a measured share for each (Orion
  Table 4, NoCap's three numbered factors multiplied out).
- Each result block ends with a bold "Takeaway" or "Key takeaways" (H2-LLM, vCXLGen, PIM Pathfinding,
  Orion), which restates a design rule.
- A weak case is reported and diagnosed: DynamoLLM (savings shrink as load rises), vNPU (high contention
  slows some operators), SIGMA (two GEMMs lost), MoE patterns (gains saturate with hop count), SmoothE
  (adversarial sets where the exact solver wins), Isaria (compile time 2.1x slower).
- A "why it works" analysis after the numbers points at marked regions of one trace (PF-LLM Section 6.4).

## Related work and conclusion

- Related work is late and short or absent: none in H2-LLM, PF-LLM and SmoothE, 270 words in
  CounterPoint, 550 words in four bold run-in paragraphs in vNPU, folded into a gap table in Lifetime.
- The closest work is credited at its first point of comparison and in a comparison table in the
  Introduction or background (Centauri Table 1, Cerberus Table I, Lifetime Table 1).
- Conclusions are 60 to 150 words and add nothing new.
