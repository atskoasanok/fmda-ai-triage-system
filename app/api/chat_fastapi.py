from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.services.llm import get_diagnosis
import json

router = APIRouter()

class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    model: str = "fmda"
    messages: List[Message]

@router.post("/v1/chat/completions")
def chat(req: ChatRequest):
    user_msg = req.messages[-1].content

    result = get_diagnosis(user_msg)

    return {
        "id": "fmda-chat",
        "object": "chat.completion",
        "model": "fmda",
        "choices": [
            {
                "index": 0,
                "message": {
                    "role": "assistant",
                    "content": json.dumps(result)
                },
                "finish_reason": "stop"
            }
        ]
    }
