#!/usr/bin/env python3
"""Check literal LaTeX source links, citations, labels, and draft markers.

This is a source heuristic, not a TeX interpreter or scientific evidence audit.
No compilation, code execution, rendering, or network access occurs.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


def visible_source(text):
    text = re.sub(r"\\begin\{(verbatim\*?|lstlisting|minted)\}.*?\\end\{\1\}", "", text, flags=re.S)
    text = re.sub(r"\\verb\*?(\W).*?\1", "", text)
    lines = []
    for line in text.splitlines():
        for index, char in enumerate(line):
            if char == "%":
                slashes = len(line[:index]) - len(line[:index].rstrip("\\"))
                if slashes % 2 == 0:
                    line = line[:index]
                    break
        lines.append(line)
    return "\n".join(lines)


def inspect(main, root):
    errors, warnings, texts = [], [], {}
    visiting = set()

    def issue(target, path, text, match, message):
        target.append({"file": str(path), "line": text.count("\n", 0, match.start()) + 1, "message": message})

    def dynamic(value):
        return "\\" in value or "#" in value or not value.strip()

    def visit(path):
        path = path.resolve()
        if not path.is_relative_to(root):
            warnings.append({"file": str(path), "message": "Outside --root; not read. Broaden --root if this source is intentional."})
            return
        if path in visiting:
            errors.append({"file": str(path), "message": "Recursive input/include cycle"})
            return
        if path in texts:
            warnings.append({"file": str(path), "message": "Source included more than once; inspect repeated labels/content manually"})
            return
        if not path.is_file():
            errors.append({"file": str(path), "message": "Missing literal LaTeX source"})
            return
        text = visible_source(path.read_text(encoding="utf-8"))
        texts[path] = text
        visiting.add(path)
        for match in re.finditer(r"\\(?:input|include)\s*\{([^{}]*)\}", text):
            name = match.group(1).strip()
            if dynamic(name):
                issue(warnings, path, text, match, "Macro-generated source path is unverified: " + name)
                continue
            target = root / name
            if not target.suffix:
                target = target.with_suffix(".tex")
            visit(target)
        for match in re.finditer(r"\\(?:input|include)\b(?!\s*\{)", text):
            issue(warnings, path, text, match, "Unbraced input/include syntax requires manual inspection")
        visiting.remove(path)

    visit(main)
    bibkeys, labels, citations, references = set(), {}, [], []
    bibfiles = set()
    for path, text in texts.items():
        for match in re.finditer(r"\\(?:bibliography|addbibresource)(?:\s*\[[^\]]*\])?\s*\{([^{}]*)\}", text):
            for name in match.group(1).split(","):
                name = name.strip()
                if dynamic(name):
                    issue(warnings, path, text, match, "Macro-generated bibliography path is unverified: " + name)
                    continue
                bib = root / name
                if not bib.suffix:
                    bib = bib.with_suffix(".bib")
                bib = bib.resolve()
                if not bib.is_relative_to(root):
                    issue(warnings, path, text, match, "Bibliography outside --root is unverified: " + str(bib))
                elif not bib.is_file():
                    issue(errors, path, text, match, "Missing bibliography: " + str(bib))
                else:
                    bibfiles.add(bib)
                    content = visible_source(bib.read_text(encoding="utf-8"))
                    bibkeys.update(re.findall(r"@(?!(?:comment|string|preamble)\b)[A-Za-z]+\s*[\{(]\s*([^\s,{}()]+)\s*,", content, flags=re.I))
        for match in re.finditer(r"\\bibitem(?:\s*\[[^\]]*\])?\s*\{([^{}]+)\}", text):
            bibkeys.add(match.group(1))
        for match in re.finditer(r"\\label\s*\{([^{}]+)\}", text):
            name = match.group(1)
            if dynamic(name):
                issue(warnings, path, text, match, "Macro-generated label is unverified: " + name)
            elif name in labels:
                issue(errors, path, text, match, "Duplicate label: " + name)
            else:
                labels[name] = str(path)
        citation_pattern = r"\\(?:cite|citep|citet|citealp|citealt|citeauthor|citeyear|parencite|textcite|autocite|nocite)\*?(?:\s*\[[^\]]*\]){0,2}\s*\{([^{}]*)\}"
        for match in re.finditer(citation_pattern, text):
            citations.append((path, text, match))
        for match in re.finditer(r"\\(?:ref|eqref|cref|Cref|autoref|pageref|vref|Vref)\*?\s*\{([^{}]+)\}", text):
            references.append((path, text, match))
        for match in re.finditer(r"\b(?:TODO|TBD|PLACEHOLDER)\b|\\(?:todo|draftnote|figplaceholder)\b", text, flags=re.I):
            issue(warnings, path, text, match, "Draft marker remains: " + match.group(0))
        for match in re.finditer(r"\\begin\{thebibliography\}", text):
            issue(warnings, path, text, match, "Manual bibliography: check full entries and author lists")
    for entries, known, kind in ((citations, bibkeys, "citation"), (references, labels, "reference")):
        for path, text, match in entries:
            for key in match.group(1).split(","):
                key = key.strip()
                if kind == "citation" and key == "*":
                    continue
                if dynamic(key):
                    issue(warnings, path, text, match, f"Macro-generated {kind} is unverified: " + key)
                elif key not in known:
                    issue(errors, path, text, match, f"Unresolved {kind}: " + key)
    return {"scope": "Literal-source heuristic only; verify macro expansion, scientific claims and bibliography correctness manually.",
            "files": [str(path) for path in texts], "bibliographies": [str(path) for path in sorted(bibfiles)],
            "errors": errors, "warnings": warnings}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("main", type=Path, help="Main .tex file; never executed")
    parser.add_argument("--root", type=Path, help="Source root used to resolve literal paths; defaults to main's directory")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    args = parser.parse_args()
    main_path = args.main.resolve()
    root = (args.root or main_path.parent).resolve()
    result = inspect(main_path, root)
    if args.format == "json":
        print(json.dumps(result, indent=2, ensure_ascii=False))
    else:
        print(result["scope"])
        for category in ("errors", "warnings"):
            for row in result[category]:
                location = row["file"] + (f":{row['line']}" if "line" in row else "")
                print(f"{category[:-1].upper()} {location}: {row['message']}")
        print(f"Checked {len(result['files'])} TeX files and {len(result['bibliographies'])} bibliographies; "
              f"{len(result['errors'])} errors, {len(result['warnings'])} warnings.")
    return 1 if result["errors"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
