#!/usr/bin/env python3
"""Retrieve source-located architecture writing cards; standard library only."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re


def words(value):
    return set(re.findall(r"[a-z0-9]+", value.lower()))


def select(rows, args):
    query = words(" ".join(filter(None, [args.query, args.move])))
    matches = []
    annotation_root = Path(__file__).resolve().parents[1] / 'data/annotations'
    for row in rows:
        if args.id and row["id"] != args.id:
            continue
        if args.venue and row["venue"].lower() != args.venue.lower():
            continue
        if args.recognition and row["recognition"] != args.recognition:
            continue
        if args.type and row["paper_type"].lower() != args.type.lower():
            continue
        topics = " ".join(row["topics"]).lower()
        if any(topic.lower() not in topics for topic in args.topic):
            continue
        annotation_matches=[]
        if args.function or args.paragraph or args.section:
            source=annotation_root/(row['id']+'.json')
            if not source.exists():continue
            annotation=json.loads(source.read_text())
            for section in annotation['sections']:
                if args.section and section['name']!=args.section:continue
                for paragraph in section['paragraphs']:
                    if args.paragraph and paragraph['role']!=args.paragraph:continue
                    selected=[x for x in paragraph['sentences'] if not args.function or x['primary']==args.function or args.function in x['secondary']]
                    if selected:
                        annotation_matches.append({'section':section['name'],'paragraph_index':paragraph['paragraph_index'],
                          'pdf_page_start':paragraph['pdf_page_start'],'pdf_page_end':paragraph['pdf_page_end'],
                          'paragraph_role':paragraph['role'],'summary':paragraph['summary'],
                          'sentence_indices':[x['sentence_index'] for x in selected],
                          'primary_sequence':[x['primary'] for x in paragraph['sentences']]})
            if not annotation_matches:continue
            row={**row,'annotation_matches':annotation_matches}
        fields = {
            "title": (row["title"], 2),
            "move": (row["writing_move"], 4),
            "topics": (topics, 3),
            "analysis": (row["analysis"], 1),
            "type": (row["paper_type"], 2),
        }
        score = sum(len(query & words(value)) * weight for value, weight in fields.values())
        if query and score == 0:
            continue
        matches.append((score + min(len(annotation_matches), 4), row))
    return [row for _, row in sorted(matches, key=lambda item: (-item[0], item[1]["venue"], -item[1]["year"], item[1]["id"]))[:args.limit]]


def render(row):
    excerpt = row["excerpt"]
    award = row["recognition"].replace("_", " ")
    if row.get("recognition_year"):
        award += f" (recognition year {row['recognition_year']})"
    lines = [f"## {row['title']}", f"{row['venue']} {row['year']} | {award}",
             f"ID: {row['id']} | Type: {row['paper_type']}",
             f"Topics: {', '.join(row['topics'])}", "",
             f"**Writing move:** {row['writing_move']}", "",
             f"> {excerpt['text']}", "",
             f"Source: {row['paper_url']} — PDF p. {excerpt['pdf_page']}, {excerpt['section']}.",
             f"Read scope: {'; '.join(row['sections_read'])}.", "",
             f"**Analysis (curator interpretation):** {row['analysis']}", "",
             f"**Transfer limit:** {row['transfer_caveat']}", "",
             f"**Selection:** {row['selection_reason']}"]
    if row.get('annotation_matches'):
        lines += ['', '**Function-matched paragraph records (original paraphrases, no full source paragraphs):**']
        for item in row['annotation_matches'][:3]:
            lines.append(f"- {item['section']} paragraph {item['paragraph_index']}, PDF pp. {item['pdf_page_start']}-{item['pdf_page_end']}: {item['summary']} Roles: {' -> '.join(item['primary_sequence'])}.")
    if row.get("version_note"):
        lines.append(f"Source version: {row['version_note']}")
    if row.get("recognition_url"):
        lines.append(f"Recognition source: {row['recognition_url']}")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--id", help="Exact readable paper ID; use --list to discover IDs")
    parser.add_argument("--venue", choices=["HPCA", "ASPLOS", "ISCA", "MICRO"], type=str.upper)
    parser.add_argument("--topic", action="append", default=[], help="Topic substring; repeat to require multiple topics")
    parser.add_argument("--recognition", choices=["best_paper", "best_paper_candidate", "test_of_time", "notable"])
    parser.add_argument("--type", help="Contribution type from the corpus index")
    parser.add_argument('--function', choices=['context','problem','prior_work','limitation','observation','insight','mechanism','methodology','result','contribution','scope','roadmap'])
    parser.add_argument('--section', choices=['abstract','introduction'])
    parser.add_argument('--paragraph', choices=['setting','gap','prior_work','insight','approach','evidence','contributions','scope','roadmap','mixed'])
    parser.add_argument("--move", help="Writing-move query, ranked by literal metadata overlap")
    parser.add_argument("--query", default="", help="Free-text query; ranking is retrieval, not a quality score")
    parser.add_argument("--limit", type=int, default=3)
    parser.add_argument("--list", action="store_true", help="Print compact index, without quotes")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    args = parser.parse_args()
    if args.limit < 1:
        parser.error("--limit must be positive")
    corpus = Path(__file__).resolve().parents[1] / "references" / "corpus.json"
    rows = json.loads(corpus.read_text(encoding="utf-8"))
    results = select(rows, args)
    if args.format == "json":
        print(json.dumps(results, indent=2, ensure_ascii=False))
    elif args.list and results:
        for row in results:
            print(f"{row['id']} | {row['venue']} {row['year']} | {row['recognition']} | {row['title']}")
    elif results:
        print("\n\n".join(render(row) for row in results))
    else:
        print("No matching exemplars. Broaden the topic/move query or use --list --limit 100.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
