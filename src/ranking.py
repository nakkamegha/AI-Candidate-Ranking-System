import json

from scoring import final_score

with open("../data/sample_candidates.json", "r") as f:
    data = json.load(f)

results = []

for candidate in data:

    score = final_score(candidate)

    results.append(
        (
            candidate["candidate_id"],
            candidate["profile"]["current_title"],
            score
        )
    )

results.sort(key=lambda x: x[2], reverse=True)

print("\nTOP 10 CANDIDATES\n")

for candidate in results[:10]:
    print(candidate)