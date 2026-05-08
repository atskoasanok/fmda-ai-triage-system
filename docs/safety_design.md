# FMDA Safety Design

FMDA is designed as a safety-aware AI-assisted family medicine triage prototype.

The system intentionally separates:
- deterministic medical triage logic
- probabilistic language model reasoning
- safety enforcement controls

to reduce unsafe or unpredictable behavior.

---

# Safety Philosophy

FMDA is NOT intended to:
- replace licensed healthcare professionals
- provide definitive diagnosis
- prescribe medication
- provide dosage instructions
- autonomously determine treatment plans

Instead, FMDA is designed to:
- assist with preliminary triage reasoning
- provide educational guidance
- encourage appropriate medical follow-up
- escalate high-risk symptoms conservatively

The project prioritizes:
- bounded AI behavior
- deterministic escalation
- explicit uncertainty
- human oversight

---

# Layered Safety Architecture

FMDA uses multiple safety layers rather than relying entirely on model prompting.

```text
Input Symptoms
↓
Deterministic Triage Logic
↓
LLM Explanation Generation
↓
Safety Guardrails
↓
Structured Response
```

This layered design improves:
- predictability
- controllability
- explainability
- failure isolation

---

# Deterministic Triage Controls

Location:

```text
app/services/triage.py
```

Emergency escalation logic is implemented deterministically.

Examples:
- chest pain
- shortness of breath
- severe bleeding
- stroke-like symptoms

These classifications do NOT depend solely on LLM interpretation.

This reduces:
- hallucination risk
- inconsistent emergency classification
- unsafe variability between model runs

---

# LLM Safety Constraints

Location:

```text
app/services/llm.py
```

The LLM is intentionally constrained through:
- system prompts
- architecture separation
- post-processing controls

The LLM is instructed to avoid:
- medication prescriptions
- dosage recommendations
- diagnostic certainty
- replacement of professional care

The LLM primarily serves:
- explanatory support
- contextual reasoning
- safety-oriented guidance

rather than authoritative medical decision-making.

---

# Safety Guardrails

Location:

```text
app/core/safety.py
```

The safety layer performs:
- prohibited content filtering
- dosage prevention
- disclaimer injection
- emergency escalation messaging

Examples of prohibited behavior:
- prescribing opioids
- recommending dosage quantities
- generating direct prescription instructions

Unsafe outputs are overridden with safety-oriented responses.

---

# Human-in-the-Loop Design

FMDA assumes:
- human oversight is required
- AI outputs may be incomplete
- medical professionals remain authoritative

The system intentionally encourages:
- clinical follow-up
- emergency escalation when appropriate
- conservative interpretation of symptoms

---

# Disclaimer Strategy

FMDA consistently injects explicit disclaimers such as:

```text
FMDA is an AI-assisted educational system and not a licensed medical provider.
```

This helps reinforce:
- system limitations
- uncertainty awareness
- non-authoritative status

---

# Evaluation Strategy

Location:

```text
app/evals/
```

FMDA includes deterministic evaluation cases for:
- triage consistency
- escalation correctness
- regression detection

The current evaluation framework focuses primarily on deterministic logic because:
- free-form LLM outputs are inherently variable
- deterministic behavior is easier to validate
- safety-critical logic requires stability

---

# Known Limitations

FMDA currently:
- is not medically validated
- does not use clinical datasets
- does not integrate medical ontologies
- does not support longitudinal patient history
- does not perform real-world diagnosis

The current triage logic is simplified and educational in nature.

---

# Future Safety Enhancements

Potential future improvements include:
- clinician-reviewed evaluation datasets
- confidence scoring
- retrieval-augmented medical references
- hallucination detection
- model output verification
- audit logging
- structured medical terminology validation
- multi-stage safety review pipelines

---

# Design Rationale

The FMDA architecture intentionally avoids:
- unrestricted autonomous diagnosis
- unconstrained LLM authority
- direct treatment generation

Instead, the project explores:
- hybrid deterministic + probabilistic systems
- layered safety controls
- explainable AI workflows
- bounded medical AI assistance

---

# Summary

FMDA is designed as:
- a safety-oriented AI systems prototype
- a deterministic + LLM hybrid architecture
- an exploration of controllable healthcare AI workflows

The project prioritizes:
- safety
- explainability
- modularity
- evaluation
- human oversight
- constrained AI behavior
