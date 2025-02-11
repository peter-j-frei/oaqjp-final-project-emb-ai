from flask import Flask, request, jsonify, render_template
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/emotionDetector', methods=['POST'])
def emotion_detector_api():
    data = request.json
    text_to_analyze = data.get("text", "").strip()
    
    if not text_to_analyze:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    
    emotions = emotion_detector(text_to_analyze)
    
    if emotions['dominant_emotion'] is None:
        return jsonify({"error": "Invalid text! Please try again!"}), 400
    
    response_text = (
        f"For the given statement, the system response is 'anger': {emotions['anger']}, "
        f"'disgust': {emotions['disgust']}, 'fear': {emotions['fear']}, "
        f"'joy': {emotions['joy']} and 'sadness': {emotions['sadness']}. "
        f"The dominant emotion is {emotions['dominant_emotion']}."
    )
    
    return jsonify({"response": response_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)