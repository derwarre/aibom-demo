"""Train the demo ticket classifier and save it as a joblib artifact."""

import json
import pathlib

import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline

root = pathlib.Path(__file__).resolve().parent.parent
rows = [json.loads(line) for line in (root / "data/support_tickets.jsonl").read_text().splitlines()]

pipeline = Pipeline(
    [
        ("tfidf", TfidfVectorizer()),
        ("clf", LogisticRegression(max_iter=1000)),
    ]
)
pipeline.fit([r["text"] for r in rows], [r["label"] for r in rows])

out = root / "models/ticket_classifier.joblib"
joblib.dump(pipeline, out)
print(f"saved {out}")
