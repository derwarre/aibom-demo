"""FastAPI entrypoint for AcmeSupport AI."""

from fastapi import FastAPI
from pydantic import BaseModel

from app.agent import run

app = FastAPI(title="AcmeSupport AI", version="1.0.0")


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
def chat(req: ChatRequest) -> dict:
    return {"reply": run(req.message)}


@app.get("/healthz")
def healthz() -> dict:
    return {"status": "ok"}
