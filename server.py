from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector", methods=["POST"])
def emotion_detection():
    input_text = request.json.get("text", "")

    # Get the result from emotion_detector
    result = emotion_detector(input_text)

    # Handle empty/invalid input
    if result["dominant_emotion"] is None:
        return jsonify({"emotion_result": "Invalid text! Please try again!"})

    # Otherwise, format and return the result
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
