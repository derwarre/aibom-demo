# aibom: concept=guardrail framework=internal
"""Input/output guardrails for the support agent.

Blocks prompt-injection markers on input and PII leakage on output.
Policy thresholds live in guardrails/config.yaml.
"""

import re

INJECTION_PATTERNS = [
    r"ignore (all )?(previous|prior) instructions",
    r"you are now",
    r"system prompt",
]

PII_PATTERNS = [
    r"\b\d{3}-\d{2}-\d{4}\b",          # SSN
    r"\b(?:\d[ -]*?){13,16}\b",        # card number
]


class GuardrailViolation(Exception):
    pass


def check_input(text: str) -> None:
    for pattern in INJECTION_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            raise GuardrailViolation("prompt-injection pattern detected")


def check_output(text: str) -> str:
    for pattern in PII_PATTERNS:
        text = re.sub(pattern, "[REDACTED]", text)
    return text
