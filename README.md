# AI Emotional Mirror

# Overview

**AI Emotional Mirror** is an AI/ML mini project that helps users gain clarity over messy thoughts by *reflecting* their emotions instead of giving advice or solutions. The system combines NLP preprocessing, transformer-based emotion detection, extractive summarization, and a generative AI reflection module.

> *Therapy often starts with reflection, not solutions.*

This project is designed to be ethical, explainable, and demonstrable with **any user input**.

---

## Problem Statement

People often feel overwhelmed but struggle to articulate *what* they are feeling. Most AI tools rush to give advice, which can feel intrusive or unhelpful. There is a need for a system that:

* Listens without judging
* Names emotions accurately
* Reflects thoughts gently
* Avoids advice, diagnosis, or motivation

---

## Solution

AI Emotional Mirror accepts free-form user input and processes it through a structured pipeline:

1. Clean and normalize text
2. Extract core meaning (summary)
3. Detect dominant and secondary emotions
4. Generate a calm, non-judgmental reflection using GenAI

The output helps users *understand themselves*, not change themselves.

---

## System Architecture

**User Input → Text Cleaning → Sentence Segmentation → Summary → Emotion Detection → Reflection Generation → UI Output**

Each component is modular and independently testable.

---

## Tech Stack

* **Frontend/UI:** Streamlit
* **NLP:** NLTK, spaCy
* **Emotion Detection:** Transformer model (`j-hartmann/emotion-english-distilroberta-base`)
* **Generative AI:** Groq API (LLaMA‑3.1‑8B‑Instant)
* **Language:** Python

---

## Modules Explanation

### `text_utils.py`

* Cleans raw text input
* Handles whitespace and formatting
* Splits text into meaningful sentences

### `summarizer.py`

* Performs extractive summarization using word frequency
* Preserves user language without rewriting
* Helps surface the core concern

### `emotion_model.py`

* Uses a transformer-based classifier
* Detects primary and secondary emotions
* Provides confidence-aware emotion selection

### `reflector.py`

* Uses Groq’s LLaMA‑3.1 model
* Generates reflective responses
* Strictly avoids advice or diagnosis
* Produces 1–2 calm sentences

### `app.py`

* Streamlit interface
* Orchestrates the full pipeline
* Displays summary, emotions, and reflection

---

## Ethical Design Principles

* ❌ No advice or prescriptions
* ❌ No diagnosis
* ❌ No emotional manipulation
* ✅ Reflection-only responses
* ✅ Clear disclaimer
* ✅ User-controlled interaction

---

## Example

**Input:**

> “I feel mentally exhausted and unsure why everything feels heavy lately.”

**Output:**

* Summary: Core concern extracted
* Emotions: Anxiety, Sadness
* Reflection: Calm, validating response

---

## Why This Project Is Unique

* Focuses on *reflection*, not solutions
* Psychology-informed design
* Handles real user input, not canned examples
* Robust to API changes via modular architecture
* Suitable for low-resource systems (laptops)

---

## Future Enhancements

* Conversation history (optional)
* Emotion trend visualization
* Multilingual support
* Voice input

---

## Disclaimer

This project is for educational purposes only and is **not a replacement for professional mental health support**.

---

## Author

**Austin A S**

AI/ML Project

I thank GOD for making this happen
