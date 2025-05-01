"""
import required modules for using the Watson NLP library url to analyse 
the emotion of the user input text
"""
import requests,json

#function definition
def emotion_detector(text_to_analyze):
    """
    This function accepts the user in imput as text_to_analyze and
    returns the value in text attribute of the response from the Watson url
    """
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    jsonobj = {"raw_document": {"text": text_to_analyze}}
    return_value = {}
    """ Error Handling - Implementing to handle the 500 server error """
    try:
        response = requests.post(url, json=jsonobj, headers=header)
        formatted_response = json.loads(response.text)
        
        ## dictionary to save the required output
        return_value = formatted_response['emotionPredictions'][0]['emotion']

        ## Finding the value of the dominant emotion
        dominant_emotion_value = max(return_value.values())

        if response.status_code == 200:
            ## Identfying the emotion which is dominant
            for key in return_value.keys():
                if return_value[key] == dominant_emotion_value:
                    return_value['dominant_emotion'] = key
                    break
        elif response.status_code == 400:
            for key in return_value.keys():
                return_value[key] = None
            return_value['dominant_emotion'] = None

        return return_value
    except KeyError as e:# this is the error while user leaves the text box blank
        return_value['dominant_emotion'] = None
        return return_value 
    #endoffunction
