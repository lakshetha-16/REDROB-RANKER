import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="AI Candidate Ranker",
    layout="wide"
)

st.title("🧠 AI Candidate Ranking System")

st.write("""
This system ranks candidates using:
- Semantic embeddings
- Cross-encoder reranking
- Behavioral signals
""")

df = pd.read_csv("outputs/submission.csv")

# Sidebar filters
st.sidebar.header("Filters")

min_score = st.sidebar.slider(
    "Minimum Score",
    float(df["score"].min()),
    float(df["score"].max()),
    float(df["score"].min())
)

filtered_df = df[df["score"] >= min_score]

st.subheader("Top Candidates")

st.dataframe(
    filtered_df.head(100),
    use_container_width=True
)

st.subheader("Top 10 Candidates Only")

st.table(
    filtered_df.head(10)
)