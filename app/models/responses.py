from pydantic import BaseModel
from typing import List


class DiagnosisResponse(BaseModel):
    triage_level: str
    risk_flags: List[str]
    possible_conditions: List[str]
    recommendation: str
    llm_explanation: str
    safety_notice: str
