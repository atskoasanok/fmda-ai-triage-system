from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.services.llm import get_diagnosis
import json

router = APIRouter()

# ---------- Request schema ----------
class Message(BaseModel):
    role: str
    content: str

class ChatRequest(BaseModel):
    messages: List[Message]

# ---------- Chat endpoint ----------
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
                    "content": json.dumps(result)  # ✅ IMPORTANT
                },
                "finish_reason": "stop"
            }
        ]
    }

# ---------- Models endpoint (CRITICAL) ----------
@router.get("/v1/models")
def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "fmda",
                "object": "model",
                "owned_by": "fmda"
            }
        ]
    }
