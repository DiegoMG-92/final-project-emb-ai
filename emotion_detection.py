from transformers import pipeline

# Load the emotion detection model
emotion_pipeline = pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=None)

def emotion_detector(text_to_analyze):
    # Get the list of emotion predictions (wrapped in another list)
    result = emotion_pipeline(text_to_analyze)[0]  # Take the first result list

    # Convert list of {'label': ..., 'score': ...} into a flat dictionary
    emotions = {item['label']: round(item['score'], 3) for item in result}

    return {
        "emotionPredictions": [
            {
                "emotion": emotions
            }
        ]
    }