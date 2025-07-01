from langchain_upstage import ChatUpstage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

llm = ChatUpstage()

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