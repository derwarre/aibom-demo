"""Application settings.

NOTE: All credentials below are intentionally fake demo values planted so
that AI BOM secret scanning has something to find. They are not real keys.
"""

import os

OPENAI_API_KEY = os.getenv(
    "OPENAI_API_KEY",
    "sk-proj-DEMO0000000000000000000000000000000000000000000",
)
ANTHROPIC_API_KEY = "sk-ant-api03-DEMO00000000000000000000000000000000000000000000"

# AWS docs' canonical example credential pair (not a real secret)
AWS_ACCESS_KEY_ID = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_ACCESS_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

HUGGINGFACE_TOKEN = "hf_DEMO000000000000000000000000000000"

PRIMARY_MODEL = "gpt-4o"
FALLBACK_MODEL = "claude-sonnet-4-5"
EMBEDDING_MODEL = "text-embedding-3-small"
CLASSIFIER_PATH = "models/ticket_classifier.joblib"
