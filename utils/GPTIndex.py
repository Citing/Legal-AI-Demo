from llama_index.core import Document
from llama_index.core.indices.vector_store.base import VectorStoreIndex
from llama_index.embeddings.openai import OpenAIEmbedding
from dotenv import load_dotenv

load_dotenv()

openai_embedding = OpenAIEmbedding(model="text-embedding-ada-002")

def createGPTIndex(chunks):
    documents = [Document(text=chunk) for chunk in chunks]
    index = VectorStoreIndex(documents, embed_model=openai_embedding)
    return index

def queryLlama(index, userQuestion):
    query_engine = index.as_query_engine()
    return query_engine.query(userQuestion).source_nodes