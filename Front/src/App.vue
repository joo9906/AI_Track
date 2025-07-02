<template>
  <div class="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-4">
    <!-- 환자 정보 입력 폼 -->
    <div v-if="!patientInfoSubmitted" class="w-full max-w-md bg-white rounded-lg shadow-lg p-8">
      <h2 class="text-2xl font-bold mb-6 text-center text-blue-700">환자 정보 입력</h2>
      <form @submit.prevent="submitPatientInfo" class="space-y-4">
        <!-- 입력 필드들 -->
        <div>
          <label class="block text-gray-700 mb-1">나이</label>
          <input v-model="patient.age" type="number" min="0" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" required />
        </div>
        <div>
          <label class="block text-gray-700 mb-1">체중 (kg)</label>
          <input v-model="patient.weight" type="number" min="0" step="0.1" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" required />
        </div>
        <div class="flex gap-4">
          <div class="flex-1">
            <label class="block text-gray-700 mb-1">최고혈압</label>
            <input v-model="patient.sbp" type="number" min="0" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" required />
          </div>
          <div class="flex-1">
            <label class="block text-gray-700 mb-1">최저혈압</label>
            <input v-model="patient.dbp" type="number" min="0" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" required />
          </div>
        </div>
        <div>
          <label class="block text-gray-700 mb-1">기저질환</label>
          <input v-model="patient.comorbidity" type="text" placeholder="예: 당뇨, 고혈압" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" />
        </div>
        <div>
          <label class="block text-gray-700 mb-1">성별</label>
          <div class="flex gap-4">
            <button type="button" :class="['flex-1 py-2 rounded border', patient.gender === '남' ? 'bg-blue-500 text-white border-blue-500' : 'bg-white text-gray-700 border-gray-300']" @click="patient.gender = '남'">남</button>
            <button type="button" :class="['flex-1 py-2 rounded border', patient.gender === '여' ? 'bg-pink-500 text-white border-pink-500' : 'bg-white text-gray-700 border-gray-300']" @click="patient.gender = '여'">여</button>
          </div>
        </div>
        <div>
          <label class="block text-gray-700 mb-1">흡연 여부</label>
          <div class="flex gap-4">
            <button type="button" :class="['flex-1 py-2 rounded border', patient.smoke === '흡연자' ? 'bg-blue-500 text-white border-blue-500' : 'bg-white text-gray-700 border-gray-300']" @click="patient.smoke = '흡연자'">흡연</button>
            <button type="button" :class="['flex-1 py-2 rounded border', patient.smoke === '비흡연자' ? 'bg-blue-500 text-white border-pink-500' : 'bg-white text-gray-700 border-gray-300']" @click="patient.smoke = '비흡연자'">비흡연</button>
          </div>
        </div>
        <div>
          <label class="block text-gray-700 mb-1">투약 약물 정보</label>
          <input v-model="patient.drug" type="text" placeholder="예: Epinephrine 1 MG Auto-Injection" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" />
        </div>
        <div>
          <label class="block text-gray-700 mb-1">알러지 정보</label>
          <input v-model="patient.allergies" type="text" placeholder="예: 페니실린 알러지" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" />
        </div>
        <div>
          <label class="block text-gray-700 mb-1">수술 및 시술 정보</label>
          <input v-model="patient.procedures" type="text" placeholder="예: 충수절제술" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" />
        </div>
        <button type="submit" class="w-full bg-blue-600 text-white py-2 rounded font-semibold hover:bg-blue-700 transition">입력 완료</button>
      </form>
    </div>

    <!-- 환자 요약 + 채팅 영역 -->
    <div v-else class="flex flex-row w-full max-w-6xl bg-white opacity-90 rounded-lg shadow-lg p-6 h-[900px] gap-[100px]">
      <!-- 환자 요약 카드 -->
      <div class="w-80 flex-shrink-0">
        <div class="p-4 rounded-lg bg-white border border-gray-300 text-gray-900 text-sm shadow-md w-full">
          <div class="font-bold text-lg mb-3 border-b pb-2">환자 요약 정보</div>
          <table class="w-full text-sm border-separate border-spacing-y-1">
            <tbody class="space-y-1">
              <tr><td class="font-medium text-blue-700">나이</td><td class="text-right font-semibold text-black">{{ patient.age }}세</td></tr>
              <tr><td class="font-medium text-blue-700">성별</td><td class="text-right font-semibold text-black">{{ patient.gender }}</td></tr>
              <tr><td class="font-medium text-blue-700">체중</td><td class="text-right font-semibold text-black">{{ patient.weight }}kg</td></tr>
              <tr><td class="font-medium text-blue-700">흡연여부</td><td class="text-right font-semibold text-black">{{ patient.smoke }}</td></tr>
              <tr><td class="font-medium text-blue-700">최고혈압</td><td class="text-right font-semibold text-black">{{ patient.sbp }}</td></tr>
              <tr><td class="font-medium text-blue-700">최저혈압</td><td class="text-right font-semibold text-black">{{ patient.dbp }}</td></tr>
              <tr><td class="font-medium text-blue-700">기저질환</td><td class="text-right font-semibold text-black">{{ patient.comorbidity || '없음' }}</td></tr>
              <tr><td class="font-medium text-blue-700">투약 약물</td><td class="text-right font-semibold text-black">{{ patient.drug || '없음' }}</td></tr>
              <tr><td class="font-medium text-blue-700">알러지</td><td class="text-right font-semibold text-black">{{ patient.allergies || '없음' }}</td></tr>
              <tr><td class="font-medium text-blue-700">수술/시술</td><td class="text-right font-semibold text-black">{{ patient.procedures || '없음' }}</td></tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- 채팅창 -->
      <div class="flex-1 flex flex-col min-h-0 ml-4">
        <div
          class="overflow-y-auto mb-4 space-y-2 flex-1 px-2"
          ref="chatContainer"
          style="max-height: 100%;"
        >
          <div v-for="(msg, idx) in messages.filter(m => m.role !== 'system')" :key="idx" :class="msg.role === 'user' ? 'text-right' : 'text-left'">
            <div :class="msg.role === 'user' ? 'inline-block bg-blue-100 text-blue-900 px-4 py-2 rounded-lg max-w-xs lg:max-w-md' : 'inline-block bg-gray-200 text-gray-800 px-4 py-2 rounded-lg max-w-xs lg:max-w-md'">
              {{ msg.content }}
            </div>
          </div>
        </div>
        <form @submit.prevent="sendMessage" class="flex gap-2 flex-shrink-0">
          <input v-model="input" type="text" placeholder="메시지를 입력하세요..." class="flex-1 border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" />
          <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition">전송</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'
import { v4 as uuidv4 } from 'uuid'

const sessionId = ref(uuidv4())

const patient = ref({
  age: '',       // 나이
  gender: '',    // 성별
  weight: '',    // 체중
  sbp: '',       // 최고 혈압
  dbp: '',       // 최저 혈압
  smoke: '',     // 흡연 여부
  comorbidity: '', // 기저 질환
  drug: '',        // 복용 중인 약물
  allergies: '',   // 알러지 정보
  procedures: '',  // 수술/시술 정보
})

const patientInfoSubmitted = ref(false)
const messages = ref([])
const input = ref('')
const chatContainer = ref(null)

function makeLLMPrompt(patient) {
  return `
당신은 의료 전문가의 약물 투약 의사결정을 돕는 AI입니다.
아래 CONTEXT 정보를 참고하세요.

[CONTEXT]
1. 환자 기본 정보: 나이 ${patient.age ?? ''}세, 성별 ${patient.gender ?? ''}, 체중 ${patient.weight ?? ''}kg, 흡연 여부: ${patient.smoke ?? ''}
2. 진단 질병 정보: ${patient.comorbidity || '없음'}
3. 약물 투여 기록: ${patient.drug || '없음'}
4. 알러지 반응 기록: ${patient.allergies || '없음'}
5. 바이탈/검사 수치: 최고혈압 ${patient.sbp ?? ''}, 최저혈압 ${patient.dbp ?? ''}
6. 수술/시술 이력: ${patient.procedures || '없음'}

전문 의료진들이 사용하는 언어로 답변해주세요.
모르면 모른다고 하세요.
`.trim()
}

function submitPatientInfo() {
  if (!patient.value.gender) return alert('성별을 선택해주세요.');
  if (!patient.value.smoke) return alert('흡연 여부를 선택해주세요.');

  // 비어 있는 항목 기본값 설정
  patient.value.procedures ||= '없음';
  patient.value.drug ||= '없음';
  patient.value.allergies ||= '없음';
  patient.value.comorbidity ||= '없음';

  patientInfoSubmitted.value = true

  // system 메시지를 messages에 추가
  const systemPrompt = makeLLMPrompt(patient.value)
  messages.value.push({ role: 'system', content: systemPrompt })

  nextTick(() => {
    if (chatContainer.value) chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  })
}

async function sendMessage() {
  if (!input.value.trim()) return;

  const userMessage = input.value.trim()
  input.value = ''

  // 프론트 히스토리 누적
  messages.value.push({ role: 'user', content: userMessage })

  await nextTick(() => {
    if (chatContainer.value) chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  })

  // system prompt를 미리 꺼내기
  let systemPrompt = messages.value.find(m => m.role === 'system')?.content
  if (!systemPrompt) {
    systemPrompt = makeLLMPrompt(patient.value)
    messages.value.unshift({ role: 'system', content: systemPrompt })
  }

  // 서버에 보낼 메시지: system + 마지막 user만 포함
  const messageToSend = `system: ${systemPrompt}\nuser: ${userMessage}`

  try {
    const res = await fetch(`${import.meta.env.VITE_SERVER_API}/chat`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        session_id: sessionId.value,
        message: messageToSend
      })
    })

    const data = await res.json()
    const reply = data.reply?.answer || data.reply || 'AI 응답이 없습니다.'
    messages.value.push({ role: 'assistant', content: reply })
  } catch (err) {
    console.error('서버 요청 실패:', err)
    messages.value.push({ role: 'assistant', content: '서버 연결 실패.' })
  }

  await nextTick(() => {
    if (chatContainer.value) chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  })
}
</script>


<style>
body {
  font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
}
</style>


<!-- 수정 전 sendMessage(프롬프트 충돌 가능성 있음) -->
<!-- function sendMessage() {
  if (!input.value.trim()) return
  messages.value.push({ role: 'user', content: input.value })
  // 실제 LLM 연동 부분은 추후 구현
  setTimeout(() => {
    messages.value.push({ role: 'assistant', content: '여기에 LLM 응답이 표시됩니다.' })
    nextTick(() => {
      if (chatContainer.value) chatContainer.value.scrollTop = chatContainer.value.scrollHeight
    })
  }, 600)
  input.value = ''
  nextTick(() => {
    if (chatContainer.value) chatContainer.value.scrollTop = chatContainer.value.scrollHeight
  })
} -->