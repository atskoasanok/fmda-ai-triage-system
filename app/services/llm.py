from app.core.config import settings

from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()


client = OpenAI(
    api_key=settings.OPENAI_API_KEY
)

USE_MOCK = settings.USE_MOCK

SYSTEM_PROMPT = """
You are FMDA, a safety-aware family medicine triage assistant.

You do NOT:
- prescribe medications
- provide dosage
- claim certainty
- replace licensed doctors

Your role:
- explain possible situations
- encourage proper medical follow-up
- remain cautious and safety-oriented
"""


def generate_llm_explanation(
    symptoms: str,
    triage_level: str
) -> str:

    # Mock mode for development/testing
    if USE_MOCK:
        return (
            f"Mock FMDA explanation: symptoms '{symptoms}' "
            f"were assessed as {triage_level}. "
            f"Please consult a healthcare professional if symptoms worsen."
        )

    user_prompt = f"""
Symptoms: {symptoms}

Triage Level: {triage_level}

Provide:
1. A brief explanation
2. General guidance
3. A safety-conscious recommendation
"""

    response = client.chat.completions.create(
        model=settings.MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=settings.TEMPERATURE
    )

    return response.choices[0].message.content

# print("MODEL:", settings.MODEL_NAME)
# print("TEMP:", settings.TEMPERATURE)
