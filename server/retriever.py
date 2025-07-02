from dotenv import load_dotenv
import os
from langchain_chroma import Chroma
from langchain_upstage import UpstageEmbeddings
from chromadb.config import Settings

load_dotenv()
api_key = os.getenv("UPSTAGE_API_KEY")

embedding = UpstageEmbeddings(
    model="embedding-query",
    api_key=api_key
)

topic_to_dir = {
    "patient": "./chroma_db/chroma_patient_db",
    "allergy": "./chroma_db/chroma_allergies",
    "medications": "./chroma_db/chroma_medications",
    "conditions": "./chroma_db/chroma_conditions_db",
    "observations": "./chroma_db/observation_chroma_db",
}

def multi_retrieve(query, k=5):
    all_results = {}
    for topic, path in topic_to_dir.items():
        vs = Chroma(persist_directory=path, embedding_function=embedding)
        retr = vs.as_retriever(search_type="mmr", search_kwargs={"k": k})
        docs = retr.invoke(query)
        all_results[topic] = docs
        print(f"{topic} ({len(docs)}개): {[doc.metadata for doc in docs]}")
    return all_results
