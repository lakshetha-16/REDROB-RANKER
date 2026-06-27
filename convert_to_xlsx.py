import pandas as pd

# 1. Load your ranked output CSV
df = pd.read_csv("outputs/submission.csv")

# 2. Sort by score (highest first)
df = df.sort_values("score", ascending=False)

# 3. Add rank column
df["rank"] = range(1, len(df) + 1)

# 4. Keep only top candidates (change number if needed)
top_df = df.head(50)   # or 10 / 100 based on requirement

# 5. Save as XLSX
top_df.to_excel("outputs/ranked_candidates.xlsx", index=False)

print("XLSX file created successfully!")