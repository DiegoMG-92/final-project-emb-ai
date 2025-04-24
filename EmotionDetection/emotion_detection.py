# Import the Hugging Face pipeline function, which simplifies using pre-trained models
from transformers import pipeline

# Load the emotion detection pipeline using a pre-trained model from Hugging Face
# - "text-classification" tells the pipeline what kind of task we're doing
# - The specific model used is fine-tuned for detecting emotions in English
# - top_k=None returns a list of scores for all possible emotions, not just the top one
emotion_pipeline = pipeline(
    "text-classification",
    model="j-hartmann/emotion-english-distilroberta-base",
    top_k=None
)

# Define a function that takes a piece of text and returns emotion scores
def emotion_detector(text_to_analyze):
    # Pass the input text to the emotion pipeline
    # It returns a list of dictionaries with 'label' (emotion name) and 'score' (confidence)
    # The [0] accesses the first item in the outer list because top_k=None returns a nested list
    result = emotion_pipeline(text_to_analyze)[0]

    # Convert the list of emotion scores into a dictionary:
    # - Lowercase the emotion labels to match the format we want (e.g., "Joy" → "joy")
    # - Round scores to 3 decimal places for readability
    emotions = {
        item['label'].lower(): round(item['score'], 3)
        for item in result
    }

    # Create a list of the target emotions we want to report in the final result
    target_emotions = ['anger', 'disgust', 'fear', 'joy', 'sadness']

    # Extract only the target emotions from the full emotion list
    # - If an emotion isn't found (very low confidence), default to 0.0
    formatted_emotions = {
        emotion: emotions.get(emotion, 0.0)
        for emotion in target_emotions
    }

    # Find the emotion with the highest score — this is the "dominant" emotion
    dominant_emotion = max(formatted_emotions, key=formatted_emotions.get)

    # Add the dominant emotion to the final dictionary
    formatted_emotions['dominant_emotion'] = dominant_emotion

    # Return the complete result: scores for each emotion and the most dominant one
    return formatted_emotions