// 챗봇과 사용자가 주고받은 대화 저장을 위한 Pinia
import {defineStore} from 'pinia'
import {ref} from 'vue'

export const useChatStore = defineStore('chat', () => {
    const history = ref([])
    const patientInfo = ref('')
    const response = ref('')
    const loading = ref(false)

    const addHistory = (user, assistant) =>{
        history.value.push({user, assistant})
    }

    return {
        history,
        patientInfo,
        response,
        loading,
        addHistory
    }
})

