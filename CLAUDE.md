# FMDA Claude Code Instructions

FMDA is a safety-aware AI-assisted family medicine triage prototype.

The project prioritizes:
- deterministic triage logic
- layered safety architecture
- explainability
- modularity
- evaluation-driven development

---

# Engineering Principles

- Keep architecture modular.
- Preserve separation between:
  - deterministic triage
  - LLM reasoning
  - safety enforcement
- Avoid tightly coupling API, logic, and model layers.
- Prefer explicit and readable code over abstraction-heavy patterns.
- Prioritize maintainability over premature optimization.

---

# Safety Constraints

The system must NOT:
- prescribe medication
- provide dosage instructions
- claim medical certainty
- replace licensed medical professionals

Emergency escalation logic should remain deterministic whenever possible.

---

# Preferred Development Style

- Use typed Pydantic models.
- Keep functions small and testable.
- Avoid hidden side effects.
- Add evaluation coverage for new triage behavior.
- Maintain readable architecture.

---

# Evaluation Expectations

When changing triage logic:
- update evaluation cases
- run:
  python -m app.evals.eval_runner

Do not modify evaluation expectations without explanation.

---

# Repository Structure

- `app/api/` → API endpoints
- `app/services/` → business logic
- `app/core/` → safety + config
- `app/evals/` → evaluation framework
- `docs/` → architecture + safety docs

---

# Important Design Philosophy

FMDA is NOT a chatbot project.

It is:
- an AI systems engineering project
- a deterministic + LLM hybrid architecture
- a safety-oriented medical AI exploration
