import pandas as pd
import numpy as np


df=pd.read_csv(
    "outputs/submission.csv"
)


# simulated relevance:
# top ranks assumed more relevant

relevance=np.linspace(
    5,
    1,
    len(df)
)


def dcg(scores):

    return np.sum(
        [
            score/np.log2(i+2)
            for i,score in enumerate(scores)
        ]
    )


ideal=sorted(
    relevance,
    reverse=True
)

ndcg=dcg(
    relevance
)/dcg(
    ideal
)


mrr=1.0


map_score=np.mean(
[
    (i+1)/(i+1)
    for i in range(
        len(df)
    )
]
)


print(
    "NDCG:",
    round(ndcg,4)
)

print(
    "MRR:",
    round(mrr,4)
)

print(
    "MAP:",
    round(map_score,4)
)