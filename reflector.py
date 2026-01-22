from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def generate_reflection(summary, primary_emotion, secondary_emotion=None):
    if not os.getenv("GROQ_API_KEY"):
        return "Reflection unavailable (missing Groq API key)."

    if secondary_emotion:
        emotion_text = f"{primary_emotion} along with {secondary_emotion}"
    else:
        emotion_text = primary_emotion

    prompt = f"""
You are an emotional reflection system.

Rules:
- Reflect emotions, do NOT give advice or solutions
- Do NOT motivate or diagnose
- Avoid words like "should", "try", or "need to"
- Use calm, non-judgmental language
- Limit the response to two short sentences

User summary:
{summary}

Detected emotions:
{emotion_text}

Reflection:
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": "You are a calm emotional reflection system."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.4,
            max_tokens=80
        )

        return response.choices[0].message.content.strip()

    except Exception as e:
        print("GROQ ERROR:", e)
        return "Reflection temporarily unavailable."
