import json
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity


model=SentenceTransformer(
    "all-MiniLM-L6-v2"
)

JD="""
Senior AI Engineer with 5-9 years experience.
Embeddings, vector databases,
retrieval systems, ranking systems,
Python, ML production deployment.
"""

CORE_SKILLS=[
"Python",
"NLP",
"LoRA",
"Milvus",
"FAISS",
"Embeddings",
"Machine Learning",
"Fine-tuning LLMs",
"Retrieval",
"Ranking"
]


def fast_filter(candidate):

    profile=candidate["profile"]

    skills=[
        s["name"]
        for s in candidate["skills"]
    ]

    experience=profile.get(
        "years_of_experience",0
    )

    matched=sum(
        1
        for skill in CORE_SKILLS
        if skill in skills
    )

    return (
        4<=experience<=10
        and matched>=2
    )


def behavior_score(candidate):

    s=candidate[
        "redrob_signals"
    ]

    score=0

    score+=s.get(
        "github_activity_score",
        0
    )*0.2

    score+=s.get(
        "recruiter_response_rate",
        0
    )*10

    if s.get(
        "open_to_work_flag",
        False
    ):
        score+=10

    if s.get(
        "notice_period_days",
        180
    )<=30:
        score+=5

    return score


def candidate_text(candidate):

    profile=candidate["profile"]

    skills=" ".join([

        s["name"]
        for s in candidate[
            "skills"
        ]

    ])

    return f"""
    {profile.get('current_title','')}
    {profile.get('headline','')}
    {profile.get('summary','')}
    Skills:{skills}
    """


filtered=[]
texts=[]

with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf8"
) as f:

    for line in f:

        c=json.loads(line)

        if fast_filter(c):

            filtered.append(c)

            texts.append(
                candidate_text(c)
            )

candidate_embeddings=model.encode(
    texts,
    batch_size=128
)

jd_embedding=model.encode(
    [JD]
)

similarities=cosine_similarity(
    jd_embedding,
    candidate_embeddings
)[0]

results=[]

for c,sim in zip(
    filtered,
    similarities
):

    score=(
        sim*70
        +behavior_score(c)
    )

    results.append({

        "candidate_id":
        c["candidate_id"],

        "score":
        round(score,3),

        "reasoning":
        f"""
        Strong semantic match with AI retrieval role,
        suitable experience and behavioral signals
        """
    })

df=pd.DataFrame(
    results
)

df=df.sort_values(
    by=["score","candidate_id"],
    ascending=[False,True]
)

top100=df.head(100)

top100["rank"]=range(
    1,
    101
)

top100=top100[
[
"candidate_id",
"rank",
"score",
"reasoning"
]
]

top100.to_csv(
"outputs/submission.csv",
index=False
)

print(
"Submission file created"
)