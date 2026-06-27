import csv
import os


def generate_submission(ranked_candidates):
    os.makedirs("outputs", exist_ok=True)

    path = "outputs/submission.csv"

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)

        writer.writerow(["candidate_id", "rank", "score", "reasoning"])

        for i, c in enumerate(ranked_candidates, 1):
            writer.writerow([
                c["candidate_id"],
                i,
                c["score"],
                "Hybrid ranking using semantic + behavioral + skill signals"
            ])

    print("Submission generated at:", path)