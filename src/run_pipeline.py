from src.data_loader import load_data
from src.preprocess import preprocess
from src.semantic_ranker import semantic_rank
import pandas as pd
import os
os.environ["TOKENIZERS_PARALLELISM"] = "false"

def build_reasoning(c):

    reasons = []

    if c.get("experience", 0) >= 5:
        reasons.append("strong experience")

    if len(c.get("skills", [])) > 10:
        reasons.append("diverse skill set")

    if c.get("github_score", 0) > 5:
        reasons.append("active GitHub profile")

    if c.get("open_to_work"):
        reasons.append("open to work")

    return ", ".join(reasons) if reasons else "balanced profile"


def main():

    print("Loading data...")
    candidates = load_data("data/candidates.jsonl")

    print("Preprocessing...")
    processed = preprocess(candidates[:50000])  # 🔥 hard limit for speed

    print("Ranking...")
    ranked = semantic_rank(processed)

    df = pd.DataFrame([
        {
            "candidate_id": r["candidate_id"],
            "score": r["score"],
            "candidate": r["candidate"]
        }
        for r in ranked
    ])

    # IMPORTANT SORTING RULE
    df = df.sort_values(
        by=["score", "candidate_id"],
        ascending=[False, True]
    ).reset_index(drop=True)

    # TOP 100 ONLY
    df = df.head(100)

    # RANK
    df["rank"] = range(1, len(df) + 1)

    # REAL REASONING
    df["reasoning"] = df["candidate"].apply(build_reasoning)

    # FINAL FORMAT
    df = df[["candidate_id", "rank", "score", "reasoning"]]

    df.to_csv("outputs/submission.csv", index=False)

    print("Submission created ✔")


if __name__ == "__main__":
    main()