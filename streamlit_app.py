import streamlit as st
import requests

st.title("FMDA — Family Medicine Doctor Assistant")

st.write(
    "Safety-aware AI-assisted medical triage prototype"
)

symptoms = st.text_area(
    "Describe symptoms",
    height=150
)

if st.button("Analyze Symptoms"):

    response = requests.post(
        "http://127.0.0.1:8000/diagnose",
        json={
            "symptoms": symptoms
        }
    )

    result = response.json()

    st.subheader("Triage Level")
    st.write(result["triage_level"])

    st.subheader("Recommendation")
    st.write(result["recommendation"])

    st.subheader("LLM Explanation")
    st.write(result["llm_explanation"])

    st.subheader("Safety Notice")
    st.warning(result["safety_notice"])
