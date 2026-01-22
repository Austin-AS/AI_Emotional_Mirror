import nltk
from collections import Counter


def generate_summary(sentences, max_sentences=2):
    """
    Generates a neutral extractive summary from a list of sentences.
    """

    # If text is already short, return it as-is
    if len(sentences) <= max_sentences:
        return " ".join(sentences)

    # Tokenize words and calculate word frequency
    words = []
    for sentence in sentences:
        words.extend(nltk.word_tokenize(sentence.lower()))

    word_frequencies = Counter(words)

    # Score sentences based on word frequency
    sentence_scores = {}
    for sentence in sentences:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in word_frequencies:
                sentence_scores[sentence] = sentence_scores.get(sentence, 0) + word_frequencies[word]

    # Select top sentences
    top_sentences = sorted(
        sentence_scores,
        key=sentence_scores.get,
        reverse=True
    )[:max_sentences]

    return " ".join(top_sentences)
