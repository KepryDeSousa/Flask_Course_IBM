"""
Emotion Detector Application using Flask.

This module sets up a web application that analyzes emotions
from text input using the EmotionDetection library.
"""

from flask import Flask, request, render_template
from EmotionDetection.emotion_detector import emotion_detector

app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emotion_analyzer():
    """
    Analyze the text input and return the detected emotions.

    Retrieves the text input from the request arguments, passes it to the emotion detector,
    and returns the detected emotions along with the dominant emotion. If the text is empty
    or the dominant emotion is None, an error message is returned.

    Returns:
        str: A response string with emotion values or an error message.
    """
    text_to_analyse = request.args.get('textToAnalyze')
    if not text_to_analyse or not text_to_analyse.strip():
        return "Invalid text! Please try again"
    
    emotion_result = emotion_detector(text_to_analyse)
    dominant_emotion = emotion_result.get('dominant_emotion')

    if not dominant_emotion:
        return "Invalid text! Please try again"

    response_str = (f"For the given statement, the system response is "
                    f"'anger': {emotion_result['anger']}, 'disgust': {emotion_result['disgust']}, "
                    f"'fear': {emotion_result['fear']}, 'joy': {emotion_result['joy']}, "
                    f"'sadness': {emotion_result['sadness']}. "
                    f"The dominant emotion is <strong>{dominant_emotion}</strong>.")
    
    return response_str

@app.route("/")
def render_index_page():
    """
    Render the index page for the Emotion Detector application.

    This function loads and returns the main HTML page for the application.
    
    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5500)
