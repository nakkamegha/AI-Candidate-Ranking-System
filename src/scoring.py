# scoring.py

def experience_score(candidate):

    experience = candidate["profile"]["years_of_experience"]

    if 5 <= experience <= 9:
        return 100

    elif 3 <= experience < 5:
        return 70

    elif 9 < experience <= 12:
        return 70

    else:
        return 30


def skill_score(candidate):

    target_skills = [
        "NLP",
        "Fine-tuning LLMs",
        "LoRA",
        "Milvus",
        "BentoML",
        "Embeddings",
        "Information Retrieval",
        "Sentence Transformers",
        "FAISS",
        "Pinecone",
        "Machine Learning",
        "Hugging Face Transformers",
        "MLOps"
    ]

    score = 0

    for skill in candidate["skills"]:

        if skill["name"] in target_skills:
            score += 10

    return min(score, 100)


def title_score(candidate):

    title = candidate["profile"]["current_title"].lower()

    if "recommendation" in title:
        return 100

    elif "machine learning" in title:
        return 100

    elif "ml engineer" in title:
        return 100

    elif "ai engineer" in title:
        return 100

    elif "nlp" in title:
        return 95

    elif "data scientist" in title:
        return 90

    elif "search engineer" in title:
        return 90

    elif "applied ml" in title:
        return 90

    elif "data engineer" in title:
        return 80

    elif "backend engineer" in title:
        return 70

    elif "software engineer" in title:
        return 70

    elif "cloud engineer" in title:
        return 60

    else:
        return 10


def career_score(candidate):

    important_keywords = [
        "machine learning",
        "ml",
        "ai",
        "llm",
        "ranking",
        "recommendation",
        "search",
        "retrieval",
        "embeddings",
        "transformers",
        "feature pipeline",
        "data science",
        "spark",
        "pyspark",
        "nlp"
    ]

    score = 0

    for job in candidate["career_history"]:

        description = job["description"].lower()

        for keyword in important_keywords:

            if keyword in description:
                score += 10

    return min(score, 100)


def redrob_score(candidate):

    signals = candidate["redrob_signals"]

    score = 0

    if signals["open_to_work_flag"]:
        score += 10

    if signals["recruiter_response_rate"] >= 0.8:
        score += 20

    if signals["profile_completeness_score"] >= 80:
        score += 20

    if signals["saved_by_recruiters_30d"] >= 10:
        score += 20

    if signals["search_appearance_30d"] >= 500:
        score += 20

    if signals["github_activity_score"] >= 50:
        score += 10

    return min(score, 100)

def summary_score(candidate):

    summary = candidate["profile"]["summary"].lower()

    keywords = [
        "machine learning",
        "ml",
        "ai",
        "nlp",
        "recommendation",
        "retrieval",
        "ranking",
        "embedding",
        "embeddings",
        "llm",
        "transformers",
        "search"
    ]

    score = 0

    for keyword in keywords:

        if keyword in summary:
            score += 10

    return min(score, 100)

def education_score(candidate):

    education = candidate["education"]

    score = 0

    for edu in education:

        degree = edu.get("degree", "").lower()

        field = edu.get("field_of_study", "").lower()

        if "m.tech" in degree:
            score += 30

        elif "b.tech" in degree:
            score += 20

        if "computer" in field:
            score += 40

        elif "machine learning" in field:
            score += 50

        elif "artificial intelligence" in field:
            score += 50

    return min(score, 100)

def final_score(candidate):

    exp_score = experience_score(candidate)

    skill_match_score = skill_score(candidate)

    role_score = title_score(candidate)

    career_match_score = career_score(candidate)

    redrob_match_score = redrob_score(candidate)

    summary_match_score = summary_score(candidate)

    education_match_score = education_score(candidate)

    total = (
        0.15 * exp_score +
        0.20 * skill_match_score +
        0.10 * role_score +
        0.20 * career_match_score +
        0.15 * redrob_match_score +
        0.10 * summary_match_score +
        0.10 * education_match_score
    )

    return round(total, 2)


def explain_score(candidate):

    print("\nCandidate:", candidate["candidate_id"])

    print("Title:", candidate["profile"]["current_title"])

    print("Experience Score:", experience_score(candidate))

    print("Skill Score:", skill_score(candidate))

    print("Title Score:", title_score(candidate))

    print("Career Score:", career_score(candidate))

    print("Redrob Score:", redrob_score(candidate))

    print("Final Score:", final_score(candidate))