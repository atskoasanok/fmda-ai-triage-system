import os

from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


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

    user_prompt = f"""
Symptoms: {symptoms}

Triage Level: {triage_level}

Provide:
1. A brief explanation
2. General guidance
3. A safety-conscious recommendation
"""

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
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
        temperature=0.3
    )

    return response.choices[0].message.content
