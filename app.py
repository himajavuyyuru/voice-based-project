import streamlit as st

from speech_to_text import transcribe_audio
from semantic_eval import calculate_similarity
from scoring_engine import (
    calculate_score,
    classify_understanding
)
from report_generator import generate_pdf

st.title("🎤 Voice Based Concept Understanding Analyser")

reference_text = st.text_area(
    "Enter Reference Concept"
)

uploaded_file = st.file_uploader(
    "Upload Audio",
    type=["wav", "mp3", "m4a"]
)

if uploaded_file and reference_text:

    with open(uploaded_file.name, "wb") as f:
        f.write(uploaded_file.getbuffer())

    transcript = transcribe_audio(uploaded_file.name)

    similarity = calculate_similarity(
        reference_text,
        transcript
    )

    score = calculate_score(similarity)

    classification = classify_understanding(score)

    st.subheader("Transcript")
    st.write(transcript)

    st.subheader("Results")
    st.write(f"Semantic Similarity: {similarity}")
    st.write(f"Understanding Score: {score}%")
    st.write(f"Classification: {classification}")

    if st.button("Generate PDF Report"):
        generate_pdf(
            "report.pdf",
            transcript,
            similarity,
            score,
            classification
        )
        st.success("PDF Report Generated!")