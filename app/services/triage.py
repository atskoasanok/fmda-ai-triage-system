from typing import Dict, List


EMERGENCY_KEYWORDS = [
    "chest pain",
    "shortness of breath",
    "unconscious",
    "stroke",
    "severe bleeding",
    "chest tightness",
]

URGENT_KEYWORDS = [
    "high fever",
    "persistent vomiting",
    "dehydration"
]

PRIMARY_CARE_KEYWORDS = [
    "fever",
    "cough",
    "headache",
    "fatigue"
]


def analyze_triage(symptoms: str) -> Dict:
    symptoms_lower = symptoms.lower()

    risk_flags: List[str] = []
    possible_conditions: List[str] = []

    # Emergency
    for keyword in EMERGENCY_KEYWORDS:
        if keyword in symptoms_lower:
            risk_flags.append(keyword)

            return {
                "triage_level": "EMERGENCY",
                "risk_flags": risk_flags,
                "possible_conditions": ["Critical condition"],
                "recommendation": "Seek emergency medical attention immediately."
            }

    # Urgent care
    for keyword in URGENT_KEYWORDS:
        if keyword in symptoms_lower:
            risk_flags.append(keyword)

            return {
                "triage_level": "URGENT_CARE",
                "risk_flags": risk_flags,
                "possible_conditions": ["Acute illness"],
                "recommendation": "Visit urgent care within 24 hours."
            }

    # Primary care
    for keyword in PRIMARY_CARE_KEYWORDS:
        if keyword in symptoms_lower:
            possible_conditions.append("Common viral illness")

            return {
                "triage_level": "PRIMARY_CARE",
                "risk_flags": [],
                "possible_conditions": possible_conditions,
                "recommendation": "Schedule a clinic visit if symptoms persist."
            }

    return {
        "triage_level": "UNCERTAIN",
        "risk_flags": [],
        "possible_conditions": [],
        "recommendation": "Insufficient information. Consult a healthcare professional."
    }
