from pydantic import BaseModel


class DiagnosisRequest(BaseModel):
    symptoms: str
    age: int | None = None
    gender: str | None = None
    duration_days: int | None = None
