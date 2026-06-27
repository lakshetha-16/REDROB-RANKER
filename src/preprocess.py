def preprocess(candidates):
    processed = []

    for c in candidates:

        profile = c.get("profile", {})
        signals = c.get("redrob_signals", {})

        skills = c.get("skills", [])
        skill_names = []

        for s in skills:
            if isinstance(s, dict):
                skill_names.append(s.get("name", "").replace(" ", ""))
            else:
                skill_names.append(str(s).replace(" ", ""))

        processed.append({
            "candidate_id": c.get("candidate_id"),
            "title": profile.get("current_title", ""),
            "experience": profile.get("years_of_experience", 0),
            "skills": skill_names,
            "github_score": signals.get("github_activity_score", 0),
            "response_rate": signals.get("recruiter_response_rate", 0),
            "open_to_work": signals.get("open_to_work_flag", False),
            "notice_period": signals.get("notice_period_days", 999)
        })

    return processed