# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from chat import chat, session_contexts
from retriever import retriever

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 개발용
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageRequest(BaseModel):
    session_id: str
    message: str

@app.post("/chat")
async def chat_endpoint(req: MessageRequest):
    # 최초 대화라면 retriever로 context 추출
    if req.session_id not in session_contexts:
        context = retriever(req.message)
        reply = chat(req.session_id, req.message, context)
    else:
        reply = chat(req.session_id, req.message)
    return {"reply": reply}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
