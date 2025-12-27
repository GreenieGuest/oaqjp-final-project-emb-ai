import requests, json, operator # import requests library

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL
    myobj = { "raw_document": { "text": text_to_analyze } }  # Input
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}  # Headers
    response = requests.post(url, json = myobj, headers=header)  # send request to API
    
    formatted_response = json.loads(response.text) # convert to dict
    
    if response.status_code == 400:
        result = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
            'dominant_emotion': None
        }
        return result

    anger_score = formatted_response['emotionPredictions'][0]["emotion"]['anger']
    disgust_score = formatted_response['emotionPredictions'][0]["emotion"]['disgust']
    fear_score = formatted_response['emotionPredictions'][0]["emotion"]['fear']
    joy_score = formatted_response['emotionPredictions'][0]["emotion"]['joy']
    sadness_score = formatted_response['emotionPredictions'][0]["emotion"]['sadness']

    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score
    }
    dominant_emotion = max(result.items(), key=operator.itemgetter(1))[0]
    result["dominant_emotion"] = dominant_emotion

    return result
