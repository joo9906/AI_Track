from dotenv import load_dotenv
import os
from langchain_upstage import ChatUpstage

load_dotenv()
api_key = os.getenv("UPSTAGE_API_KEY")
llm = ChatUpstage(api_key=api_key)

def chat(query, docs_dict, patient, history=None):
    try:
        # 시스템 프롬프트 작성
        prompt_text = """
당신은 의료 전문가의 약물 투약 의사결정을 돕는 AI입니다.
다음은 실제 환자와 유사한 가상환자의 정보입니다. 이를 기반으로 적절한 약물을 제안하십시오.
답변은 간결하고 의사결정에 도움이 될 만한 유의미한 정보만 제공해야 합니다.
환자가 실제로 복용 중인 약물 정보는 '[실제 환자 정보]'의 '투약 약물' 항목에 명시됩니다.
환자가 실제로 가진 알러지는 '[실제 환자 정보]'의 '알러지' 항목에 명시됩니다.
해당 항목에 '없음'으로 표기된 경우, 환자가 현재 복용 중인 약물과 알러지은 없다고 간주해야 합니다.
환자가 복용하지 않은 약물을 '복용 중'으로 간주하거나 언급하지 마십시오.
환자가 가지지 않은 알러지를 '알러지 보유'로 간주하거나 언급하지 마십시오.
답변은 무조건 한국어로 답변해주세요.
답변은 항상 의료 전문가를 대상으로 하는 것이기에 전문가의 조언을 구하는 내용은 반드시 넣지 말아주세요.
"""

        # 실제 환자 정보
        prompt_text += "\n[실제 환자 정보]\n"
        for key, value in patient.items():
            prompt_text += f"{key}: {value}\n"

        # 벡터 검색 정보
        for topic, docs in docs_dict.items():
            context = "\n".join([
                d.page_content if hasattr(d, "page_content") else str(d)
                for d in docs
            ])
            prompt_text += f"\n--- {topic.upper()} 정보 ---\n{context}\n"

        # 사용자 질문 추가
        prompt_text += f"\n사용자 질문: {query}\n"

        # LLM 직접 호출
        result = llm.invoke(prompt_text)
        
        # content만 추출
        if hasattr(result, 'content'):
            answer = result.content
        elif isinstance(result, dict) and 'content' in result:
            answer = result['content']
        else:
            answer = str(result)

        return {"answer": answer, "status": "success"}

    except Exception as e:
        return {"answer": "오류 발생", "status": "fail", "error": str(e)}
