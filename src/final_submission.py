import json
import csv

from scoring import final_score


def generate_reason(candidate):

    title = candidate["profile"]["current_title"]

    exp = candidate["profile"]["years_of_experience"]

    important_skills = [
        "NLP",
        "Machine Learning",
        "Embeddings",
        "FAISS",
        "Pinecone",
        "Milvus",
        "MLOps",
        "LoRA",
        "Fine-tuning LLMs",
        "Sentence Transformers",
        "Information Retrieval"
    ]

    skill_names = []

    for skill in candidate["skills"]:

        if skill["name"] in important_skills:
            skill_names.append(skill["name"])

    skill_names = skill_names[:5]

    reason = (
        f"{title} with {exp} years experience; "
        f"skills: {', '.join(skill_names)}"
    )

    return reason


# ==========================
# LOAD DATASET
# ==========================

candidates = []

with open("../data/candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:
        candidate = json.loads(line)
        candidates.append(candidate)

print("Total Candidates:", len(candidates))


# ==========================
# CREATE LOOKUP DICTIONARY
# ==========================

candidate_lookup = {}

for candidate in candidates:
    candidate_lookup[candidate["candidate_id"]] = candidate


# ==========================
# SCORE CANDIDATES
# ==========================

results = []

for candidate in candidates:

    score = final_score(candidate)

    results.append(
        (
            candidate["candidate_id"],
            score
        )
    )

print("Scoring Complete")


# ==========================
# SORT CANDIDATES
# ==========================

results.sort(
    key=lambda x: x[1],
    reverse=True
)

print("Sorting Complete")


# ==========================
# TOP 100
# ==========================

top_100 = results[:100]

print("Top 100 Selected")


# ==========================
# DISPLAY TOP 10
# ==========================

print("\nTOP 10 CANDIDATES\n")

for candidate_id, score in top_100[:10]:

    candidate = candidate_lookup[candidate_id]

    print("\n===================")
    print("Candidate ID:", candidate_id)
    print("Score:", score)
    print("Title:", candidate["profile"]["current_title"])
    print("Experience:", candidate["profile"]["years_of_experience"])
    print("Summary:", candidate["profile"]["summary"][:200])


# ==========================
# CREATE SUBMISSION DATA
# ==========================

submission_rows = []

for rank, (candidate_id, score) in enumerate(top_100, start=1):

    candidate = candidate_lookup[candidate_id]

    reasoning = generate_reason(candidate)

    submission_rows.append(
        [
            candidate_id,
            rank,
            round(score / 100, 3),
            reasoning
        ]
    )


# ==========================
# EXPORT CSV
# ==========================

with open(
    "../output/final_submission.csv",
    "w",
    newline="",
    encoding="utf-8"
) as f:

    writer = csv.writer(f)

    writer.writerow(
        [
            "candidate_id",
            "rank",
            "score",
            "reasoning"
        ]
    )

    writer.writerows(submission_rows)

print("\nFinal Submission File Created!")