
import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    headers = {
        "grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"
    }

    payload = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, headers = headers, data = json.dumps(payload))

    if response.status_code == 200:
        emotions = response.json().get("emotionPredictions",[])[0].get("emotion", {})

        required_emotions = { 
            'anger': emotions.get('anger', 0),
            'disgust': emotions.get('disgust', 0),
            'fear': emotions.get('fear', 0),
            'joy': emotions.get('joy', 0),
            'sadness': emotions.get('sadness', 0)
        }

        dominant_emotion = max(required_emotions, key=emotions.get)
        
        required_emotions['dominant_emotion'] = dominant_emotion
    
        return required_emotions
    else:
        return f"Error: {response.status_code}, {response.text}"

