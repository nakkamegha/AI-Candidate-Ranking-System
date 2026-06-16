import json

# Load dataset
with open("../data/sample_candidates.json", "r") as f:
    data = json.load(f)

# Basic dataset information
print("=== DATASET INFO ===")
print("Type:", type(data))
print("Number of candidates:", len(data))

# First candidate
candidate = data[30]

print("\n=== CANDIDATE KEYS ===")
print(candidate.keys())

print("\n=== CANDIDATE ID ===")
print(candidate["candidate_id"])

print("\n=== PROFILE ===")
print(candidate["profile"])

print("\n=== SKILLS ===")
print(candidate["skills"])

print("\n=== CAREER HISTORY ===")
print(candidate["career_history"])

print("\n=== SKILL NAMES ===")
for skill in candidate["skills"]:
    print(skill["name"])

print("\n=== FIRST JOB ===")
print(candidate["career_history"][0])

print("\n=== JOB TITLES ===")

for job in candidate["career_history"]:
    print(job["title"])
    
print("\n=== EDUCATION ===")
print(candidate["education"])

print("\n=== CERTIFICATIONS ===")
print(candidate["certifications"])

print("\n=== JOB DESCRIPTIONS ===")

for job in candidate["career_history"]:
    print("\nJOB:", job["title"])
    print(job["description"])

print("\n=== REDROB SIGNALS ===")
print(candidate["redrob_signals"])

print("\n=== PROFILE DETAILS ===")
print("Name:", candidate["profile"]["anonymized_name"])
print("Title:", candidate["profile"]["current_title"])
print("Experience:", candidate["profile"]["years_of_experience"])
print("Company:", candidate["profile"]["current_company"])
print("Location:", candidate["profile"]["location"])

print("\n=== DATA TYPES ===")
print("Candidate:", type(candidate))
print("Profile:", type(candidate["profile"]))
print("Skills:", type(candidate["skills"]))
print("Career History:", type(candidate["career_history"]))
print("Education:", type(candidate["education"]))
print("Redrob Signals:", type(candidate["redrob_signals"]))
