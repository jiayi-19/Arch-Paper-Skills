# Contribution lists and the contribution paragraph

## What the 20 papers do

Counts from the notes: 3 to 4 items is the norm (a few have 2, 5, 6 or 7). Two papers have no list at all
(Mess and PIM Pathfinding, both characterization or tool papers). Three papers write the contributions as
running prose or numbered paragraphs instead of bullets (vNPU, Lifetime, Mess). Several attach a section
pointer to each item (vNPU, NoCap, Constable).

Item types, as the readers of the notes classified them:

| Type | Example in the sample | Carries |
|---|---|---|
| A finding or analysis | DynamoLLM item 1 (analysis of the opportunities), vNPU item 1 (study of inference on real hardware), MoE patterns (six key insights) | what was learned, usually with a scope |
| A capability | Fusion-3D item 1 (first to support instant reconstruction and real-time rendering at 5 Gbps USB) | what becomes possible, with a number |
| An abstraction or mechanism | Centauri (three-dimensional partition abstraction), Isaria (phase-oriented synthesis) | what is new and what it changes |
| A named artifact with a contrast | Lifetime (benchmark suite "unlike traditional benchmarks that focus on X") | what it is and how it differs from the usual one |
| The evaluation item | most papers, last item | the headline numbers with the baseline named |

The strongest lists mix types: one finding that makes the problem real, one or two artifacts that answer
it, one evaluation item with numbers. DynamoLLM has exactly this shape (analysis, system, evaluation).

## Why a list reads as low-level

- Each item names a component and a count ("a benchmark with 20 designs and 21 tasks") and says nothing
  about what that establishes.
- No item is a finding. The reader learns what was built and never what was learned.
- No item has a number or a contrast with existing work.
- The items are not in the order of the gaps.

## How to write an item

An item has three parts: the delivered object, what it establishes or enables, and one number or one
contrast with the usual approach. Templates seen in the sample (fill the blanks from facts only):

1. "We show that [existing approaches fail on X] because [cause]. [Quantity] changes by [N] when only
   [factor] is varied (Section N)." (finding)
2. "We present [Name], a [object] that [does what] so that [capability]. Unlike [usual practice], it
   [difference] (Section N)." (artifact with contrast)
3. "[Name] achieves [N]x on [workload set] against [named baseline], with [cost] (Section N)."
   (evaluation, with the baseline in the same sentence)
4. "To the best of our knowledge, [Name] is the first to achieve both [A] and [B]." (priority claim, use
   only when checked; Fusion-3D, Lifetime and others do, and some of those claims are weakly supported)

## Order and coverage

- Same order as the frame. Every frame item has at least one contribution and every contribution answers
  an item.
- The last item is the evaluation. It names the number of tasks, the headline results with their
  baselines, and the control that matters (for example, the control that gives the baseline the same
  information).
- Keep each item to two or three sentences. Longer items become the answer paragraphs of the Introduction
  (Orion, vNPU) and the list shrinks to a one-line recap.

## The results paragraph that precedes the list

Papers that include it (about half) place one paragraph with the headline numbers before the list. Each
number carries its baseline and scope in the same sentence ("up to", "geomean", "against the best
baseline"). Abstract numbers are sometimes against a weaker baseline than the body (Fusion-3D reports
same-algorithm baselines in the abstract and the stronger best-baseline numbers only in the body), so
state in the Introduction which baseline each number uses.
