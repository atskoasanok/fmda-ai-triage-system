# FMDA Architecture

FMDA follows a layered AI system architecture designed to separate deterministic medical triage logic, probabilistic LLM reasoning, and safety enforcement.

The architecture emphasizes:
- explainability
- modularity
- controllability
- safety-oriented AI integration
- deterministic evaluation

---

# High-Level System Flow

```text
Client Request
↓
FastAPI Endpoint
↓
Deterministic Triage Engine
↓
LLM Reasoning Layer
↓
Safety Guardrails
↓
Structured JSON Response
```

---

# Architectural Principles

## 1. Deterministic Safety-Critical Logic

Medical risk escalation should not rely entirely on probabilistic language model behavior.

FMDA therefore separates:
- deterministic triage classification
from
- natural language reasoning generation

Emergency escalation logic is implemented through explicit rule-based logic.

---

## 2. Layered AI System Design

The system separates responsibilities across multiple layers:

| Layer | Responsibility |
|---|---|
| API Layer | request orchestration |
| Triage Layer | deterministic classification |
| LLM Layer | explanation generation |
| Safety Layer | policy enforcement |
| Evaluation Layer | measurable validation |

This separation improves:
- maintainability
- observability
- testability
- safety control

---

# Core Components

## API Layer

Location:

```text
app/api/
```

Responsibilities:
- request handling
- orchestration
- response formatting

Primary endpoint:

```text
POST /diagnose
```

---

## Triage Engine

Location:

```text
app/services/triage.py
```

Responsibilities:
- deterministic symptom classification
- risk escalation
- triage categorization

Current triage levels:
- EMERGENCY
- URGENT_CARE
- PRIMARY_CARE
- SELF_CARE
- UNCERTAIN

The triage engine is intentionally deterministic for predictable behavior.

---

## LLM Reasoning Layer

Location:

```text
app/services/llm.py
```

Responsibilities:
- natural language explanations
- contextual symptom guidance
- safety-oriented recommendations

The LLM layer does NOT directly determine emergency severity.

This design reduces over-reliance on probabilistic model behavior for safety-critical decisions.

---

## Safety Layer

Location:

```text
app/core/safety.py
```

Responsibilities:
- prohibited medical guidance filtering
- dosage prevention
- emergency escalation notices
- disclaimer enforcement

The safety layer acts as a post-processing control boundary.

---

## Configuration Layer

Location:

```text
app/core/config.py
```

Responsibilities:
- environment configuration
- model selection
- mock vs real inference switching
- runtime parameter management

The architecture supports:
- local testing
- reproducible environments
- provider abstraction

---

## Evaluation Framework

Location:

```text
app/evals/
```

Responsibilities:
- deterministic test execution
- regression testing
- triage accuracy validation

Example evaluation flow:

```text
input symptoms
↓
expected triage
↓
predicted triage
↓
pass/fail scoring
```

The evaluation framework is intentionally focused on deterministic logic rather than unstable free-form LLM outputs.

---

# Design Decisions

## Why Deterministic Triage?

Pure LLM-based diagnosis systems may:
- hallucinate
- behave inconsistently
- vary between runs

FMDA therefore uses:
- deterministic triage logic
for safety-critical classification.

---

## Why Separate LLM Reasoning?

LLMs are useful for:
- explanation
- summarization
- communication

but less reliable for:
- strict medical risk escalation
- deterministic policy enforcement

FMDA therefore constrains the LLM role primarily to explanatory support.

---

## Why Safety Guardrails?

Healthcare-oriented AI systems require:
- bounded behavior
- escalation logic
- explicit disclaimers
- constrained outputs

FMDA uses layered safety controls to reduce unsafe behavior risk.

---

# Current Limitations

FMDA is currently:
- a prototype system
- not medically validated
- not clinically deployed
- not connected to medical databases
- not intended for real-world diagnosis

The current system uses simplified deterministic rules and general-purpose language models.

---

# Future Enhancements

Potential future improvements include:
- confidence scoring
- retrieval-augmented medical references
- longitudinal memory
- provider abstraction
- clinician review workflows
- structured medical ontologies
- web-based UI
- multi-agent orchestration

---

# Summary

FMDA is designed as:
- an AI systems engineering project
- a safety-aware LLM integration prototype
- a deterministic + probabilistic hybrid architecture exploration

The project intentionally prioritizes:
- controllability
- modularity
- explainability
- evaluation
- safety-oriented design
