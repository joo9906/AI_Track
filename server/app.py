from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from chat import chat
from retriever import multi_retrieve

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class MessageRequest(BaseModel):
    message: str
    patient: dict
    history: Optional[list] = None

@app.post("/chat")
async def chat_endpoint(query: MessageRequest):
    docs_dict = multi_retrieve(query.message)
    return {"reply": chat(query.message, docs_dict=docs_dict, patient=query.patient, history=query.history)}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)