import requests
import json
import pandas as pd

def emotion_detector(text_to_analyze):
    url ='https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    input_json = { "raw_document": { "text": text_to_analyze } }
    #Colleting data 
    response = requests.post(url, json=input_json, headers=header).json()
    emotions = response['emotionPredictions'][0]['emotion']
    #treatment
    data = {
        'anger': emotions['anger'],
        'disgust': emotions['disgust'],
        'fear': emotions['fear'],
        'joy': emotions['joy'],
        'sadness': emotions['sadness']
    }

    max_emotion = max(data, key=data.get)
    data['dominant_emotion'] = max_emotion
    return data

if __name__ == "__main__":
#  text = "I am so happy today"
#   print(emotion_detector(text))
   
#   text = "Hmm... Sorry"
#   print(emotion_detector(text))
    text="I love this new technology."
    print(f"Prompt: "+text)
    print("*"*50)
    print(emotion_detector(text))