# Adversarial Review Response

Review Date: 2026-05-16

## Review Context

Branch: `feature/ui-alert-cards`

Purpose:
Improve Streamlit triage alert visualization.

Reviewer:
Codex adversarial review via Claude Code plugin (`/codex:adversarial-review`, 2026-05-16).
Note: Codex quota exhausted; equivalent adversarial review executed by Claude Code.

---
## Review Outcome Summary

Total Findings: 9

- Accepted: 4
- Deferred: 2
- Lower Priority: 3

Overall Assessment:
The current FMDA architecture remains structurally sound for MVP scope. The highest-priority concerns involve:
- deployment portability
- medical safety fallback directionality
- frontend HTML rendering safety

No critical architectural redesign is currently required.

---
## Accepted Findings

### 1. Hardcoded localhost endpoint

Status: ACCEPTED

Location: `streamlit_app.py:60`

```python
response = requests.post("http://127.0.0.1:8000/diagnose", ...)
```

Rationale:
Blocks deployment portability. Any non-localhost environment (Docker, cloud, CI) fails immediately with no configuration path.

Planned Action:
Move backend URL to environment variable (e.g. `FMDA_BACKEND_URL`).

---

### 2. UNCERTAIN fallback to SELF_CARE

Status: ACCEPTED

Location: `streamlit_app.py:75` / `triage.py:69`

```python
# triage.py — returns when no keyword matches
return {"triage_level": "UNCERTAIN", ...}

# streamlit_app.py — UNCERTAIN has no TRIAGE_CONFIG entry
config = TRIAGE_CONFIG.get(triage_level, TRIAGE_CONFIG["SELF_CARE"])
```

Rationale:
Medical safety directionality concern. An undetermined clinical situation silently renders as a green "Self Care" badge, actively misleading the user.

Planned Action:
Create explicit `UNCERTAIN` UI state with neutral color and advisory message (e.g. "Unable to determine — please consult a healthcare professional").

---

### 3. EMERGENCY collects only first matching risk flag

Status: ACCEPTED

Location: `triage.py:34–43`

```python
for keyword in EMERGENCY_KEYWORDS:
    if keyword in symptoms_lower:
        risk_flags.append(keyword)
        return {  # all remaining emergency keywords discarded
```

Rationale:
If a patient describes multiple emergency symptoms (e.g. "chest pain" and "chest tightness"), only the first matched keyword is captured. This understates clinical severity.

Planned Action:
Accumulate all matched emergency keywords before returning.

---

### 4. `unsafe_allow_html=True` with API response content

Status: ACCEPTED

Location: `streamlit_app.py:103–116`

```python
st.markdown(
    f"...<div...>{result.get('recommendation', '—')}</div>...",
    unsafe_allow_html=True,
)
```

Rationale:
`recommendation` content from the backend is interpolated directly into an HTML template. A prompt injection attack could cause the LLM to emit HTML tags, creating an XSS path.

Planned Action:
HTML-escape `recommendation` before interpolation, or use `st.markdown` without raw HTML wrapping.

---

## Deferred Findings

### Shared frontend/backend enum synchronization

Status: DEFERRED

Rationale:
Good architectural idea but premature for MVP stage. The triage level values (`"EMERGENCY"`, `"URGENT_CARE"`, etc.) are independently defined in both `triage.py` and `TRIAGE_CONFIG`. Centralizing these into a shared enum (e.g. `app/models/triage_level.py`) would eliminate contract drift, but adds refactoring overhead not justified at current scale.

Revisit when: backend adds a new triage level or the frontend is separated into its own deployment unit.

---

### Implicit API contract / no shared response schema

Status: DEFERRED

Rationale:
The frontend accesses all response fields by string key without importing `DiagnosisResponse`. In a single-repo Python project, this is low friction to fix (import the model), but the risk is low while both sides evolve together. Deferred until the Streamlit frontend is treated as a distinct client.

---

## Rejected / Lower Priority Findings

### `USE_MOCK = true` as default

Status: LOWER PRIORITY

Location: `config.py:35`

Rationale:
A deployment concern, but low blast radius — mock mode is obvious in responses and not a silent data corruption. Acceptable for a prototype. Flag in deployment runbook.

---

### Unhandled `Timeout` and `RequestException`

Status: LOWER PRIORITY

Location: `streamlit_app.py:67–72`

Rationale:
`requests.exceptions.Timeout` (triggered after the 30-second timeout) and other `RequestException` subclasses are uncaught. This surfaces an unhandled exception to the user. Acceptable for MVP; can be caught with a single broad `except requests.exceptions.RequestException` clause.

---

### `API_KEY` has no startup validation

Status: LOWER PRIORITY

Location: `config.py:20`

Rationale:
If `USE_MOCK=false` and `API_KEY` is unset, failure is deferred to request time. Acceptable while mock mode is the default. Add a startup assertion before production hardening.

---

### `safety_notice` not guaranteed in all code paths

Status: LOWER PRIORITY

Location: `safety.py` / `streamlit_app.py:128`

Rationale:
`apply_safety_guardrails` sets `safety_notice` in both branches. Risk only materializes if a future code path bypasses the guardrail. Acceptable for now; mitigated by keeping guardrails as the single exit point for all responses.

---

## Human Engineering Notes

This review successfully identified:
- Deployment concerns (hardcoded endpoint, mock-mode default)
- Safety directionality risks (UNCERTAIN → SELF_CARE silent fallback)
- Hidden frontend/backend coupling (implicit string-keyed contract)
- An XSS path introduced by `unsafe_allow_html` with API content

The review also demonstrates the usefulness of adversarial AI review for healthcare-oriented systems, particularly for catching silent fallback behavior that is architecturally correct in general web applications but dangerous in medical triage contexts.

---
## Next Planned Actions

Planned implementation sequence:

1. Externalize backend URL via environment variable
2. Add explicit UNCERTAIN UI state
3. Escape recommendation content before HTML rendering
4. Improve emergency keyword accumulation logic

Deferred items will be revisited during:
- deployment preparation
- frontend/backend separation
- provider-router refactor
