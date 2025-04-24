"""server.py

This Flask application serves a web interface for detecting emotions from text
using a pre-trained NLP model. It renders an HTML frontend and provides
an API endpoint for emotion analysis.
"""

from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    """
    Render the homepage with the input form (index.html).
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detection():
    """
    Handle emotion analysis request.
    Expects JSON with a 'text' field and returns a formatted string with
    emotion scores and dominant emotion. Handles blank input gracefully.
    """
    input_text = request.json.get("text", "")

    result = emotion_detector(input_text)

    if result["dominant_emotion"] is None:
        return jsonify({"emotion_result": "Invalid text! Please try again!"})

    response_text = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

    return jsonify({"emotion_result": response_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
