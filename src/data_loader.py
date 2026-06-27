import json
import gzip
import os

def load_data(file_path: str):
    """
    Loads candidate dataset safely (.jsonl or .jsonl.gz)
    """

    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Dataset not found at: {file_path}")

    data = []

    # gzip file
    if file_path.endswith(".gz"):
        with gzip.open(file_path, "rt", encoding="utf-8") as f:
            for line in f:
                data.append(json.loads(line))

    # jsonl file
    elif file_path.endswith(".jsonl"):
        with open(file_path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    data.append(json.loads(line))

    # json file
    elif file_path.endswith(".json"):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

    else:
        raise ValueError("Unsupported file format")

    print(f"Total candidates loaded: {len(data)}")
    return data