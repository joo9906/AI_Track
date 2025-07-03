import { defineStore } from 'pinia';
import { v4 as uuidv4 } from 'uuid';

export const useChatStore = defineStore('chat', {
  state: () => ({
    patientInfo: null,
    messages: [],
    isLoading: false,
  }),
  actions: {
    registerPatient(info) {
      this.patientInfo = {
        name: `Patient-${uuidv4().slice(0, 8)}`,
        ...info,
      };
      this.messages.push({
        sender: 'bot',
        text: `안녕하세요, ${this.patientInfo.name}님. 어떤 도움이 필요하신가요?`,
      });
    },
    addMessage(message) {
      this.messages.push(message);
    },
    setLoading(status) {
      this.isLoading = status;
    },
    clearSession() {
      this.patientInfo = null;
      this.messages = [];
      this.isLoading = false;
    },
  },
});
