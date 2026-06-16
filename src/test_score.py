import json

from scoring import *

with open("../data/sample_candidates.json", "r") as f:
    data = json.load(f)

candidate = data[30]

explain_score(candidate)