from transformers import pipeline


# Load emotion classification pipeline once
emotion_classifier = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    return_all_scores=True
)


def detect_emotions(text, threshold=0.1):
    """
    Detects primary and secondary emotions from text.
    """
    results = emotion_classifier(text)[0]

    # Sort emotions by confidence score (descending)
    sorted_emotions = sorted(results, key=lambda x: x['score'], reverse=True)

    primary_emotion = sorted_emotions[0]

    secondary_emotion = None

    # Decide secondary emotion based on confidence difference
    if len(sorted_emotions) > 1:
        diff = primary_emotion['score'] - sorted_emotions[1]['score']
        if diff < threshold:
            secondary_emotion = sorted_emotions[1]

    return primary_emotion, secondary_emotion
