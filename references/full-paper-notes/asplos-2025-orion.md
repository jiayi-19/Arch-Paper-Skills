# asplos-2025-orion: Orion: A Fully Homomorphic Encryption Framework for Deep Learning

Word counts below come from pdftotext output with figure, table and listing text mixed in, so section sizes are approximate (plus or minus 15 percent). Sentence and paragraph statistics are from prose paragraphs only.

### 0. Identity
- Title: Orion: A Fully Homomorphic Encryption Framework for Deep Learning
- Venue and year: ASPLOS 2025 (Rotterdam), Volume 2. Award: Best Paper.
- Contribution type: framework and compiler (automation): a PyTorch-to-FHE system with two new algorithms (a packing strategy and a bootstrap placement method) and an API.
- Pages: 16 (including references). Authors: Austin Ebel, Karthik Garimella, Brandon Reagen (NYU).
- Full text used: https://arxiv.org/abs/2311.03470 (PDF v3, 12 Feb 2025).

### 1. Skeleton
| Section | Words (approx.) | Figs / tables | Role |
|---|---|---|---|
| Abstract | 236 | 0 | |
| 1 Introduction | 1000 | 0 | setting, challenges, solutions, contributions |
| 2 CKKS Background | 1500 | 1 fig, 1 table | background (datatypes, encoding, encryption, RNS, operations) |
| 3 FHE Matrix-Vector Products | 700 | 1 fig | background on prior techniques (diagonal method, BSGS, hoisting) |
| 4 Efficient Convolutions in Orion | 1500 | 3 figs | design 1 (packing) |
| 5 Automatic Bootstrap Placement | 1500 | 1 fig | design 2 (bootstrap placement and level policy) |
| 6 The Orion Framework | 900 | 1 listing, 1 fig | design 3 (API, range estimation, scale management, data handling) |
| 7 Methodology | 500 | 0 | methodology |
| 8 Evaluation | 1800 | 4 tables, 1 fig | evaluation (8.1 to 8.6) |
| 9 Related Works | 400 | 0 | related work |
| 10 Conclusion | 170 | 0 | conclusion with future work |

No separate motivation, overview or discussion section, and no appendix.

### 2. Abstract
- 12 sentences, about 236 words. Average 19 words.
- Functions in order: (1) setting, FHE can improve privacy; (2) setting, strongest for deep learning services in the cloud; (3) problem, beyond cost, mapping networks onto FHE primitives is the main obstacle; (4) list of programming challenges (packing, noise, instruction set); (5) gap, large FHE networks are intractable with today's tools; (6) approach, Orion named here, a fully automated framework; (7) what it does, takes PyTorch networks and emits FHE programs; (8) mechanism, single-shot multiplexed packing plus automatic bootstrap placement and scale management; (9) result, 2.38x over state of the art on ResNet-20, "the largest network they report"; (10) scope, techniques allow deeper and larger networks; (11) demonstration, ResNet-50 on ImageNet and the first high-resolution FHE object detection with a 139 million parameter YOLO-v1; (12) open-source link.
- Five of twelve sentences pose the problem before the system is named. The one comparison number has its scope in the sentence itself (baseline, network, and the qualifier that ResNet-20 is the largest network the baseline reports).

### 3. Introduction
- 9 prose paragraphs plus 4 contribution items; about 1000 words (no figure). Three paragraphs open with bold run-in challenge labels.
- P1: FHE definition and setting; opens with "Fully Homomorphic Encryption (FHE) is a powerful encryption scheme". Ends with deep learning services as the target.
- P2: problem and prior work: wide deployment is limited by cost and by the difficulty of translating ordinary networks into FHE programs; accelerators and compilers are credited; the gap is running large-dataset FHE inference from a high-level framework such as PyTorch. Last sentence moves to "multiple compounding factors".
- P3 (bold "Vector packing:"), P4 ("Bootstrap placement:"), P5 ("Programmability:"): one challenge each, each explaining why it is hard and what it costs; labeled, about 100 words each.
- P6: "To address these challenges, we develop and open-source Orion", advancing all three areas. Describes the packing method as an improvement in three numbered ways over the prior best (i, ii, iii), with the rotation reduction up to 6.41x.
- P7: "We then present a fully-automated and efficient solution for placing bootstrap operations", shortest paths in a DAG, matches the state of the art in bootstrap count while 8x to 1270x faster; further numbers in parentheses (1.94 s and 11.0 s on ResNet-20 and ResNet-110; 351 versus 8480 bootstraps for ResNet-50; 37 versus 58 for ResNet-20).
- P8: "Finally, we design Orion to be accessible to machine learning researchers"; PyTorch inheritance; the largest FHE inference to date (YOLO-v1).
- P9: "We evaluate Orion ... report significant improvements" then "We make the following contributions:".
- Contribution list (4): 1 the framework (artifact and capability, 2.38x over the prior best on ResNet-20); 2 single-shot multiplexed packing (mechanism, depth one); 3 automatic bootstrap placement (mechanism, with a number: matches the bootstrap count of the prior best and runs up to 1270x faster); 4 first high-resolution object detection with a 139 million parameter model (result and capability). Three of four carry a number.
- The three challenge paragraphs (P3 to P5) map to the three solution paragraphs (P6 to P8) ("advances the state-of-the-art in all three areas"). Results are attached to each solution paragraph, so there is no separate results-preview paragraph. The key packing insight (a convolution is a matrix-vector product in diagonal form) is not in the introduction; it first appears in Sec 4.1. Prior work is credited as a group (P2), then named and compared against in numbers (P6, P7).
- Challenges device: three bold run-in labels with colon.

### 4. Motivation and background
- No motivation section. The problem is argued in the introduction, and the difficulty of bootstrap placement in Sec 5.1 ("Problem Overview") through three stated reasons plus an analytical argument that minimizing the bootstrap count increases latency.
- Evidence: Fig 1 (measured latency of key operations versus ciphertext level), which also fixes a design parameter, and analytic complexity statements. Two background sections cover CKKS (about 2200 words in total with Sec 3) before the first contribution in Sec 4.
- Observations end with explicit labels in the text: "Takeaway:" (end of Sec 3.3), "Orion:" (Sec 4.1 start of own contribution), "The core idea:" (Sec 5.2). The mapping from problem to design is by section (packing in Sec 4, bootstrap in Sec 5, usability in Sec 6).

### 5. Overview of the design
- No Overview section and no system architecture figure. The introduction's three-challenge, three-solution structure is the overview. Sections 4, 5 and 6 each open with one paragraph (e.g., "In this section, we show how Orion efficiently expresses all convolutions as matrix-vector products ...") and 5 adds "We begin by ... Then ... We close with ...".
- Sec 6 ("The Orion Framework") gives the user's view: a Listing 1 ResNet block in PyTorch style next to the idea that Orion inherits from PyTorch modules. This works as the system overview, but it comes late, after the algorithms.

### 6. Design sections
- Subsection pattern for packing: start from the prior method (Gazelle), "Orion:" marker followed by the observation that it equals the diagonal method, a toy 3x3 example worked through (Figs 3 to 5, same symbols a to i), generalization to multiple channels and to strides, then cost and benefit (rotations 1457 to 836 on ResNet-20; Table 3).
- Bootstrap placement pattern: the problem in a small feed-forward example (Fig 6a to 6b), then a harder case with a skip connection (Fig 6c to 6d), then bold run-in blocks "Placement constraint:", "Cost model:", "The core idea:", "A general strategy:", "Implementation details:". Complexity is argued in the evaluation (8.5), not in Sec 5.
- Names stay stable: single-shot multiplexing, level digraph, level management policy, SESE region, errorless evaluation.
- Left out: cryptographic details of hoisting and polynomial evaluation (cited), code links (in Table 2).
- Figure types: matrices with colored cells for toy examples, directed graph, code listing, line plots of operation latency versus level.

### 7. Evaluation
- Organized by benchmark (MNIST, CIFAR-10, Tiny ImageNet, ImageNet), then bootstrap placement scalability (8.5), then a case study (8.6). Within CIFAR-10, bold run-in labels "Packing comparisons", "Performance comparisons", "Choice of activation function".
- First result: MNIST, with a headline comparison (0.23 s against 19.0 s for the prior best, about 83x, helped by a smaller ring degree).
- Claims bounded: everything is single-threaded, run on the same GCP instance as the baselines which were rerun by the authors; outputs validated against cleartext PyTorch (all 10,000 images for MNIST, samples for CIFAR-10 and Tiny ImageNet, one inference for ImageNet).
- Ablation by decomposition: Table 4 splits the 2.38x over Fhelipe into rotations (1.71x), bootstraps (1.58x), and convolution time (11.2x), then explains why convolution time improves far more than rotation count (hoisting, precomputed plaintexts). Table 3 compares packing strategies by rotation counts only.
- Negative or weak results are stated in plain words: the 17.5-hour object detection run is "still far from practical"; SiLU trades 2.1 percent accuracy for a 1.77x speedup; ImageNet has one encrypted inference per network; a direct runtime comparison with HeLayers is unavailable, so the comparison uses bootstrap counts.

### 8. Sentence and paragraph habits
- Average sentence about 22 words (counted 22.2); prose paragraphs about 170 words (median 138). "We" about 22 per 1k words (the highest of the four).
- Bold run-in labels in almost every section ("Orion:", "Takeaway:", "Validation:", "Benchmarks:"). Inline enumeration with (i), (ii), (iii) and First/Second.
- About 7 semicolons and essentially no em or en dashes (3 en dashes in the whole text), about 17 parentheses per 1k words, often used for paired numbers ("1.94 (11.0) seconds ... ResNet-20 (ResNet-110)"). Hedging is low. "Notably," 7 times, "Thus," 8 times, "Therefore," 6 times.
- Eight patterns:
  1. "While [hardware accelerators] have addressed [A] and [compilers] have made progress in [B], it remains a challenge to [target capability]."
  2. "Besides the computational costs, multiple compounding factors make effectively [doing X] challenging."
  3. "[Bold label]: [why it is hard, in two or three sentences]. [Consequence]."
  4. "To address these challenges, we develop and open-source [NAME]: a fully-automated framework for [task] that advances the state-of-the-art in all three areas."
  5. "Our observation here is that prior works' [X] is equivalent to [Y]."
  6. "This approach directly improves upon [prior] in three ways: (i) ..., (ii) ..., (iii) ...."
  7. "Takeaway: [method] has two fundamental benefits: (i) ... and (ii) ...."
  8. "Notably, despite having only [small factor] fewer [counts], our [metric] is [large factor] faster, which occurs for two reasons. First, ... Second, ..."

### 9. Figures and tables
- First figure (Fig 1, in Sec 2.4): measured latency of three key operations (plaintext multiply, rotation, bootstrap) versus ciphertext level. It comes first because it explains why level management matters, and its caption states the design decision (the chosen effective level and why).
- Carrying the argument: Fig 3 (the prior packing method and Orion's matrix form on the same example) and Fig 6 (level digraph).
- Tables: Table 2 is a master table, one row per model and activation, with parameters, FLOPS, code link, parameter set, rotations, depth, bootstraps, clear and FHE accuracy, precision bits, time. Tables 3 and 4 end with an "Improvement" row of ratios.
- Captions: descriptive, some stating the point ("Strided convolutions produce Toeplitz matrices with many sparse non-zero diagonals (a). Orion automatically converts these ...").

### 10. Why it reads as strong, and what does not transfer
1. Three bold-labeled challenges in the introduction (P3 to P5) answered by three solution paragraphs (P6 to P8), each already carrying its own number, then by Sections 4, 5, 6 and by evaluation subsections. The reader can verify the introduction's promises one by one.
2. The "Orion:" and "Takeaway:" run-in markers (Sec 3.3, 4.1, 5.2) separate what is borrowed from what is new inside sections that are mostly prior work, so credit and contribution never blur.
3. Results are decomposed rather than just claimed (Table 4, Sec 8.2): the overall factor is split into rotations, bootstraps and convolution time, with a reason for each.
- Not to copy: the long CKKS tutorial before the first contribution (about 2200 words), notation tables, a single-threaded-only caveat that fits crypto but not a design paper.

Quotations used (section): "it remains a challenge to run FHE neural inference on large datasets in a high-level deep learning framework" (1); "Besides the computational costs, multiple compounding factors make effectively mapping neural networks to FHE challenging." (1); "a fully-automated framework for private neural inference that advances the state-of-the-art in all three areas" (1); "Takeaway: The double-hoisting BSGS method has two fundamental benefits" (3.3); "Our observation here is that prior works' packed SISO method is equivalent to the diagonal method" (4.1); "While this is still far from practical" (8.6).
