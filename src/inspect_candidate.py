import json
from pprint import pprint

with open(
    "data/candidates.jsonl",
    "r",
    encoding="utf-8"
) as f:

    first_candidate = json.loads(next(f))

print("\nCandidate ID:\n")
print(first_candidate["candidate_id"])

print("\nFull candidate structure:\n")

pprint(first_candidate)