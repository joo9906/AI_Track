# AI_Track

## 진행 상황
### 07.01 
- 16:00 : 프론트 완료, 백 + LLM으로 직접 넘기는 부분 추가해야 함
### 07.02
- 10:30 : server쪽 파일들 수정
-  retrieval.py : 단일 db 참조에서 다중 db 참조로 변경
-  chat.py : 프롬프트 수정
- 11:00 : 전체 코드 수정
-   app.py : 실제 환자 정보와 history 활용
-   front/App.vue : 서버로 실제 환자 정보 날림 + 히스토리 및 환자 정보 pinia 저장

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

