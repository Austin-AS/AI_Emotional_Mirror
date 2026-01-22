import re
import nltk
import spacy

# Load spaCy English model once
nlp = spacy.load("en_core_web_sm")


def clean_text(text):
    """
    Cleans user input text by removing extra spaces and unwanted characters.
    """
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)

    # Strip leading and trailing spaces
    text = text.strip()

    return text


def split_sentences(text):
    """
    Splits cleaned text into sentences.
    """
    sentences = nltk.sent_tokenize(text)
    return sentences
