import json
import pandas as pd


AI_SKILLS=[

    "Python",
    "NLP",
    "LoRA",
    "Milvus",
    "FAISS",
    "Vector Database",
    "Embeddings",
    "Fine-tuning LLMs",
    "Machine Learning",
    "Ranking",
    "Retrieval"
]


def score_candidate(candidate):

    profile=candidate["profile"]
    signals=candidate["redrob_signals"]
    skills=candidate["skills"]

    score=0

    experience=profile.get(
        "years_of_experience",0
    )

    if 5<=experience<=9:
        score+=20


    candidate_skills=[
        s["name"]
        for s in skills
    ]

    matched=0

    for skill in AI_SKILLS:
        if skill in candidate_skills:
            matched+=1

    score+=matched*5

    github=signals.get(
        "github_activity_score",0
    )

    score+=github*0.2

    response=signals.get(
        "recruiter_response_rate",0
    )

    score+=response*10

    if signals.get(
        "open_to_work_flag",False
    ):
        score+=10

    return round(score,2)



results=[]


with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    for line in f:

        candidate=json.loads(line)

        score=score_candidate(candidate)

        results.append({

            "candidate_id":
            candidate["candidate_id"],

            "title":
            candidate["profile"]["current_title"],

            "experience":
            candidate["profile"]["years_of_experience"],

            "score":
            score
        })



df=pd.DataFrame(results)

df=df.sort_values(
    by="score",
    ascending=False
)

print(df.head(10))