from langchain_chroma import Chroma
from langchain_upstage import UpstageEmbeddings

# 이미 저장된 ChromaDB 경로
persist_directory = "./chroma_db"  # 크로마DB가 저장된 폴더 경로로 수정

# 임베딩 모델은 반드시 저장할 때 사용한 것과 동일해야 함
embedding = UpstageEmbeddings(model="solar-embedding-1-large")

# 저장된 크로마DB에서 벡터스토어 불러오기
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