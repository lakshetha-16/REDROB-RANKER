import pandas as pd
import os

df = pd.read_csv("data/sample_submission.csv")

df = df.loc[:, ~df.columns.duplicated()]

clean_df = pd.DataFrame({
    "candidate_id": df.iloc[:, 0],
    "rank": df.iloc[:, 1],
    "final_score": df.iloc[:, 2]
})

clean_df["final_score"] = pd.to_numeric(clean_df["final_score"], errors="coerce")
clean_df = clean_df.sort_values("final_score", ascending=False).reset_index(drop=True)
clean_df["rank"] = range(1, len(clean_df) + 1)

# ✅ FIX: ensure folder exists
os.makedirs("outputs", exist_ok=True)

output_path = "outputs/final_ranked_candidates.xlsx"

# If file is locked, change name automatically
if os.path.exists(output_path):
    output_path = "outputs/final_ranked_candidates_v2.xlsx"

clean_df.to_excel(output_path, index=False)

print("DONE ✅ Saved at:", output_path)