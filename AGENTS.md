# FMDA Agent Instructions

This repository contains a safety-aware AI-assisted medical triage prototype.

Agents working in this repository should prioritize:
- deterministic behavior
- safety-aware outputs
- modular architecture
- evaluation consistency
- explainability

---

# Repository Priorities

1. Safety
2. Deterministic triage
3. Maintainability
4. Evaluation coverage
5. Readability
6. Modularity

---

# Development Rules

- Do not introduce direct medication prescription behavior.
- Do not generate dosage logic.
- Avoid bypassing safety guardrails.
- Avoid tightly coupling business logic and LLM outputs.
- Prefer explicit deterministic logic for risk escalation.

---

# Evaluation Workflow

Run evaluations after modifying triage behavior:

```bash
python -m app.evals.eval_runner
```

Expected:
- deterministic results
- stable outputs
- reproducible evaluation behavior

---

# Architecture Notes

FMDA intentionally separates:
- triage logic
- LLM reasoning
- safety enforcement

This separation is a core architectural principle.

---

# Code Style

- Prefer simple readable Python.
- Keep functions focused.
- Use descriptive naming.
- Preserve modular boundaries.
- Avoid unnecessary frameworks.

---

# Documentation

Important docs:
- README.md
- docs/architecture.md
- docs/safety_design.md
