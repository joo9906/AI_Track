# AI_Track
## 진행 상황
### 07.01 
- 16:00 : 프론트 완료, 백 + LLM으로 직접 넘기는 부분 추가해야 함
### 07.02
- 10:30 : server쪽 파일들 수정
  - retrieval.py : 단일 db 참조에서 다중 db 참조로 변경
  -  chat.py : 프롬프트 수정
- 11:00 : 전체 코드 수정
  -   ec2 서버와 연결
  -   프론트 코드 수정
- 17:00
  - 채팅창 환자요약정보 사이 gap 추가
  - 서버 쪽으로 히스토리 보냄 -> sysprompt가 있으면 유저의 메세지만 보내고 아니면 환자 정보도 처음엔 보내줌
### 07.03
- 16:00 : 프론트 전체 수정
  - component로 분화하여 관리
  - ui 개선
  - pinia에 환자 + 대화를 저장하여 불러올 수 있게 함
  - amplify로 올릴 수 있는 yml 파일 생성
  - 배포 완료
## 파일 구성
### colab
- *.csv : 실제로 사용할 데이터 셋
- Team8.ipynb : Solar 이용을 위한 코드, 백터화

### Front
- src/App.vue 부분 프론트엔드 코드
- Vue, JS로 구성
  - npm run dev로 서버 구동

### server
- 서버 관련 파일들
- fastApi로 구성
  - python app.py로 서버 구동

