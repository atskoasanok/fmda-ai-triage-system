import pytest
from app.core.safety import apply_safety_guardrails


def _make_response(triage_level: str, llm_explanation: str = "") -> dict:
    return {
        "triage_level": triage_level,
        "llm_explanation": llm_explanation,
    }


def test_emergency_sets_safety_notice():
    response = _make_response("EMERGENCY")
    result = apply_safety_guardrails(response)
    assert "emergency" in result["safety_notice"].lower()


def test_non_emergency_sets_fmda_disclaimer():
    response = _make_response("PRIMARY_CARE")
    result = apply_safety_guardrails(response)
    assert "FMDA" in result["safety_notice"]


def test_prohibited_term_is_blocked():
    response = _make_response("PRIMARY_CARE", "You should prescribe amoxicillin.")
    result = apply_safety_guardrails(response)
    assert "prescribe" not in result["llm_explanation"].lower()
    assert "not supported" in result["llm_explanation"]


def test_dosage_instruction_is_blocked():
    response = _make_response("PRIMARY_CARE", "The dosage is 500mg twice daily.")
    result = apply_safety_guardrails(response)
    assert "not supported" in result["llm_explanation"]


def test_opioid_mention_is_blocked():
    response = _make_response("URGENT_CARE", "Consider opioid pain management.")
    result = apply_safety_guardrails(response)
    assert "not supported" in result["llm_explanation"]


def test_safe_explanation_is_preserved():
    safe_text = "Drink plenty of fluids and rest."
    response = _make_response("PRIMARY_CARE", safe_text)
    result = apply_safety_guardrails(response)
    assert result["llm_explanation"] == safe_text


def test_multiple_prohibited_terms_blocked_once():
    """Ensure the loop breaks after the first violation (no duplicate overwrites)."""
    response = _make_response("PRIMARY_CARE", "prescribe dosage opioid")
    result = apply_safety_guardrails(response)
    assert result["llm_explanation"].count("not supported") == 1
