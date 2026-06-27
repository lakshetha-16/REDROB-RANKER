from src.semantic_ranker import rank_candidates


def compute_final_score(candidate, semantic_score):
    profile = candidate["profile"]
    signals = candidate["redrob_signals"]

    # Experience
    exp = profile.get("years_of_experience", 0)
    exp_score = min(exp / 10, 1.0)

    # Skills
    skills = candidate.get("skills", [])
    skill_score = min(len(skills) / 15, 1.0)

    # GitHub
    github = signals.get("github_activity_score", 0)
    github_score = 0 if github == -1 else github / 100

    # Behavior
    response_rate = signals.get("recruiter_response_rate", 0)
    interview_rate = signals.get("interview_completion_rate", 0)
    behavior_score = (response_rate + interview_rate) / 2

    # Availability
    open_to_work = 1.0 if signals.get("open_to_work_flag") else 0.0

    final_score = (
        0.40 * semantic_score +
        0.20 * exp_score +
        0.15 * skill_score +
        0.10 * github_score +
        0.10 * behavior_score +
        0.05 * open_to_work
    )

    return round(final_score * 100, 4)


def rank_all(candidates, job_text):
    semantic_scores = rank_candidates(candidates, job_text)

    results = []

    for c, s in zip(candidates, semantic_scores):
        final = compute_final_score(c, s)

        results.append({
            "candidate_id": c["candidate_id"],
            "score": final
        })

    results = sorted(results, key=lambda x: x["score"], reverse=True)

    return results