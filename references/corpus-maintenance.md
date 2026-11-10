# Maintaining the exemplar corpus

## Inclusion and recognition

Select papers from HPCA, ASPLOS, ISCA and MICRO for useful argument patterns and topic
breadth. Separate best paper, formally listed candidate/nominee, Test of Time or named
influential-paper award, and notable-by-curation. Record the original paper year and
the recognition year separately. Record the exact award name in the selection reason.
A frequently cited paper is not an award winner unless the source says so.

Use an official conference, society or award page for recognition and an author,
institution, publisher or archival original-paper source for the passage. If sources
conflict, retain the ambiguity or replace the entry; do not resolve it by familiarity.
If a paper is selected as notable, explain its writing value and use a primary source
for its venue and identity. An award page alone does not prove what the paper says.

## Reading and extraction

Read the actual abstract/introduction and the method/evaluation material used in the
analysis. Record sections read honestly. Prefer one short verbatim excerpt per paper
with a one-based PDF page and section locator, then explain its rhetorical function
in original prose. Count quotations across all included excerpts from the same paper;
keep the installed corpus under a conservative 25-word total per paper. Shortened
quotes still need to match contiguous text; mark ellipses and their omission explicitly.

Store full PDFs and temporary text extraction outside the installed skill in the
host's designated scratch/storage locations. The skill ships small excerpts, metadata,
source URLs and analytical cards, not a redistributed paper library.

The analysis should explain what information precedes/follows the excerpt, what
technical mechanism the passage exposes, the evidence sequence inspected, which
writing request benefits from it, and a limit on transferring the move. Treat the
analysis as a curator's interpretation, not a quoted author or award-committee claim.

## Data contract

`references/corpus.json` is the machine-readable source of truth. Each row has:

- Readable `id`, exact `title`, `venue`, publication `year`.
- `recognition`, `recognition_year`, `recognition_url`, and `selection_reason`.
- `paper_url`, verified `doi` if available, topic tags and contribution type.
- `sections_read` documenting actual reading scope.
- `excerpt`: `text`, one-based `pdf_page`, and `section`.
- `writing_move`, original `analysis`, and `transfer_caveat`.

The index `references/corpus.md` and cards rendered by the finder disclose the reading
scope and use these records. Store each exact quote once in the JSON source of truth. The finder ranks literal metadata matches; its ranking is a retrieval
aid, not a quality score. Do not copy the source excerpt into a new manuscript or
assume any paper result applies to the user's experiment.

## Rechecking and scope

When adding papers, verify both the passage and award sources; preserve author names,
DOIs and venue identity accurately. Prefer readable versions and source URLs. The
corpus is a purposefully selected set, with selection bias toward accessible and
recognizable papers. No controlled inference about all award papers, conference
culture, statistical writing style or acceptance probability follows from it.
