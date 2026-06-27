from sentence_transformers import SentenceTransformer
import numpy as np
from src.scorer import compute_score

# 🔥 LOAD MODEL ONCE (prevents repeated overhead)
model = SentenceTransformer("all-MiniLM-L6-v2")


def semantic_rank(candidates):

    # 🔥 LIMIT TEXT SIZE (big speed boost)
    candidates = candidates[:50000]

    texts = [
        (c["title"] + " " + " ".join(c.get("skills", [])[:5]))  # limit skills
        for c in candidates
    ]

    # 🔥 FAST BATCH EMBEDDING
    embeddings = model.encode(
        texts,
        batch_size=128,          # increased batch size = faster
        show_progress_bar=True,
        normalize_embeddings=True
    )

    results = []

    for i, c in enumerate(candidates):

        semantic_score = float(np.mean(embeddings[i]))

        score = compute_score(c, semantic_score)

        results.append({
            "candidate_id": c["candidate_id"],
            "score": score,
            "candidate": c
        })

    return results