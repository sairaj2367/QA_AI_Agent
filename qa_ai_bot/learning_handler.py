import os
import json
from datetime import datetime

LEARNING_DIR = 'learned_data'


def save_learning(query, response):
    if not os.path.exists(LEARNING_DIR):
        os.makedirs(LEARNING_DIR)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"learning_{timestamp}.json"
    filepath = os.path.join(LEARNING_DIR, filename)

    data = {
        "query": query,
        "response": response,
        "timestamp": timestamp
    }

    with open(filepath, 'w') as file:
        json.dump(data, file, indent=4)


def get_recent_learnings(limit=5):
    if not os.path.exists(LEARNING_DIR):
        return []

    files = sorted(os.listdir(LEARNING_DIR), reverse=True)[:limit]
    learnings = []

    for file in files:
        with open(os.path.join(LEARNING_DIR, file), 'r') as f:
            learnings.append(json.load(f))

    return learnings