"""MCP server exposing support-desk tools to AI assistants."""

from mcp.server.fastmcp import FastMCP

mcp = FastMCP("acme-support-desk")


@mcp.tool()
def get_ticket(ticket_id: str) -> str:
    """Fetch a support ticket by id."""
    return f"Ticket {ticket_id}: open, priority=medium"


@mcp.tool()
def classify_ticket(text: str) -> str:
    """Classify a ticket's intent using the local ticket classifier model."""
    import joblib

    model = joblib.load("models/ticket_classifier.joblib")
    return str(model.predict([text])[0])


@mcp.resource("kb://articles/{article_id}")
def kb_article(article_id: str) -> str:
    """Serve a knowledge-base article."""
    return f"Article {article_id}"


if __name__ == "__main__":
    mcp.run(transport="stdio")
