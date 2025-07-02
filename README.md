# AI_Track

## 진행 상황
### 07.01 16:00
- 프론트 완료, 백 + LLM으로 직접 넘기는 부분 추가해야 함
### 07.02 16:00
- 프론트에 히스토리 저장
- 서버로는 사용자의 현재 질문만 전달(sessionID는 UUID로 생성, message는 str로 보냄)
- 

## 파일 구성
### colab
- *.csv : 실제로 사용할 데이터 셋
- Team8.ipynb : Solar 이용을 위한 코드

### Front
- src/App.vue 부분 프론트엔드 코드
- Vue, JS로 구성

### server
- 서버 관련 파일들
- fastApi로 구성

