import numpy as np


def compute_score(candidate, semantic_score=0.0):

    # -----------------------------
    # EXPERIENCE SCORE (log scaling)
    # -----------------------------
    exp = candidate.get("experience", 0)
    exp_score = np.log1p(exp) * 10  # smooth scaling

    # -----------------------------
    # SKILL SCORE
    # -----------------------------
    skills = candidate.get("skills", [])
    skill_score = min(len(skills), 20) * 2.0

    # -----------------------------
    # SIGNAL SCORE (normalized)
    # -----------------------------
    github = candidate.get("github_score", 0) * 2
    response = candidate.get("response_rate", 0) * 25
    notice = 10 if candidate.get("notice_period", 999) <= 30 else 0

    open_to_work = 5 if candidate.get("open_to_work") else 0

    signal_score = github + response + notice + open_to_work

    # -----------------------------
    # FINAL HYBRID SCORE (IMPORTANT)
    # -----------------------------
    final_score = (
        semantic_score * 0.45 +
        exp_score * 0.2 +
        skill_score * 0.2 +
        signal_score * 0.15
    )

    return float(final_score)