import streamlit as st

from text_utils import clean_text, split_sentences
from emotion_model import detect_emotions
from summarizer import generate_summary
from reflector import generate_reflection


# Page configuration
st.set_page_config(
    page_title="AI Emotional Mirror",
    layout="centered"
)

# Title
st.title("AI Emotional Mirror")
st.caption("Reflecting emotions, not giving solutions.")

# Input area
user_input = st.text_area(
    "Write freely below:",
    placeholder="You can express your thoughts without worrying about structure or clarity.",
    height=200
)

# Disclaimer
st.markdown(
    "<small><i>This tool provides emotional reflection only and is not a substitute for professional mental health support.</i></small>",
    unsafe_allow_html=True
)

# Button
if st.button("Reflect"):

    if not user_input.strip():
        st.warning("Please write something to reflect on.")
    else:
        # Step 1: Clean text
        cleaned_text = clean_text(user_input)

        # Step 2: Split into sentences
        sentences = split_sentences(cleaned_text)

        # Step 3: Generate summary
        summary = generate_summary(sentences)

        # Step 4: Detect emotions
        primary, secondary = detect_emotions(cleaned_text)

        # Step 5: Generate reflection
        reflection = generate_reflection(
            summary,
            primary["label"],
            secondary["label"] if secondary else None
        )

        # Output section
        st.markdown("---")

        st.subheader("Summary")
        st.write(summary)

        st.subheader("Detected Emotions")
        st.write(f"**Primary:** {primary['label'].capitalize()}")
        if secondary:
            st.write(f"**Secondary:** {secondary['label'].capitalize()}")

        st.subheader("Reflection")
        st.write(reflection)
