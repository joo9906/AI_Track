# 🏥 RAG 기반 환자 요약 및 투약 제안 챗봇

## 💡 프로젝트 소개

본 프로젝트는 환자 CSV 데이터를 기반으로 환자 개인 맞춤형 요약 정보를 생성하고, RAG(Retrieval-Augmented Generation) 구조를 통해 의료진에게 투약 제안을 제공하는 챗봇 시스템입니다.  
임베딩 모델, 벡터 스토어, LLM을 결합하여 정확하고 신뢰성 있는 응답을 제공합니다.

---

## 🚀 사용법

(예시)
1. 환자 CSV 파일(patients.csv, conditions.csv 등)을 준비합니다.
2. 파싱 및 임베딩 후 벡터 DB(Chroma)에 저장합니다.
3. 챗봇 UI 또는 CLI 환경에서 자연어로 질의를 입력합니다.
4. 챗봇이 환자 정보 기반의 요약 및 투약 제안을 반환합니다.

---

## 🌐 배포된 링크

- **웹 데모 링크**: [바로가기](https://main.d2pi120e4ybq0g.amplifyapp.com)
- **API 문서**: [API Docs](https://your-api-doc-link.com)

---

## ⚙️ 실행 방법

(예시)
```bash
# 1. 레포 클론
git clone https://github.com/your-org/your-repo.git
cd your-repo

# 2. 의존성 설치
pip install -r requirements.txt

# 3. 로컬 실행
python app.py

# 4. (선택) Chroma DB 초기화 및 벡터 DB 생성
python create_vectorstore.py

# 5. 웹 또는 CLI에서 챗봇 사용
