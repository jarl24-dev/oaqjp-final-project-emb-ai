''' Executing this function initiates the application of emotion
    detection to be executed over the Flask channel and deployed on
    localhost:5000.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app :
app = Flask("Emotion Detector")

@app.route("/emotionDetector")
def emot_detection():
    ''' This code receives the text from the HTML interface and
        runs emotion detection over it using emotion_detector()
        function. The output returned shows the different emotions
        and the dominant.
    '''
    # Retrieve the text to analyze from the request arguments
    text_to_analyze = request.args.get('textToAnalyze')
    # Pass the text to the sentiment_analyzer function and store the response
    response = emotion_detector(text_to_analyze)

    if response["dominant_emotion"] is None:
        formatted_response =  "Invalid text! Please try again!"
    else:
        emotions = {k: v for k, v in response.items() if k != "dominant_emotion"}

        emotions_str = ", ".join(
            f"'{k}': {v}" for k, v in emotions.items()
        ).replace(", 'sadness'", " and 'sadness'")

        formatted_response = (
            f"For the given statement, the system response is "
            f"{emotions_str}. "
            f"The dominant emotion is {response['dominant_emotion']}."
        )
    # Return a formatted string with the sentiment label and score
    return formatted_response

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
