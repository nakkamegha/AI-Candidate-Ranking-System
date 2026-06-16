# AI Candidate Ranking System

A hybrid rule-based candidate ranking system that evaluates 100,000 candidate profiles and recommends the top 100 candidates for AI/ML roles using experience, skills, career history, education, and recruiter engagement signals.

## Problem Statement

Recruiters often struggle to identify the best candidates from a large talent pool. This project builds an AI-inspired candidate ranking system that evaluates candidate profiles and recommends the top candidates for AI/ML-related roles.

The system processes candidate profiles, scores them across multiple dimensions, ranks them, and produces the top 100 recommendations.

## Dataset

The project uses:

- candidates.jsonl (100,000 candidate profiles)
- sample_candidates.json (sample dataset for testing)
- candidate_schema.json
- job description document
- Redrob signals document

Each candidate contains:

- Profile information
- Skills
- Career history
- Education
- Certifications
- Languages
- Redrob signals

## Project Structure

IndiaRunsProject/

data/
- candidates.jsonl
- sample_candidates.json
- candidate_schema.json

src/
- explore.py
- scoring.py
- test_score.py
- ranking.py
- export_results.py
- final_submission.py

output/
- ranked_candidates.csv
- final_submission.csv

README.md

## Approach

The solution uses a Hybrid Rule-Based Ranking System.

Each candidate is evaluated using:

1. Experience Score
2. Skill Match Score
3. Current Title Score
4. Career History Score
5. Redrob Signal Score
6. Summary Relevance Score
7. Education Score

These scores are combined using weighted scoring to produce a final ranking score.

## Scoring Formula

Final Score =

0.15 × Experience Score

+ 0.20 × Skill Score

+ 0.10 × Title Score

+ 0.20 × Career Score

+ 0.15 × Redrob Score

+ 0.10 × Summary Score

+ 0.10 × Education Score

## Workflow

1. Load candidate dataset
2. Calculate candidate scores
3. Rank candidates
4. Select Top 100 candidates
5. Generate reasoning
6. Export final submission CSV

## Running The Project

### Explore Data

```bash
python explore.py
```

### Test Scoring

```bash
python test_score.py
```

### Rank Sample Candidates

```bash
python ranking.py
```

### Export Sample Results

```bash
python export_results.py
```

### Generate Final Submission

```bash
python final_submission.py
```

## Output

The final output file contains:

- candidate_id
- rank
- score
- reasoning

Generated file:

```text
output/final_submission.csv
```

## Future Improvements

- Semantic Search
- Vector Embeddings
- Sentence Transformers
- LLM-based Ranking
- Hybrid Retrieval and Ranking Pipeline

## Author

Nakka Sai Meghana