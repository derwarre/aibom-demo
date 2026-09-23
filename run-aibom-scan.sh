#!/usr/bin/env bash
# Scan the demo AI container and (optionally) upload the AI BOM to Cisco AI Defense.
#
# Usage:
#   ./run-aibom-scan.sh                       # scan only, writes aibom-report.json + aibom-dashboard.html
#   AI_DEFENSE_API_KEY=... ./run-aibom-scan.sh   # scan + upload to AI Defense (US region)
#
# Optional LLM enrichment (better classification, fewer false positives):
#   OPENAI_API_KEY=...    LLM_MODEL=gpt-5.4        ./run-aibom-scan.sh
#   ANTHROPIC_API_KEY=... LLM_MODEL=claude-opus-5  ./run-aibom-scan.sh
set -euo pipefail
export PATH="$HOME/.docker/bin:$HOME/.local/bin:$PATH"

IMAGE="acmesupport-ai:1.0.0"
POST_URL="${AIBOM_POST_URL:-https://api.security.cisco.com/api/ai-defense/v1/aibom/analysis}"

ARGS=()
if [[ -n "${LLM_MODEL:-}" ]]; then
  ARGS+=(--llm-model "$LLM_MODEL" --llm-api-key "${OPENAI_API_KEY:-${ANTHROPIC_API_KEY:?set OPENAI_API_KEY or ANTHROPIC_API_KEY when LLM_MODEL is set}}")
fi
if [[ -n "${AI_DEFENSE_API_KEY:-}" ]]; then
  ARGS+=(--post-url "$POST_URL" --ai-defense-api-key "$AI_DEFENSE_API_KEY")
fi

cisco-aibom analyze "$IMAGE" --output-format json --output-file aibom-report.json "${ARGS[@]}"
cisco-aibom analyze "$IMAGE" --output-format html --output-file aibom-dashboard.html "${ARGS[@]:0:${#ARGS[@]}}" || true

echo
echo "Report:    $(pwd)/aibom-report.json"
echo "Dashboard: $(pwd)/aibom-dashboard.html"
[[ -n "${AI_DEFENSE_API_KEY:-}" ]] && echo "Uploaded to AI Defense ($POST_URL)"
