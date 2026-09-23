"""RAG pipeline: Chroma vector store over the support knowledge base."""

from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

# Embedding model for knowledge-base retrieval
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

_vector_store = None


def get_vector_store() -> Chroma:
    global _vector_store
    if _vector_store is None:
        _vector_store = Chroma(
            collection_name="support_kb",
            embedding_function=embeddings,
            persist_directory="/data/chroma",
        )
    return _vector_store


def get_retriever():
    return get_vector_store().as_retriever(search_kwargs={"k": 4})
