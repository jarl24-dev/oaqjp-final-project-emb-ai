import requests  # Import the requests library to handle HTTP requests
import json

def emotion_detector(text_to_analyse):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    myobj = { "raw_document": { "text": text_to_analyse } }
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    response = requests.post(url, json = myobj, headers=header) 

    extracted_emotions = {}

    if response.status_code == 400:
        extracted_emotions["anger"] = None
        extracted_emotions["disgust"] = None
        extracted_emotions["fear"] = None
        extracted_emotions["joy"] = None
        extracted_emotions["sadness"] = None
        extracted_emotions["dominant_emotion"] = None
    else:
        # Parsing the JSON response from the API
        formatted_response = json.loads(response.text)
        extracted_emotions = formatted_response["emotionPredictions"][0]["emotion"]
        extracted_emotions["dominant_emotion"] = max(extracted_emotions, key=extracted_emotions.get)

    return extracted_emotions  # Return the response text from the API
