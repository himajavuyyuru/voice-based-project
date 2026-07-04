import streamlit as st
from speech_to_text import speech_to_text
from semantic_eval import evaluate_concept
from scoring_engine import calculate_score
from report_generator import generate_report

st.set_page_config(
    page_title="Voice Based Concept Understanding Analyzer",
    page_icon="🎤",
    layout="centered"
)

st.title("🎤 Voice Based Concept Understanding Analyzer")

# --------------------------
# Session State
# --------------------------
if "transcript" not in st.session_state:
    st.session_state.transcript = ""

if "concept_score" not in st.session_state:
    st.session_state.concept_score = 0

if "feedback" not in st.session_state:
    st.session_state.feedback = ""

if "analyzed" not in st.session_state:
    st.session_state.analyzed = False


# --------------------------
# Upload Audio
# --------------------------
uploaded_file = st.file_uploader(
    "Upload an Audio File",
    type=["wav", "mp3", "m4a"]
)

col1, col2 = st.columns(2)

# --------------------------
# Analyze Button
# --------------------------
with col1:
    if st.button("Analyze Concept"):

        if uploaded_file is None:
            st.warning("Please upload an audio file.")
            st.stop()

        try:
            with st.spinner("Analyzing audio..."):

                transcript = speech_to_text(uploaded_file)

                feedback = evaluate_concept(transcript)

                score = calculate_score(feedback)

                st.session_state.transcript = transcript
                st.session_state.feedback = feedback
                st.session_state.concept_score = score
                st.session_state.analyzed = True

        except Exception as e:
            st.error(f"Error: {e}")


# --------------------------
# Clear Button
# --------------------------
with col2:
    if st.button("Clear"):

        st.session_state.transcript = ""
        st.session_state.feedback = ""
        st.session_state.concept_score = 0
        st.session_state.analyzed = False

        st.rerun()


# --------------------------
# Display Results
# --------------------------
if st.session_state.analyzed:

    st.success("Analysis Completed")

    st.subheader("Transcript")
    st.write(st.session_state.transcript)

    st.subheader("Concept Evaluation")
    st.write(st.session_state.feedback)

    st.subheader("Score")
    st.progress(st.session_state.concept_score / 100)
    st.write(f"{st.session_state.concept_score}/100")

    if st.button("Generate Report"):
        report = generate_report(
            st.session_state.transcript,
            st.session_state.feedback,
            st.session_state.concept_score
        )

        st.download_button(
            "Download Report",
            report,
            file_name="concept_report.txt"
        )