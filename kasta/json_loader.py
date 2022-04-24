import json

def load_json(path):
    with open(path) as f:
        data = json.load(f)
    return data

