from fastapi import APIRouter

from app.models.requests import DiagnosisRequest
from app.models.responses import DiagnosisResponse

from app.services.triage import analyze_triage
from app.services.llm import generate_llm_explanation

from app.core.safety import apply_safety_guardrails

router = APIRouter()


# place holder for "from app.services.llm import generate_llm_explanation"


@router.post("/diagnose", response_model=DiagnosisResponse)
def diagnose(request: DiagnosisRequest):

    # Step 1 — deterministic triage
    triage_result = analyze_triage(request.symptoms)

    # Step 2 — LLM explanation
    llm_explanation = generate_llm_explanation(
        request.symptoms,
        triage_result["triage_level"]
    )

    triage_result["llm_explanation"] = llm_explanation

    # Step 3 — safety guardrails
    safe_response = apply_safety_guardrails(triage_result)

    return DiagnosisResponse(**safe_response)
