# Model Card: ticket_classifier

- **Artifact:** `models/ticket_classifier.joblib`
- **Type:** scikit-learn Pipeline (TfidfVectorizer + LogisticRegression)
- **Task:** classify incoming support tickets into `shipping` / `refund` / `troubleshooting`
- **Training data:** `data/support_tickets.jsonl` (demo dataset, 12 rows)
- **Intended use:** demo asset for AI BOM scanning; not a production model
- **Metrics:** trained to convergence on the full demo set; no held-out evaluation
