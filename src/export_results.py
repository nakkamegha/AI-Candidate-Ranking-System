import json
import csv

from scoring import final_score

with open("../data/sample_candidates.json", "r") as f:
    data = json.load(f)

results = []

for candidate in data:

    score = final_score(candidate)

    results.append([
        candidate["candidate_id"],
        candidate["profile"]["current_title"],
        score
    ])

# SORT RESULTS FROM HIGHEST SCORE TO LOWEST SCORE
results.sort(key=lambda x: x[2], reverse=True)

with open("../output/ranked_candidates.csv", "w", newline="") as f:

    writer = csv.writer(f)

    writer.writerow([
        "Candidate ID",
        "Title",
        "Final Score"
    ])

    writer.writerows(results)

print("CSV file created successfully!")