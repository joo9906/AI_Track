from dotenv import load_dotenv
import os
from langchain_chroma import Chroma
from langchain_upstage import UpstageEmbeddings

# 1. .env 파일에서 환경변수 불러오기
load_dotenv()
api_key = os.getenv("UPSTAGE_API_KEY")

# 2. 임베딩 모델 생성 (API 키 전달)
embedding = UpstageEmbeddings(
    model="solar-embedding-1-large",
    api_key=api_key
)

# 3. 이미 저장된 ChromaDB 경로
persist_directory = "./chroma_db"  # 크로마DB가 저장된 폴더 경로로 수정

# 4. 저장된 크로마DB에서 벡터스토어 불러오기
vectorstore = Chroma(
    persist_directory=persist_directory,
    embedding_function=embedding
)

def retriever(query, k=3):
    retriever = vectorstore.as_retriever(
        search_type='mmr',
        search_kwargs={"k": k}
    )
    result_docs = retriever.invoke(query)
    return result_docs
