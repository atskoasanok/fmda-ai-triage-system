from typing import Dict


PROHIBITED_TERMS = [
    "take 500mg",
    "prescribe",
    "dosage",
    "opioid",
    "antibiotic prescription"
]


def apply_safety_guardrails(response: Dict) -> Dict:
    """
    Apply safety checks and disclaimers to FMDA responses.
    """

    llm_text = response.get("llm_explanation", "").lower()

    # Block unsafe medical instructions
    for term in PROHIBITED_TERMS:
        if term in llm_text:
            response["llm_explanation"] = (
                "⚠️ Medical prescription or dosage guidance is not supported. "
                "Please consult a licensed healthcare professional."
            )

    # Force emergency escalation notice
    if response.get("triage_level") == "EMERGENCY":
        response["safety_notice"] = (
            "This may represent a medical emergency. "
            "Seek immediate medical attention."
        )

    else:
        response["safety_notice"] = (
            "FMDA is an AI-assisted educational system and not a licensed medical provider."
        )

    return response
