"""
RoBacTutor dataset cleaning pass.

Produces a corrected copy of the SFT dataset:
1. Strips the fabricated "baremul oficial ANCE <year>" citation from every
   response field (same pattern as clean_barem_text() in the backend, but
   applied at the source this time, not just at display-time).
2. Surfaces duplication candidates (as before, via find_duplication_candidates)
   for YOU to manually confirm/reject -- this script does not auto-fix
   duplication, since that requires human judgement (see dataset_quality_audit.py
   notes on why automated fixing here is unreliable).
3. Writes a change log: exactly which records were modified and how, so this
   cleaning pass is itself documentable/citable in the dissertation.

Usage:
    python clean_dataset.py path/to/robactutor_sft_dataset_reviewed.jsonl

Outputs (written next to the input file):
    robactutor_sft_dataset_cleaned.jsonl   -- citation-stripped dataset
    cleaning_changelog.md                  -- what was changed, and the
                                               duplication candidates for
                                               manual review
"""

import json
import re
import sys
import difflib
from pathlib import Path


def clean_citation(response_text: str) -> tuple:
    """Returns (cleaned_text, was_changed)."""
    cleaned = re.sub(
        r"\*?Not[ăa]:\s*Acest r[ăa]spuns este bazat pe baremul oficial ANCE\s*\d{4}\.?\*?",
        "", response_text, flags=re.IGNORECASE,
    ).strip()
    return cleaned, (cleaned != response_text.strip())


def find_duplication_candidates(text: str, window: int = 5, max_gap: int = 12,
                                 threshold: float = 0.55) -> list:
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
    return hits[:1]


def main(path: str) -> None:
    input_path = Path(path)
    output_path = input_path.parent / "robactutor_sft_dataset_cleaned.jsonl"
    changelog_path = input_path.parent / "cleaning_changelog.md"

    records = []
    with open(input_path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                records.append(json.loads(line))

    citation_changes = []
    duplication_candidates = []

    for i, item in enumerate(records):
        cleaned, changed = clean_citation(item["response"])
        if changed:
            citation_changes.append({
                "index": i,
                "subject": item["metadata"]["subject"],
                "instruction_preview": item["instruction"][:70],
            })
            item["response"] = cleaned

        dup_hits = find_duplication_candidates(item["response"])
        if dup_hits:
            span_a, span_b, ratio = dup_hits[0]
            duplication_candidates.append({
                "index": i,
                "subject": item["metadata"]["subject"],
                "instruction_preview": item["instruction"][:70],
                "ratio": ratio,
                "span_a": span_a,
                "span_b": span_b,
                "full_response": item["response"],
            })

    with open(output_path, "w", encoding="utf-8") as f:
        for item in records:
            f.write(json.dumps(item, ensure_ascii=False) + "\n")

    duplication_candidates.sort(key=lambda c: -c["ratio"])

    with open(changelog_path, "w", encoding="utf-8") as f:
        f.write("# RoBacTutor Dataset Cleaning Changelog\n\n")
        f.write(f"Input: `{input_path.name}` ({len(records)} records)\n")
        f.write(f"Output: `{output_path.name}`\n\n")
        f.write("## Citation removal\n\n")
        f.write(f"{len(citation_changes)} of {len(records)} records "
                f"({len(citation_changes)/len(records):.1%}) contained the fabricated "
                f"\"baremul oficial ANCE <year>\" citation; it was stripped in each.\n\n")
        by_subject = {}
        for c in citation_changes:
            by_subject.setdefault(c["subject"], 0)
            by_subject[c["subject"]] += 1
        for subj, count in sorted(by_subject.items()):
            f.write(f"- {subj}: {count}\n")

        f.write("\n## Duplication candidates -- MANUAL REVIEW REQUIRED\n\n")
        f.write(f"{len(duplication_candidates)} records flagged as possible "
                f"duplicated/spliced text (NOT auto-fixed -- see dataset_quality_audit.py "
                f"notes on why this can't be done reliably). Read each and decide:\n\n")
        for c in duplication_candidates:
            f.write(f"### Record {c['index']} ({c['subject']}) -- match ratio {c['ratio']:.2f}\n")
            f.write(f"Instruction: \"{c['instruction_preview']}...\"\n\n")
            f.write(f"Span A: `{c['span_a']}`\n\n")
            f.write(f"Span B: `{c['span_b']}`\n\n")
            f.write(f"Full response: {c['full_response'][:300]}...\n\n")
            f.write("**Verdict (fill in): [ ] Real duplication -- needs fixing  "
                    "[ ] False positive (legitimate structure) -- no action\n\n")
            f.write("---\n\n")

    print(f"Cleaned dataset written: {output_path}")
    print(f"Changelog written: {changelog_path}")
    print(f"\nCitation fixes: {len(citation_changes)} / {len(records)} records")
    print(f"Duplication candidates for manual review: {len(duplication_candidates)}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python clean_dataset.py path/to/dataset.jsonl")
        sys.exit(1)
    main(sys.argv[1])
