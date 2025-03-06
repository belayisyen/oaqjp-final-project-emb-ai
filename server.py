""" This module is the final project """
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask('Emotion Detector')

@app.route("/emotionDetector")

def sent_analyzer():
    """
    This module provides functionality for detecting emotions in text.
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['disgust'] is None:
        return "Invalid text! Please try again!"

    return f"For the given statement, the system response is 'anger': {response['anger']}, " \
        f"'disgust': {response['disgust']}, " \
        f"'fear': {response['fear']}, " \
        f"'joy': {response['joy']}, " \
        f"'sadness': {response['sadness']}. " \
        f"The dominant emotion is {response['dominant_emotion']}."

@app.route("/")
def render_index_page():
    """
    This module renders the home page
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
