<template>
  <div class="flex flex-col h-screen">
    <!-- 네비게이션 바 -->
<div class="w-full flex justify-center pt-4 pb-2 sticky top-0 z-20">
  <nav class="max-w-xl w-full bg-gradient-to-r from-blue-500 via-blue-600 to-blue-700 text-white shadow-lg rounded-2xl flex items-center justify-between px-6 py-3">
    <div class="flex items-center gap-3">
      <div class="bg-white bg-opacity-10 rounded-full p-2 shadow">
        <IdentificationIcon class="w-7 h-7 text-white drop-shadow" />
      </div>
      <span class="text-2xl font-extrabold drop-shadow-sm text-white">약물 투약 제안 챗봇</span>
    </div>
    <div class="hidden md:flex items-center gap-6 pr-2">
      <span class="text-sm text-blue-100 font-semibold tracking-wide">Powered by AI</span>
    </div>
  </nav>
</div>

    <div class="flex flex-1 overflow-hidden">
      <div v-if="showSidebar && selectedSession">
        <SessionSidebar :sessions="sessions" @select="handleSelectSession" />
      </div>
      <div class="flex-1 flex flex-col overflow-hidden">
        <div v-if="selectedSession" class="flex items-center justify-between p-4 flex-shrink-0">
          <button
            class="bg-gray-200 text-gray-700 px-4 py-2 rounded hover:bg-blue-100 transition font-semibold"
            @click="showSidebar = !showSidebar"
          >
            {{ showSidebar ? '대화 세션 닫기' : '대화 세션 보기' }}
          </button>
        </div>
        <div class="flex-1 flex flex-col p-4 overflow-hidden">
          <div v-if="!selectedSession" class="flex-1 overflow-hidden">
            <PatientForm @submit="handleNewSession" />
          </div>
          <div v-else class="flex gap-16 h-full overflow-hidden">
            <PatientInfo :patient="selectedSession.patient" :session-id="selectedSession.id" />
            <Chat
              :messages="selectedSession.messages.filter(msg => msg.role !== 'system')"
              @send="handleSendMessage"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { v4 as uuidv4 } from 'uuid'
import SessionSidebar from './components/SessionSidebar.vue'
import PatientForm from './components/PatientForm.vue'
import PatientInfo from './components/PatientInfo.vue'
import Chat from './components/Chat.vue'
import { IdentificationIcon } from '@heroicons/vue/24/outline'

const sessions = ref([])
const selectedSession = ref(null)
const showSidebar = ref(false)

function makeLLMPrompt(patient) {
  return `
[New_Patient]
1. 환자 기본 정보: 나이 ${patient.age ?? ''}세, 성별 ${patient.gender ?? ''}, 체중 ${patient.weight ?? ''}kg, 흡연 여부: ${patient.smoke ?? ''}
2. 진단 질병 정보: ${patient.comorbidity || '없음'}
3. 약물 투여 기록: ${patient.drug || '없음'}
4. 알러지 반응 기록: ${patient.allergies || '없음'}
5. 바이탈/검사 수치: 최고혈압 ${patient.sbp ?? ''}, 최저혈압 ${patient.dbp ?? ''}
6. 수술/시술 이력: ${patient.procedures || '없음'}
전문 의료진들이 사용하는 언어로 답변해주세요.
대답은 보기 쉽게 정리하여 마크다운 형식으로 주세요.
`.trim();
}

function handleNewSession(patientData) {
  const newSession = {
    id: uuidv4().replace(/-/g, '').substring(0, 8),
    patient: patientData,
    messages: [],
    createdAt: new Date()
  }
  sessions.value.push(newSession)
  selectedSession.value = newSession
}

function handleSelectSession(session) {
  selectedSession.value = session
  showSidebar.value = false
}

async function handleSendMessage(message) {
  if (!selectedSession.value) return;
  // 사용자 메시지 추가
  selectedSession.value.messages.push({ ...message, role: 'user' });

  // system prompt 생성 (최초 메시지일 때만)
  let systemPrompt = '';
  if (selectedSession.value.messages.filter(m => m.role === 'system').length === 0) {
    systemPrompt = makeLLMPrompt(selectedSession.value.patient);
    selectedSession.value.messages.unshift({ role: 'system', content: systemPrompt });
  } else {
    systemPrompt = selectedSession.value.messages.find(m => m.role === 'system')?.content || '';
  }

  // 서버로 메시지 전송
  let messageToSend = '';
  if (systemPrompt && selectedSession.value.messages.filter(m => m.role === 'assistant').length === 0) {
    messageToSend = `system: ${systemPrompt}\nuser: ${message.content}`;
  } else {
    messageToSend = `user: ${message.content}`;
  }

  try {
    const res = await fetch(`${import.meta.env.VITE_SERVER_API}/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        session_id: selectedSession.value.id,
        message: messageToSend
      })
    });
    const data = await res.json();
    const reply = data.reply?.answer || data.reply || 'AI 응답이 없습니다.';
    selectedSession.value.messages.push({ role: 'assistant', content: reply });
  } catch (err) {
    selectedSession.value.messages.push({ role: 'assistant', content: '서버 연결 실패.' });
  }
}
</script>

<style>
body {
  font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
}
</style>


