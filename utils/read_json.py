import json

def get_data():
    with open("./data/case_data.json", "r", encoding="utf-8") as f:
        return json.load(f)
