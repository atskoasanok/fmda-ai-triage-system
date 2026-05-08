from fastapi import APIRouter
from pydantic import BaseModel
from typing import List
from app.services.llm import get_diagnosis

router = APIRouter()


class Message(BaseModel):
    role: str
    content: str


class ChatRequest(BaseModel):
    model: str = "fmda"
    messages: List[Message]


def format_diagnosis(result: dict) -> str:
    conditions = ", ".join(result.get("conditions", [])) or "Unknown"
    severity = result.get("severity", "Unknown")
    urgency = result.get("urgency", "Unknown")
    recommendation = result.get("recommendation", "No recommendation available.")

    return (
        f"Possible conditions: {conditions}\n"
        f"Severity: {severity}\n"
        f"Urgency: {urgency}\n"
        f"Recommendation: {recommendation}"
    )


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
                    "content": format_diagnosis(result),
                },
                "finish_reason": "stop",
            }
        ],
    }


@router.get("/v1/models")
def list_models():
    return {
        "object": "list",
        "data": [
            {
                "id": "fmda",
                "object": "model",
                "owned_by": "fmda",
            }
        ],
    }
