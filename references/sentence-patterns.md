# Sentence habits and a pattern bank (templates of moves, not sentences to copy)

## Statistics from the 20 prize papers

| Feature | Range across papers | Typical |
|---|---|---|
| Mean sentence length (body) | 18 to 36 words | 22 to 28 (SIGMA 18, MetaSapiens 20, PIM Pathfinding 33 to 36) |
| Paragraph length | 60 to 280 words | 100 to 180 |
| Introduction length | 700 to 1350 words | about 900 |
| Tense | present for the design, past for measured results in some | present |
| "we" frequency | 12 to 22 per 1,000 words in four of the papers measured | the system name is the subject of many design sentences |
| Em dashes in body | 0 in about nine papers, about 6 to 26 in six | zero to few |
| Semicolons in body | 0 to 50 | 3 to 25 |
| Hedging | low in most | "may", "can", "typically" for technical possibility, rarely for claims |

Clean-prose models (zero or almost no em dashes, few semicolons): Centauri, Constable, DynamoLLM, H2-LLM,
Mess, PIM Pathfinding, Lifetime, Orion, PF-LLM, vNPU, MoE patterns, MetaSapiens, SIGMA, NoCap. Do not take
sentence rhythm from Cerberus (about 26 em dashes), CounterPoint (about 23), SmoothE (about 19) or
vCXLGen (about 14).

Numbers appear with the unit, the multiplication sign for speedups, "up to" or "geomean" or "on average"
as the scope word, and the baseline in the same sentence.

## Pattern bank (templates, not sentences to copy)

**Setting**
- "[X] is the next frontier of [field]." (Lifetime)

**Credit, then the gap**
- "While [prior work] has addressed [A], it remains a challenge to [target capability]." (Orion)
- "However, existing [class] tend to lean towards either [A] or [B], constraining [C]." (Centauri)
- "Despite [prior work]'s promises, they still fall short in meeting two critical requirements: 1) ...
  2) ..." (Fusion-3D)
- "Yet as shown in Figure N, no prior work has systematically investigated [X]." (MoE patterns)
- "Unfortunately, all tested [tools], including [trusted ones], poorly resemble [ground truth]." (Mess)

**Challenge and need**
- Bold run-in: "Lack of [X] support for [Y]." then "However, [Z] cannot [do it] since [cause]. We need [W]."
  (vNPU)
- "[Bold label]: [why it is hard in two or three sentences]. [Consequence]." (Orion)
- "These limitations underscore two fundamental challenges in [X]." (Centauri)
- "Realizing an effective [X] entails addressing five key requirements: (1) ... (2) ..." (vCXLGen)

**Insight**
- "Our key insight is that [domain] exhibits [property], which makes [quantity] a first-class design
  parameter." (Lifetime)
- "The key insight behind [Name] is that [claim] when the following two conditions are satisfied."
  (Constable)
- "This motivates our central question: can [X] do [Y] automatically?" (PF-LLM)
- "If [X] were fully unpredictable, it would [consequence]. Fortunately, as we later show, [X] indeed
  [has structure] that designers can exploit." (MoE patterns)
- "On the surface, this insight contradicts [objection]. But unlike [prior], [Name] [resolves it]." (Isaria)

**Naming the system**
- "To address these challenges, we develop [Name], a [type] for [task] that [advance]." (Orion)
- "To bridge the gap between the promise and reality of [X], we invent [Name], a framework that [verb]."
  (CounterPoint)
- "To pave the way towards [goal], this paper introduces [Name], the first [type] for [task]." (DynamoLLM)

**Answer, one per challenge**
- "[Bold label]. [What it does]. [Why it works]. [One number]. (Section N)" (Orion, MetaSapiens, NoCap)
- "Challenge C[N]: [Name]. [Recap]. To this end, we introduce Technique T[N] (see Sec. N)." (Fusion-3D)
- "We follow Insight N to design [component] and leverage [property] to build [mechanism]." (MoE patterns)

**Roadmap and hand-off**
- "We first present A (Sec. X). Based on this, we enable B (Sec. Y) and C (Sec. Z)." (vNPU)
- "These findings motivate [next component]." and "The findings from A and B raise a key question: how
  should [decision] be guided through [tradeoff]?" (Lifetime)

**Observation closes with a takeaway**
- "We make N key observations from Fig. M. First, ... Second, ... We conclude that ..." (Constable)
- "Insight #N: [observation]. To achieve [goal], [the system] needs to [requirement]." (DynamoLLM)
- "Takeaway N: With the increase of [variable], [component] should be designed with [consequence]."
  (H2-LLM)
- "Key takeaways: A. ... B. ..." in bold at the end of each case study (PIM Pathfinding)

**Result with its cost**
- "[Name] reduces [A] by X% and Y%, while it increases [B] by Z%." (DynamoLLM)
- "In a few cases (e.g., [workloads]), [feature] may slightly impact [metric]. However, [Name] still
  achieves [result]." (vNPU)
- "As the [load] increases, the savings of [Name] reduce, because [reason]." (DynamoLLM)
- "We note that our [setup] inherently limits [X]: with [Y], [Z]. We expect [W] at [scale]." (MoE patterns)
- "Overall, while [measure] is worse than [baseline], we believe the productivity gain is worth the
  trade-off." (Isaria)

**Scope**
- "Determining which design point is more favorable is not the purpose of this case study. Rather, we
  seek to demonstrate [capability]." (PIM Pathfinding)
- "Domain of [Name]: [scope in one line]." bold run-in at the start of the design (PF-LLM)

## What to avoid, from the same sample

- Priority claims ("the first ...") are frequent in the sample, and some are weakly supported (Fusion-3D
  uses them about five times). In a new paper, state a first only when checked.
- Long parenthetical chains (PIM Pathfinding averages 33 to 36 words per sentence with 280 parentheses)
  hurt readability even in an award paper.
