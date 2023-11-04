import requests
import pickle

brand_map = {0:"Anger", 1:"Fear", 2:"Joy", 3:"Love",
4:"Sadness", 5:"Surprise"}

def predict_emote(model,txt):
    # url = "http://localhost:5000/api/genvec"
    url = "http://172.17.0.2:5000/api/genvec"
    response = requests.get(url, json={"text_data":txt})
    if response.status_code == 200:
        try:
            response_data = response.json()
            data_list = [response_data[key] for key in response_data]
            emote = model.predict(data_list[0])
            result_brand=brand_map.get(emote[0])

            return result_brand
        except requests.exceptions.JSONDecodeError as e:
            print("JSON Decode Error:", e)
    else:
        print("API Request Error. Status Code:", response.status_code)
        return None