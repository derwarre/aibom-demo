FROM python:3.12-slim

LABEL org.opencontainers.image.title="AcmeSupport AI" \
      org.opencontainers.image.description="Demo AI customer-support service for Cisco AI Defense AI BOM scanning" \
      org.opencontainers.image.version="1.0.0"

WORKDIR /srv/acmesupport

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY app/ app/
COPY config/ config/
COPY prompts/ prompts/
COPY guardrails/ guardrails/
COPY mcp/ mcp/
COPY data/ data/
COPY models/ models/

ENV PYTHONUNBUFFERED=1

EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
