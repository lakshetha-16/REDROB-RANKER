import streamlit as st
import pandas as pd

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_excel("outputs/final_ranked_candidates_v2.xlsx")

st.set_page_config(page_title="Candidate Ranking Dashboard", layout="wide")

st.title("🏆 AI Candidate Ranking Dashboard")

# -----------------------------
# SEARCH BOX
# -----------------------------
search_id = st.text_input("🔎 Search Candidate ID")

if search_id:
    result = df[df["candidate_id"].astype(str).str.contains(search_id, case=False)]
    st.subheader("Search Result")
    st.dataframe(result)

# -----------------------------
# TOP 10 TABLE
# -----------------------------
st.subheader("📊 Top 10 Candidates")

top10 = df.head(10)
st.dataframe(top10, use_container_width=True)

# -----------------------------
# GRAPH (TOP 10 SCORES)
# -----------------------------
st.subheader("📈 Top 10 Score Visualization")

chart_data = top10[["candidate_id", "final_score"]].set_index("candidate_id")
st.bar_chart(chart_data)

# -----------------------------
# DOWNLOAD BUTTON
# -----------------------------
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇️ Download Full Ranking CSV",
    data=csv,
    file_name="final_ranked_candidates.csv",
    mime="text/csv"
)

# -----------------------------
# FOOTER
# -----------------------------
st.success("Dashboard loaded successfully 🚀")