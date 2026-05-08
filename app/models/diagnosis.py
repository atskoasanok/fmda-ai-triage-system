from pydantic import BaseModel


class DiagnosisRequest(BaseModel):
    symptoms: str


class DiagnosisResponse(BaseModel):
    conditions: list[str]
    severity: str
    urgency: str
    recommendation: str
