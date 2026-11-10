#!/usr/bin/env python3
"""Shared transparent prose measurements; lexical proxies, not writing-quality scores."""
from __future__ import annotations
import math
import re
import unicodedata

CONNECTORS = ('however','therefore','thus','moreover','furthermore','nevertheless','consequently','in contrast','as a result')
HEDGES = ('may','might','could','likely','possibly','potentially','suggests','suggest')
BOOSTERS = ('significant','significantly','substantial','substantially','dramatic','dramatically','novel','efficient','effective','outperforms')
ABBREVIATIONS = ('e.g.','i.e.','et al.','Fig.','Figs.','Sec.','Secs.','Eq.','Eqs.','Dr.','vs.','etc.')
WORD = re.compile(r"[A-Za-z]+(?:['’\-][A-Za-z]+)*|\d+(?:[.,]\d+)*(?:[%×]|x\b)?")
NUMBER = re.compile(r'(?<![A-Za-z\d])\d+(?:[.,]\d+)*(?:[%×]|x\b)?')


def plain(text):
    text = unicodedata.normalize('NFKC', text)
    text = re.sub(r'\\(?:cite\w*|ref|cref|Cref|eqref|label)\*?(?:\[[^\]]*\])*\{[^{}]*\}', '', text)
    text = re.sub(r'\\(?:section|subsection|paragraph|title)\*?\{[^{}]*\}', '', text)
    text = re.sub(r'\\(?:begin|end)\{[^{}]*\}', '', text)
    text = re.sub(r'\\(?:textbf|textit|emph|textrm|textsf)\{([^{}]*)\}', r'\1', text)
    text = re.sub(r'\\[A-Za-z]+\*?', ' ', text)
    text = re.sub(r'\[\d+(?:\s*[,–-]\s*\d+)*\]', '', text)
    return text.replace('{','').replace('}','').strip()


def sentences(text):
    """Draft-only boundary heuristic; corpus boundaries are inspected annotations."""
    text = plain(text)
    replacements = {}
    for index, abbreviation in enumerate(ABBREVIATIONS):
        token = f'ABBREV{index}TOKEN'
        replacements[token] = abbreviation
        text = re.sub(re.escape(abbreviation), token, text, flags=re.I)
    text = re.sub(r'(?<=\d)\.(?=\d)', 'DECIMALTOKEN', text)
    parts = re.split(r'(?<=[.!?])\s+(?=[A-Z0-9“"\\])|\n\s*\n', text)
    output = []
    for part in parts:
        for token, abbreviation in replacements.items():
            part = part.replace(token, abbreviation)
        part = part.replace('DECIMALTOKEN','.')
        if WORD.search(part): output.append(part.strip())
    return output


def count_phrases(text, phrases):
    return sum(len(re.findall(r'\b'+re.escape(term)+r'\b', text, flags=re.I)) for term in phrases)


def measure(text, annotated_sentences=None):
    clean = plain(text)
    sents = annotated_sentences if annotated_sentences is not None else sentences(text)
    lengths = [len(WORD.findall(plain(s))) for s in sents]
    count = len(WORD.findall(clean))
    total = lambda n: 100*n/count if count else 0.0
    trailing = sum(bool(re.search(r',\s*(?:making|enabling|allowing|providing|yielding|leading|resulting|demonstrating)\b',s,re.I)) for s in sents)
    passive = len(re.findall(r'\b(?:is|are|was|were|be|been)\s+(?:\w+ly\s+)?[A-Za-z]+(?:ed|en)\b',clean,re.I))
    return {'word_count':count,'sentence_count':len(sents),
      'mean_sentence_words':sum(lengths)/len(lengths) if lengths else 0.0,
      'number_tokens':len(NUMBER.findall(clean)), 'numbers_per_100_words':total(len(NUMBER.findall(clean))),
      'connectors_per_100_words':total(count_phrases(clean,CONNECTORS)),
      'hedges_per_100_words':total(count_phrases(clean,HEDGES)),
      'boosters_per_100_words':total(count_phrases(clean,BOOSTERS)),
      'trailing_participial_sentences_pct':100*trailing/len(sents) if sents else 0.0,
      'em_dashes_per_100_words':total(clean.count('—')+clean.count('---')),
      'passive_proxy_per_100_words':total(passive)}


def quantile(values, q):
    ordered=sorted(values)
    if not ordered:return None
    position=(len(ordered)-1)*q
    lo=math.floor(position);hi=math.ceil(position)
    return ordered[lo]+(ordered[hi]-ordered[lo])*(position-lo)


def distribution(values):
    return {'n':len(values),'min':min(values) if values else None,
            'p10':quantile(values,.1),'p50':quantile(values,.5),
            'p90':quantile(values,.9),'max':max(values) if values else None}
