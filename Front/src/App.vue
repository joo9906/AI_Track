<template>
  <div class="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-4">
    <div v-if="!patientInfoSubmitted" class="w-full max-w-md bg-white rounded-lg shadow-lg p-8">
      <h2 class="text-2xl font-bold mb-6 text-center text-blue-700">환자 정보 입력</h2>
      <form @submit.prevent="submitPatientInfo" class="space-y-4">
        <div>
          <label class="block text-gray-700 mb-1">나이</label>
          <input v-model="patient.age" type="number" min="0" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" required />
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
          <input v-model="patient.drug" type="text" placeholder="예: Epinephrine 1 MG Auto-Injection, Diazepam 5 MG Oral Tablet " class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" />
        </div>

        <div>
          <label class="block text-gray-700 mb-1">알러지 정보</label>
          <input v-model="patient.allergies" type="text" placeholder="예: 페니실린 알러지" class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" />
        </div>

        <div>
          <label class="block text-gray-700 mb-1">수술 및 시술 정보</label>
          <input v-model="patient.procedures" type="text" placeholder="예: 충수절제술, 심장판막치환술
          " class="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" />
        </div>

        <button type="submit" class="w-full bg-blue-600 text-white py-2 rounded font-semibold hover:bg-blue-700 transition">입력 완료</button>
      </form>
    </div>
    <div v-else class="w-full max-w-2xl bg-white rounded-lg shadow-lg p-6 flex flex-col h-[70vh]">
      <div class="mb-4 p-4 rounded-lg bg-blue-50 border border-blue-200 text-blue-900 text-sm shadow-sm">
        <div class="font-bold text-base mb-1">환자 요약 정보</div>
        <div class="flex flex-wrap gap-x-6 gap-y-1">
          <div>나이: <span class="font-semibold">{{ patient.age }}</span>세</div>
          <div>성별: <span class="font-semibold">{{ patient.gender }}</span></div>
          <div>흡연여부: <span class="font-semibold">{{ patient.smoke }}</span></div>
          <div>최고혈압: <span class="font-semibold">{{ patient.sbp }}</span></div>
          <div>최저혈압: <span class="font-semibold">{{ patient.dbp }}</span></div>
        </div>
        <div class="mt-1">기저질환: <span class="font-semibold">{{ patient.comorbidity || '없음' }}</span></div>
        <div>투약 약물: <span class="font-semibold">{{ patient.drug || '없음' }}</span></div>
        <div>알러지: <span class="font-semibold">{{ patient.allergies || '없음' }}</span></div>
        <div>수술/시술: <span class="font-semibold">{{ patient.procedures || '없음' }}</span></div>
      </div>
      <div class="flex-1 overflow-y-auto mb-4 space-y-2" ref="chatContainer">
        <div v-for="(msg, idx) in messages" :key="idx" :class="msg.role === 'user' ? 'text-right' : 'text-left'">
          <div :class="msg.role === 'user' ? 'inline-block bg-blue-100 text-blue-900 px-4 py-2 rounded-lg' : 'inline-block bg-gray-200 text-gray-800 px-4 py-2 rounded-lg'">
            {{ msg.content }}
          </div>
        </div>
      </div>
      <form @submit.prevent="sendMessage" class="flex gap-2">
        <input v-model="input" type="text" placeholder="메시지를 입력하세요..." class="flex-1 border border-gray-300 rounded px-3 py-2 focus:outline-none focus:ring-2 focus:ring-blue-400" />
        <button type="submit" class="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700 transition">전송</button>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, nextTick } from 'vue'

const patient = ref({
  age: '', // 나이
  gender: '', //성별
  sbp: '', //최고 혈압
  dbp: '', //최저 혈압
  smoke: '', // 흡연 여부
  comorbidity: '', // 질병 정보(기저 질환)
  drug: '', // 투약 약물 정보
  allergies: '', //알러지 정보
  procedures: '', //수술, 시술 정보
})
const patientInfoSubmitted = ref(false)
const messages = ref([])
const input = ref('')
const chatContainer = ref(null)

function makeLLMPrompt(patient) {
  prompt_content = `당신은 환자 정보에 대한 질문에 친절히 답변하는 한국어 의료 AI 어시스턴트입니다.\n아래 CONTEXT 정보를 참고하여 환자 정보를 자연스럽고 이해하기 쉽게 한국어로 풀어서 설명해 주세요.\nCONTEXT 정보는 총 6가지로 제공됩니다. 각각은 순서대로 환자 기본 정보, 진단 질병 정보, 약물 투여 기록, 알러지 반응 기록, 바이탈/검사 수치, 수술/시술 이력입니다.\nPATIENT_ID를 기준으로 같은 환자의 정보를 연결해서 참고하세요. 해당 환자가 존재하지 않다면, 유사한 환자의 기록으로 대체해주세요.\n각 정보를 의료진이 환자에게 직접 설명하듯 문단 형태로 자연스럽게 이어서 작성해 주세요.\n너무 긴 리스트 형태는 피하고, 중요한 내용은 간결히 요약해 주세요.\n모르면 모른다고 솔직히 답변하세요.\n\n[CONTEXT]\n1. 환자 기본 정보: 나이 ${patient.age ?? ''}세, 성별 ${patient.gender ?? ''}, 흡연여부 ${patient.smoke ?? ''}\n2. 진단 질병 정보: ${patient.comorbidity ?? ''}\n3. 약물 투여 기록: ${patient.drug ?? ''}\n4. 알러지 반응 기록: ${patient.allergies ?? ''}\n5. 바이탈/검사 수치: 최고혈압 ${patient.sbp ?? ''}, 최저혈압 ${patient.dbp ?? ''}\n6. 수술/시술 이력: ${patient.procedures ?? ''}`
  console.log(prompt_content)
  return prompt_content;
}

function submitPatientInfo() {
  if (!patient.value.gender) return alert('성별을 선택해주세요.');
  if (!patient.value.smoke) return alert('흡연 여부를 선택해주세요.');
  // 비어있는 항목은 '없음'으로 자동 입력
  if (!patient.value.procedures) patient.value.procedures = '없음';
  if (!patient.value.drug) patient.value.drug = '없음';
  if (!patient.value.allergies) patient.value.allergies = '없음';
  if (!patient.value.comorbidity) patient.value.comorbidity = '없음';
  patientInfoSubmitted.value = true;
  messages.value.push({
    role: 'system',
    content: makeLLMPrompt(patient.value),
  });
  nextTick(() => {
    if (chatContainer.value) chatContainer.value.scrollTop = chatContainer.value.scrollHeight;
  });
}

function sendMessage() {
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
}
</script>

<style>
body {
  font-family: 'Pretendard', 'Noto Sans KR', sans-serif;
}
</style>
