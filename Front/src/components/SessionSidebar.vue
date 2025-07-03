<template>
  <div class="w-64 bg-white border-r border-gray-200 p-4 overflow-y-auto">
    <h2 class="text-lg font-bold mb-4 text-gray-800">대화 세션</h2>
    <div v-for="session in sessions" :key="session.id" class="mb-3">
      <button
        class="w-full text-left p-3 border border-gray-200 rounded-lg hover:bg-blue-50 hover:border-blue-300 transition-colors"
        @click="$emit('select', session)"
      >
        <div class="flex items-center gap-2 mb-1">
          <span class="text-lg">🧑</span>
          <span class="font-medium text-gray-900">{{ session.patient.age }}세 / {{ session.patient.gender }}</span>
        </div>
        <div class="text-xs text-gray-500">
          환자 번호: {{ session.id }}
        </div>
      </button>
      <div class="ml-2 mt-2 text-sm text-gray-600 space-y-1" v-if="session.messages.length">
        <div v-for="(msg, i) in session.messages.slice(-2)" :key="i" class="truncate">
          <span class="font-medium">{{ msg.role === 'user' ? '사용자' : 'AI' }}:</span> 
          <span class="text-gray-500">{{ msg.content.substring(0, 30) }}{{ msg.content.length > 30 ? '...' : '' }}</span>
        </div>
      </div>
    </div>
    <div v-if="sessions.length === 0" class="text-center text-gray-500 py-8">
      <p>등록된 세션이 없습니다</p>
      <p class="text-sm">환자 정보를 입력해주세요</p>
    </div>
  </div>
</template>

<script setup>
defineProps(['sessions'])
defineEmits(['select'])
</script> 