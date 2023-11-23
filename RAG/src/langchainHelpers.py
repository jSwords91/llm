from typing import List, Optional, Any
from langchain.vectorstores import Chroma
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader


#loader = DirectoryLoader('./new_articles/', glob="./*.txt", loader_cls=TextLoader)

class PdfLoad:
    def __init__(self, filepath: str) -> None:
        self.filepath = filepath
        self.loader = PyPDFLoader(self.filepath)
        self.documents = self.loader.load()

    def characterSplitter(self, chunk_size: int = 1000, chunk_overlap: int = 200):
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
        return text_splitter.split_documents(self.documents)

class ChromaDB:
    def __init__(self, persist_directory: str, embedding: Any) -> None:
        self.persist_directory = persist_directory
        self.embedding = embedding

    def initiate(self, texts: List, persist: bool = True) -> Any:
        """
        Initiates the embedding process and optionally persists the data.
        """
        try:
            vectordb = Chroma.from_documents(
                documents=texts,
                embedding=self.embedding,
                persist_directory=self.persist_directory,
            )

            if persist:
                vectordb.persist()

            return vectordb

        except Exception as e:
            raise RuntimeError(f"Error during db creation: {e}")

    def load(self):
        try:
            return Chroma(
            persist_directory=self.persist_directory, embedding_function=self.embedding
        )

        except Exception as e:
            raise RuntimeError(f"Error during db loading: {e}")

class ChromaRetriever:
    def __init__(self, vectorDb: Any, k: int = 3) -> None:
        self.k = k
        self.retriever = vectorDb.as_retriever(search_kwargs={"k": self.k})

    def get_relevant_documents(self, query: str) -> List:
        return self.retriever.get_relevant_documents(query)