# The argument frame that holds a paper together

## What it is

A short numbered list, usually three items (four in Fusion-3D, Lifetime, NoCap, vCXLGen has five), that
names what is missing in existing work. The same words are then used in every later place the reader
needs to check a promise. In the sample, the frame appears in these places:

| Place | What happens to the items |
|---|---|
| Introduction, problem paragraphs | The items are stated as gaps or challenges, often one bold run-in paragraph each |
| Introduction, answer paragraphs | Each item is answered in the same order, each with its own number |
| Contribution list | The same order again, with section pointers |
| Overview figure and text | Each component is tagged with the item it answers |
| Design sections | Section or subsection titles repeat the item names |
| Evaluation | The opening paragraph lists the claims in the same order. Ablation arms add one item at a time |

## Worked examples from the sample

- **vNPU (MICRO 2024).** Three bold run-in gaps ("Lack of system abstraction support", "Lack of
  architectural support", "Lack of ISA support"). Each gap paragraph ends with a "We need ..." sentence.
  Three contribution paragraphs answer them in the same order. The evaluation opens with three numbered
  claims, each with a subsection pointer.
- **SIGMA (HPCA 2020).** Three named requirements (flexibility, sparsity, scalability) set in the
  Introduction. They become the rows of a comparison table, the subsections of the analysis, and the arms
  of the ablation figure.
- **Fusion-3D (MICRO 2024).** A label convention stated once in the Introduction ("C1 to C4 for challenges,
  T1 to T4 for techniques"). The overview figure marks which technique sits where. Section headings and
  ablation items carry the same tags.
- **Orion (ASPLOS 2025).** Three bold challenge paragraphs (vector packing, bootstrap placement,
  programmability), then three solution paragraphs that each carry a number. There is no overview section,
  because this pairing does the job.
- **Lifetime-Aware Design (ASPLOS 2026).** Three gaps in the design stack (benchmarks, processors,
  methodology) become three named artifacts. A single quantity, lifetime, is called a first-class design
  parameter in the title, the abstract, the Introduction and the evaluation question. Each section opens
  with a sentence that hands off from the previous finding ("These findings motivate X").
- **DynamoLLM (HPCA 2025).** A numbered list of sources of variation in the Introduction is reused as the
  structure of the characterization section, then as three insights, then as four design principles.
- **Centauri (ASPLOS 2024).** Two challenges, each followed in the same paragraph by its insight. The
  insights become named triplets (three partition dimensions, three scheduling tiers).

## How to choose the items

An item is good when all three hold:
1. It is a distinct failure of existing approaches, and the paper can say which approach fails and why.
2. One component, loop or mechanism of the paper answers it.
3. One experiment or ablation can show that the answer works.

If two items are answered by the same component, merge them. If a component answers no item, the
component is either unmotivated or belongs inside another item's answer.

Give each item a short noun phrase and never change the words. A reader should be able to say the
paper's thesis as one phrase (Lifetime: "lifetime as a first-class design parameter").

## Device variants

- Bold run-in labels, one paragraph per item (vNPU, Orion, CounterPoint, Constable "Key limitation",
  "Key mechanism", "Key results").
- Inline numbering, "(1) ... (2) ... (3) ...", in one sentence of the abstract and again in the
  Introduction (SmoothE, Lifetime, DynamoLLM).
- Challenge and technique tags, C1 to C4 and T1 to T4 (Fusion-3D).
- Observation and insight numbering, Ob1 to Ob5 feeding Insight 1 to 6, then "We follow Insight N to
  design X" at the start of each design part (MoE patterns paper, DynamoLLM).
- Research questions as section headings, listed once up front (Isaria, five questions).
- A promise-versus-reality pair of paragraphs, then three insights (CounterPoint).

## The need sentence

Each gap paragraph ends by turning the gap into a requirement: "We need to ...", "Therefore, X with
proper Y is the key issue." This is what lets the answer paragraph read as a consequence and not as a
product announcement.

## Failure modes seen when a draft lacks the frame

- Five or six components listed in one sentence with equal weight and no order.
- The Introduction gaps, the contribution list and the section titles use different words for the same
  thing.
- A contribution that answers no stated gap, or a stated gap that no contribution answers.
- An Overview that restates every component in one paragraph, which duplicates the design sections.

## Test before writing

Write the frame as a three-column table: item, which existing approach fails and why, which component
answers it and where it is evaluated. If any cell is empty, fix the frame before writing prose.

## Where to read the examples

Each example above has a full-paper note in `full-paper-notes/`: `micro-2024-vnpu`, `hpca-2020-sigma`,
`micro-2024-fusion3d`, `asplos-2025-orion`, `asplos-2026-lifetime`, `hpca-2025-dynamollm`,
`asplos-2024-centauri`. The notes record where each frame item appears (Introduction paragraph, contribution
item, figure tag, evaluation claim). They describe a sample of 24 papers, so treat the frequency as a
tendency and not as a rule.
