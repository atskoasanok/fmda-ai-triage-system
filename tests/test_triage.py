import pytest
from app.services.triage import analyze_triage


def test_chest_tightness_is_emergency():
    result = analyze_triage("I have chest tightness")
    assert result["triage_level"] == "EMERGENCY"
    assert "chest tightness" in result["risk_flags"]


def test_chest_tightness_mixed_symptoms_is_emergency():
    result = analyze_triage("chest tightness and mild fatigue")
    assert result["triage_level"] == "EMERGENCY"


def test_chest_pain_is_emergency():
    result = analyze_triage("chest pain")
    assert result["triage_level"] == "EMERGENCY"


def test_shortness_of_breath_is_emergency():
    result = analyze_triage("shortness of breath")
    assert result["triage_level"] == "EMERGENCY"


def test_unconscious_is_emergency():
    result = analyze_triage("patient is unconscious")
    assert result["triage_level"] == "EMERGENCY"


def test_high_fever_is_urgent():
    result = analyze_triage("high fever")
    assert result["triage_level"] == "URGENT_CARE"


def test_fever_and_cough_is_primary_care():
    result = analyze_triage("fever and cough")
    assert result["triage_level"] == "PRIMARY_CARE"


def test_unknown_symptom_is_uncertain():
    result = analyze_triage("I feel slightly off today")
    assert result["triage_level"] == "UNCERTAIN"


def test_emergency_response_structure():
    result = analyze_triage("chest tightness")
    assert "triage_level" in result
    assert "risk_flags" in result
    assert "possible_conditions" in result
    assert "recommendation" in result
    assert result["recommendation"] != ""
