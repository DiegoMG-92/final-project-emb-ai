from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

# Route for the home page with the form (index.html)
@app.route("/")
def index():
    return render_template("index.html")

# Route to handle emotion detection request
@app.route("/emotionDetector", methods=["GET", "POST"])
def emotion_detection():
    # Get the input statement from the form
    input_text = request.json.get("text", "")
    
    if not input_text:
        return jsonify({"error": "No text provided"}), 400

    # Get emotion analysis result
    result = emotion_detector(input_text)

    # Format the output for display
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
