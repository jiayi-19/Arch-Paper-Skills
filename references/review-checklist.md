# Review checklist

Run this on a draft section before delivery. Each item is a yes or no. It adds argument-level checks to
the source and evidence checks in `workflow.md` and the scripts.

## Structure
1. Can the argument frame be written as three or four short noun phrases, each with the existing approach
   that fails and the component that answers it? If not, fix the frame first (`argument-frame.md`).
2. Do the Introduction gaps, the contribution items, the overview components and the evaluation questions use
   the same words in the same order?
3. Does each contribution item state a finding or a capability and carry a number or a contrast? Is at least
   one item a finding? (`contributions.md`)
4. Is the overview short (150 to 350 words in most papers), tied to a figure, and free of method detail that a
   later section explains? (`full-paper-structure.md`)
5. Is each claim earned before the design appears, by a measured motivation, an oracle or headroom study, a
   cheap failing baseline or a concrete refuted assumption?
6. Does each observation end with a sentence that turns it into a requirement?
7. Is there a place where the paper reports a cost, a loss or a case where the plain baseline wins?
8. Is the first figure the setting, the gap or the central object, and not a result?

## Sentences
9. Does each paragraph have a topic sentence with a concrete subject (the system, the object, the
   evaluator) and a closing sentence that sets up the next paragraph?
10. Is every number stated with its baseline, its scope word and, for results, its cost?
11. Are names stable from the Introduction to the evaluation?

## Common failure modes in drafts
- A question or a gap that appears with no setup.
- Saying a method "cannot" do something without saying concretely what works today and what fails, or
  blaming the wrong cause (the technology is hard) when the failure is of the existing approach.
- Parallel paragraphs that open with the same word and read as a ledger.
- Comparing two things on a dimension where they do not differ.
- Abstract sentences that say nothing concrete. Evidence placed under a point it does not support.
- A comparison with related work placed in a motivation paragraph with no stated purpose.
- Revealing the method inside a problem paragraph, or spending all the motivation in the Introduction when a
  background section exists for it.
- A contribution list that names components and counts (a feature list) and an overview that gives every
  component equal weight with no focus.
