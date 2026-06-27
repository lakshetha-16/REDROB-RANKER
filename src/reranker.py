from sentence_transformers import CrossEncoder
import pandas as pd
import json

model = CrossEncoder(
    "cross-encoder/ms-marco-MiniLM-L-6-v2"
)

JD="""
Senior AI Engineer with 5-9 years experience.
Embeddings, vector databases,
retrieval systems, ranking systems,
Python, ML production deployment
"""


CORE_SKILLS=[
"Python",
"NLP",
"LoRA",
"Milvus",
"FAISS",
"Machine Learning",
"Fine-tuning LLMs"
]


def fast_filter(candidate):

    skills=[
        s["name"]
        for s in candidate["skills"]
    ]

    exp=candidate["profile"].get(
        "years_of_experience",
        0
    )

    matches=sum(
        1
        for x in CORE_SKILLS
        if x in skills
    )

    return (
        4<=exp<=10
        and matches>=2
    )


def candidate_text(candidate):

    profile=candidate["profile"]

    skills=" ".join([
        s["name"]
        for s in candidate["skills"]
    ])

    return f"""
    {profile.get("current_title","")}
    {profile.get("headline","")}
    {profile.get("summary","")}
    Skills:{skills}
    """


filtered=[]

with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:

        c=json.loads(line)

        if fast_filter(c):

            filtered.append(c)


print(
    "Candidates after filtering:",
    len(filtered)
)


pairs=[]

for c in filtered:

    pairs.append(
        [
            JD,
            candidate_text(c)
        ]
    )


print(
    "Running reranker..."
)

scores=model.predict(
    pairs,
    batch_size=64
)


results=[]

for c,score in zip(
    filtered,
    scores
):

    results.append({

        "candidate_id":
        c["candidate_id"],

        "title":
        c["profile"][
            "current_title"
        ],

        "score":
        round(
            float(score),
            3
        )

    })


df=pd.DataFrame(
    results
)

df=df.sort_values(
    by=["score","candidate_id"],
    ascending=[False,True]
)

print(
    df.head(10)
)