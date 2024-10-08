import chromadb
import chromadb.utils.embedding_functions as embedding_functions
import uuid
from utils.apiKey import APIKey

class DBClient:
    def __init__(self, DBName):
        self.__DBName = DBName
        self.__client = chromadb.PersistentClient(f"./data/chromadb/{DBName}")
        self.__collection = self.__client.create_collection(
            name=DBName,
            embedding_function=embedding_functions.OpenAIEmbeddingFunction(
                api_key=APIKey.get_key(),
                model_name="text-embedding-3-small"
            ),
            metadata={"hnsw:space": "cosine"},
            get_or_create=True
        )

    def DBAdd(self, chunk, docID=None):
        if docID is None:
            guid = uuid.uuid4()
            docID = str(guid)

        self.__collection.add(
            documents=[chunk],
            metadatas=[{"Doc Name": self.__DBName}],
            ids=[docID]
        )
        return

    def DBQuery(self, query, n_results):
        queries = self.__collection.query(
            query_texts=[query],
            include=["documents", "metadatas"],
            n_results=n_results
        )
        return queries['documents'][0][0]

    def DBUpdate():
        return
    def DBDelete():
        return