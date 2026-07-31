"""
RoBacTutor hybrid-grading calibration test.

Runs 5 answers -- spanning non-attempt, nonsense, wrong-but-plausible,
honest-partial, and fully-correct-but-reworded -- against the SAME question,
so you can see whether the hybrid similarity score actually discriminates
between them or just reacts to surface text overlap.

Usage:
    1. Set BASE_URL below to your running backend (e.g. http://localhost:8000)
    2. Set QUESTION_ID to the binomial-coefficient item's id (grab it from
       your browser's Network tab -- the question_id field in the most
       recent /practice/start or /practice/grade request)
    3. python calibration_test.py
"""

import requests

BASE_URL = "http://127.0.0.1:8000"  # adjust to your actual backend URL
QUESTION_ID = "q156"                # binomial-coefficient item (C(9,6)=84), line 156 of the dataset JSONL

ANSWERS = {
    "1. non-attempt": "Nu știu.",
    "2. nonsense-numeric (known: 2.2/8, 27.5%)": "67 2/3",
    "3. WRONG final answer, correct method (real test)": (
        "2^(n-1) = 256, deci n = 9. Termenul general este "
        "T(k+1) = C(9,k)·x^((9-k)/3-k/2). Am pus exponentul egal cu -2 și am "
        "rezolvat ecuația, obținând k = 6. Coeficientul este C(9,6) = 504."
    ),
    "4. partial, honestly incomplete": (
        "2^(n-1) = 256, deci 2^(n-1) = 2^8, deci n = 9. Termenul general este "
        "T(k+1) = C(9,k)·x^((9-k)/3-k/2). Nu am reușit să rezolv ecuația "
        "pentru k, deci nu am calculat coeficientul final."
    ),
    "5. fully correct, heavily reworded": (
        "Din condiția dată rezultă că 2 la puterea (n-1) este egal cu 256, "
        "adică 2 la puterea 8, deci n este 9. Termenul de rang k+1 din "
        "dezvoltare are forma combinării de 9 luate câte k, înmulțită cu x "
        "la puterea (9 minus k) supra 3, minus k supra 2. Punând acest "
        "exponent egal cu -2, obținem k egal cu 6. Coeficientul cerut este "
        "combinarea de 9 luate câte 6, adică 84."
    ),
}


def main():
    if QUESTION_ID == "REPLACE_ME":
        print("Set QUESTION_ID first -- grab it from your browser's Network tab.")
        return

    print(f"{'Answer':55s} {'Punctaj':>10s} {'Similaritate':>13s}")
    print("-" * 80)
    for label, answer in ANSWERS.items():
        resp = requests.post(
            f"{BASE_URL}/api/practice/grade",
            json={"session_id": "calibration-test", "question_id": QUESTION_ID, "student_answer": answer},
        )
        resp.raise_for_status()
        data = resp.json()
        print(f"{label:55s} {data['punctaj_estimat']:>6.1f}/{data['punctaj_total']:<3d} {data['similaritate']:>12.1%}")

    print("\nWhat to check:")
    print("- Does #3 (wrong final answer) score suspiciously close to #5 (fully correct)?")
    print("  If so, the hybrid score is rewarding 'looks like the barem' over 'is actually right'.")
    print("- Does #4 (honest partial) land clearly between #1/#2 and #5?")
    print("- Does #5 (correct but reworded) still score high despite different phrasing/notation?")
    print("  If not, the score may be penalizing legitimate alternative phrasing.")


if __name__ == "__main__":
    main()
