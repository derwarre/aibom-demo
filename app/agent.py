"""Support triage agent for AcmeSupport AI.

Routes customer tickets to tools, escalates when confidence is low.
"""

from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.tools import tool

from app.guardrails import check_input, check_output
from app.rag import get_retriever

# Primary reasoning model for the triage agent
llm = ChatOpenAI(model="gpt-4o", temperature=0.2)

# Fallback model used when the primary provider is unavailable
fallback_llm_model = "claude-sonnet-4-5"


@tool
def lookup_order(order_id: str) -> str:
    """Look up an order's status by its order id."""
    return f"Order {order_id}: shipped"


@tool
def refund_eligibility(order_id: str) -> str:
    """Check whether an order is eligible for a refund."""
    return f"Order {order_id}: eligible within 30 days"


@tool
def search_kb(query: str) -> str:
    """Search the support knowledge base for relevant articles."""
    docs = get_retriever().invoke(query)
    return "\n".join(d.page_content for d in docs)


def build_agent() -> AgentExecutor:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", open("prompts/system_prompt.txt").read()),
            ("human", "{input}"),
            ("placeholder", "{agent_scratchpad}"),
        ]
    )
    agent = create_tool_calling_agent(llm, [lookup_order, refund_eligibility, search_kb], prompt)
    return AgentExecutor(agent=agent, tools=[lookup_order, refund_eligibility, search_kb])


def run(user_message: str) -> str:
    check_input(user_message)
    result = build_agent().invoke({"input": user_message})
    return check_output(result["output"])
