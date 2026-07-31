"""
RoBacTutor dataset quality audit.

Two separate data-quality issues found by inspection (see dissertation Ch5):

1. FABRICATED CITATIONS -- reliably countable. response fields containing
   "Nota: Acest raspuns este bazat pe baremul oficial ANCE <year>." ANCE is
   not a real cited authority for this content; this appears to be an
   artifact from how the dataset's responses were originally generated.
   This count is a hard number: the regex match is unambiguous.

2. DUPLICATED/SPLICED TEXT -- NOT reliably countable by string similarity
   alone, and this script does not pretend otherwise. Example real artifact:
   "Integreaza critic informatiile din Integreaza critic(4p.) sursele
   propuse..." -- two phrasings of the same criterion spliced together.
   The problem: genuine official barems ALSO legitimately repeat structure
   on purpose (e.g. "Se acorda 4 puncte... Se acorda 3 puncte... Se acorda
   2 puncte...", a normal tiered-scoring pattern). A fuzzy-match threshold
   loose enough to catch real splicing artifacts is also loose enough to
   flag that completely normal pattern as if it were corruption -- tested
   directly against both cases, no threshold cleanly separates them.
   So: this script surfaces CANDIDATES sorted by match strength for a human
   to read and judge, it does NOT report a confirmed count. Do not cite the
   candidate count in the dissertation as if it were a measured error rate --
   cite the number of candidates a human actually confirmed after review.

Usage:
    python dataset_quality_audit.py path/to/robactutor_sft_dataset_reviewed.jsonl
"""

import difflib
import json
import re
import sys
from collections import defaultdict


def has_fabricated_citation(text: str) -> bool:
    return bool(re.search(r"ANCE\s*\d{4}", text, flags=re.IGNORECASE))


def find_duplication_candidates(text: str, window: int = 5, max_gap: int = 12,
                                 threshold: float = 0.55) -> list[tuple[str, str, float]]:
    """Returns candidate (span_a, span_b, ratio) tuples where a nearby
    word-span pair looks similar. This is a SCREENING heuristic for manual
    review, not a validated detector -- see module docstring."""
    words = re.findall(r"\S+", text)
    n = len(words)
    hits = []
    for i in range(n - window + 1):
        span_a = " ".join(words[i:i + window])
        for j in range(i + window, min(i + window + max_gap, n - window + 1)):
            span_b = " ".join(words[j:j + window])
            ratio = difflib.SequenceMatcher(None, span_a.lower(), span_b.lower()).ratio()
            if ratio >= threshold:
                hits.append((span_a, span_b, ratio))
    hits.sort(key=lambda h: -h[2])
    return hits[:1]  # strongest match only, per text


def main(path: str) -> None:
    total = 0
    citation_count = 0
    candidates = []  # (instruction, response, subject, ratio, span_a, span_b)
    by_subject = defaultdict(lambda: {"total": 0, "citation": 0})

    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            item = json.loads(line)
            response = item["response"]
            subject = item["metadata"]["subject"]

            total += 1
            by_subject[subject]["total"] += 1

            if has_fabricated_citation(response):
                citation_count += 1
                by_subject[subject]["citation"] += 1

            dup_hits = find_duplication_candidates(response)
            if dup_hits:
                span_a, span_b, ratio = dup_hits[0]
                candidates.append((item["instruction"][:70], response, subject, ratio, span_a, span_b))

    candidates.sort(key=lambda c: -c[3])

    print("=" * 70)
    print("RoBacTutor dataset quality audit")
    print("=" * 70)
    print(f"Total pairs: {total}\n")

    print("--- RELIABLE: fabricated citation ('ANCE <year>') ---")
    print(f"{citation_count} / {total} ({citation_count / total:.1%})")
    print("By subject:")
    for subject, counts in sorted(by_subject.items()):
        t = counts["total"]
        print(f"  {subject:20s} {counts['citation']:3d} / {t:3d} ({counts['citation'] / t:.1%})")

    print(f"\n--- NOT reliable, needs manual review: {len(candidates)} duplication candidates ---")
    print("(sorted strongest match first -- read these yourself, don't cite this count directly)\n")
    for instr, response, subject, ratio, span_a, span_b in candidates[:15]:
        print(f"[{subject}] \"{instr}...\"  (match ratio {ratio:.2f})")
        print(f"   span A: {span_a!r}")
        print(f"   span B: {span_b!r}")
        print(f"   full response: {response[:250]}...")
        print()

    if len(candidates) > 15:
        print(f"...and {len(candidates) - 15} more candidates below the top 15 shown.")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "robactutor_sft_dataset_reviewed.jsonl"
    main(path)

