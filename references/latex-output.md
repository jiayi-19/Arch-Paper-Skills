# LaTeX output and delivery

Use the existing official conference template when supplied. `prepare_paper.py
--template DIR --out NEW_DIR` makes an independent copy, omitting Git metadata and
caches and refusing an existing destination or source symlinks. It does not invent
an official conference style or edit the original. If no template is requested,
produce Markdown or section fragments rather than an approximately compliant kit.

Keep the requested outline, macros, section labels, bibliography and author choices.
Replace sample text only within the intended work. Verify current venue/year rules
when changing format; preserve anonymity, paper size, review mode and actual submission
number. Add citation keys only after checking the real paper and bibliography entry.

Integrate actual-data plots and diagram/table fragments. Escape literal %, &, _, #
and use the project's existing math/reference macros. Draft result gaps stay visible.
Source checks: `check_manuscript.py`, `check_draft.py`, `check_figures.py`. Compile/render
only when authorized and appropriate to the user's workflow; no rendering is needed
for the helper checks. Report what was actually checked rather than calling uncompiled
source layout-verified. Private report/annotation material stays outside submission text.
