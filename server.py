''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''

## Import the modules :
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detection Application")

@app.route("/emotionDetector")
def emot_detection():
    """ This method enables users to access the application using the 
    url path /emotionDetector and returns the system response for the 
    user input statement """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    if response['dominant_emotion'] is None:
        return "Invalid text! Please try again."

    return (
        f"For the given statement, the system response is "
        f"'anger': {response['anger']}, "
        f"'disgust': {response['disgust']}, "
        f"'fear': {response['fear']}, "
        f"'joy': {response['joy']}," 
        f"'sadness': {response['sadness']}. The dominant emotion is {response['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """ Calling the index page while loading application """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
