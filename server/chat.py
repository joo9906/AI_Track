from dotenv import load_dotenv
import os
from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# .env 파일에서 환경변수 불러오기
load_dotenv()

# 환경변수에서 API 키 읽기
api_key = os.getenv("UPSTAGE_API_KEY")

# ChatUpstage에 API 키 전달
llm = ChatUpstage(api_key=api_key)

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            당신은 질문-응답 작업을 위한 어시스턴트입니다.
            대화의 히스토리를 고려하여, 아래에 제공된 검색된 문맥 정보를 활용해 질문에 답변하세요.
            만약 답을 모른다면, 모른다고만 답변하세요.
            반드시, 한국어로 대답하세요.
            ---
            CONTEXT:
            {context}
            """,
        ),
        ("human", "{input}"),
    ]
)

def chat(query, doc):
    chain = prompt | llm | StrOutputParser()
    response = chain.invoke({"context": doc, "input": query})
    return response
