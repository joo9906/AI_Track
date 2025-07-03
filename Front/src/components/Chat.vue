<template>
  <div class="flex flex-col flex-1" style="margin-left: 10px;">
    <div class="flex-1 overflow-y-auto p-4 border border-gray-200 mb-4 bg-gray-50 rounded-lg">
      <div v-for="(msg, i) in messages" :key="i" class="mb-6">
        <div :class="msg.role === 'user' ? 'text-right' : 'text-left'">
          <div :class="msg.role === 'user' ? 'inline-block bg-blue-100 text-blue-900 px-4 py-2 rounded-lg max-w-xs lg:max-w-md' : 'inline-block bg-gray-200 text-gray-800 px-4 py-2 rounded-lg max-w-xs lg:max-w-md'">
            <div class="font-semibold text-xs mb-1">{{ msg.role === 'user' ? '사용자' : 'AI' }}</div>
            {{ msg.content }}
          </div>
        </div>
      </div>
      <div v-if="messages.length === 0" class="text-center text-gray-500 py-8">
        <p>대화를 시작해보세요</p>
      </div>
    </div>
    <form @submit.prevent="send" class="flex gap-2">
      <input 
        v-model="input" 
        class="flex-1 border border-gray-300 px-3 py-2 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400" 
        placeholder="메시지를 입력하세요" 
      />
      <button 
        type="submit"
        class="bg-blue-600 text-white px-4 py-2 rounded-lg hover:bg-blue-700 transition font-semibold"
      >
        전송
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps(['messages'])
const emit = defineEmits(['send'])
const input = ref('')

function send() {
  if (!input.value.trim()) return
  emit('send', { content: input.value.trim() })
  input.value = ''
}
</script> 