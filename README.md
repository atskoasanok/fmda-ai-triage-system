# FMDA — Family Medicine Doctor Assistant

FMDA is a safety-aware LLM-assisted family medicine triage prototype designed to explore how hybrid AI system architectures and large language models can work together in healthcare-oriented decision support systems.

The project emphasizes:
- explainable AI workflows
- safety guardrails
- structured API outputs
- modular AI system architecture
- human-in-the-loop medical guidance

---

# Key Features

## Deterministic Triage Engine
Deterministic rule-based triage classification:
- EMERGENCY
- URGENT_CARE
- PRIMARY_CARE
- SELF_CARE
- UNCERTAIN

## LLM-Assisted Reasoning
Uses OpenAI models to generate:
- symptom explanations
- safety-conscious guidance
- follow-up recommendations

## Safety Guardrails
The system explicitly avoids:
- medication prescriptions
- dosage recommendations
- overconfident diagnosis
- replacement of licensed medical professionals

## Structured API Responses
FMDA returns typed and testable JSON responses using Pydantic models.

---

# Architecture

```text
Request
↓
Triage Engine
↓
LLM Reasoning Layer
↓
Safety Guardrails
↓
Structured Response
```
---

# Project Structure

```text
fmda/
├── app/
│   ├── api/
│   ├── core/
│   ├── evals/
│   ├── models/
│   └── services/
├── docs/
├── tests/
├── .env.example
├── README.md
└── run_eval.sh
```

Key directories:

- `api/` → FastAPI endpoints
- `services/` → business logic and LLM integration
- `core/` → configuration and safety controls
- `evals/` → evaluation framework
- `models/` → request/response schemas
- `docs/` → architecture and safety documentation

---

# Tech Stack

- Python
- FastAPI
- OpenAI API
- Pydantic
- Uvicorn

---

# Development Setup

All commands below should be executed from the project root directory:

```bash
cd fmda
```

---

## Clone Repository

```bash
git clone <your_repo_url>
cd fmda
```
---

## Create Virtual Environment

If `uv` is not installed:

```bash
brew install uv
```

Using uv:

```bash
uv venv
source .venv/bin/activate
```

---

## Install Dependencies

```bash
uv pip install fastapi uvicorn openai python-dotenv pydantic
```

---

## Configure Environment Variables

Copy the example configuration:

```bash
cp .env.example .env
```

Then update the `.env` file:

```env
OPENAI_API_KEY=your_api_key_here

USE_MOCK=false

MODEL_NAME=gpt-4o

TEMPERATURE=0.5
```

---

## Running the API

Start the FastAPI development server:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

---

## Health Check

```bash
curl http://127.0.0.1:8000/health
```

Expected response:

```json
{
  "status": "ok"
}
```

---

## Running Evaluations

FMDA includes a deterministic evaluation framework for validating triage logic.

Run evaluations from the project root directory:

```bash
python -m app.evals.eval_runner
```

or use the helper script:

```bash
./run_eval.sh
```

Example evaluation output:

```text
==================================================
INPUT: chest pain and shortness of breath
EXPECTED: EMERGENCY
PREDICTED: EMERGENCY
RESULT: PASS
==================================================
FINAL ACCURACY: 100.00%
```

---

## Python Package Execution Notes

FMDA uses package-aware imports such as:

```python
from app.services.triage import analyze_triage
```

Therefore evaluation modules should be executed using:

```bash
python -m app.evals.eval_runner
```

instead of:

```bash
python app/evals/eval_runner.py
```

to ensure proper package resolution and consistent execution behavior.

---

## Mock vs Real LLM Mode

FMDA supports both mock mode and real LLM inference.

### Mock Mode

Useful for:
- local development
- testing
- CI pipelines
- avoiding API costs

```env
USE_MOCK=true
```

---

### Real LLM Mode

Uses OpenAI APIs for live inference:

```env
USE_MOCK=false
```

The active model and temperature are controlled through:

```env
MODEL_NAME=gpt-4o
TEMPERATURE=0.5
```

---

# Example API Request

```bash
curl -X POST http://127.0.0.1:8000/diagnose \
-H "Content-Type: application/json" \
-d '{"symptoms":"fever and cough"}'
```

---

# Example Response

```json
{
  "triage_level": "PRIMARY_CARE",
  "risk_flags": [],
  "possible_conditions": [
    "Common viral illness"
  ],
  "recommendation": "Schedule a clinic visit if symptoms persist.",
  "llm_explanation": "...",
  "safety_notice": "FMDA is an AI-assisted educational system and not a licensed medical provider."
}
```

---

# Goals

FMDA is intended as:
- an applied AI systems learning project
- a healthcare-oriented AI architecture prototype
- an exploration of safe LLM integration patterns

The project is NOT intended to provide real medical diagnosis or treatment.

---

# Future Roadmap

- evaluation framework
- confidence scoring
- memory/context handling
- provider abstraction
- retrieval-augmented medical references
- web UI
- multi-agent orchestration

---

# Disclaimer

FMDA is an educational prototype only and is NOT a licensed medical system.
Always consult qualified healthcare professionals for medical advice.
