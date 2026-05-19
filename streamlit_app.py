# TODO: add triage alert cards

import streamlit as st
import requests

# ── Page config ─────────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="FMDA — Family Medicine Doctor Assistant",
    page_icon="🏥",
    layout="centered",
)

# ── Triage level config ──────────────────────────────────────────────────────────
TRIAGE_CONFIG = {
    "EMERGENCY": {
        "label": "🚨 Emergency",
        "display": st.error,
        "color": "#FF4B4B",
    },
    "URGENT_CARE": {
        "label": "⚠️ Urgent Care",
        "display": st.warning,
        "color": "#FFA500",
    },
    "PRIMARY_CARE": {
        "label": "🏥 Primary Care",
        "display": st.info,
        "color": "#4B9FFF",
    },
    "SELF_CARE": {
        "label": "🌿 Self Care",
        "display": st.success,
        "color": "#2ECC71",
    },
}

# ── Header ───────────────────────────────────────────────────────────────────────
st.title("🏥 FMDA")
st.caption("Family Medicine Doctor Assistant — Safety-aware AI-assisted medical triage prototype")

st.divider()

# ── Input area ───────────────────────────────────────────────────────────────────
symptoms = st.text_area(
    "Describe your symptoms",
    height=160,
    placeholder="e.g. Fever for 3 days, sore throat, headache...",
)

analyze_clicked = st.button("🔍 Analyze Symptoms", type="primary", use_container_width=True)

# ── Results area ─────────────────────────────────────────────────────────────────
import os
from app.core.config import settings

if analyze_clicked:
    if not symptoms.strip():
        st.warning("Please enter your symptoms first.")
        st.stop()

    with st.spinner("Analyzing symptoms, please wait..."):
        try:
            response = requests.post(
                f"{settings.FMDA_BACKEND_URL}/diagnose",
                json={"symptoms": symptoms},
                timeout=30,
            )
            response.raise_for_status()
            result = response.json()
        except requests.exceptions.ConnectionError:
            st.error("Cannot connect to backend. Please ensure the FastAPI server is running on port 8000.")
            st.stop()
        except requests.exceptions.HTTPError as e:
            st.error(f"Backend error: {e}")
            st.stop()

    triage_level = result.get("triage_level", "SELF_CARE")
    config = TRIAGE_CONFIG.get(triage_level, TRIAGE_CONFIG["SELF_CARE"])

    st.divider()

    # ── Triage level (color badge) ───────────────────────────────────────────
    st.subheader("Triage Level")
    config["display"](f"**{config['label']}**")

    st.write("")  # spacing

    # ── Risk flags ───────────────────────────────────────────────────────────
    risk_flags = result.get("risk_flags", [])
    if risk_flags:
        st.subheader("⛳ Risk Flags")
        for flag in risk_flags:
            st.markdown(f"- 🔴 {flag}")
        st.write("")

    # ── Possible conditions ───────────────────────────────────────────────────
    possible_conditions = result.get("possible_conditions", [])
    if possible_conditions:
        st.subheader("🔬 Possible Conditions")
        for condition in possible_conditions:
            st.markdown(f"- {condition}")
        st.write("")

    # ── Recommendation ───────────────────────────────────────────────────────
    st.subheader("📋 Recommendation")
    st.markdown(
        f"""
        <div style="
            background-color: {config['color']}22;
            border-left: 4px solid {config['color']};
            padding: 1rem 1.2rem;
            border-radius: 0.4rem;
            line-height: 1.6;
        ">
        {result.get('recommendation', '—')}
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.write("")

    # ── AI explanation (expandable) ──────────────────────────────────────────
    with st.expander("🤖 AI Explanation (LLM)", expanded=False):
        st.markdown(result.get("llm_explanation", "—"))

    st.write("")

    # ── Safety notice ────────────────────────────────────────────────────────
    st.warning(
        f"⚕️ **Safety Notice**\n\n{result.get('safety_notice', '')}",
        icon="⚕️",
    )
