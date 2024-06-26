import requests

API_URL = "https://api-inference.huggingface.co/models/mistralai/Mistral-7B-Instruct-v0.2"
headers = {"Authorization": "Bearer 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"}



def get_response(text):
    payload = {
        "inputs":text
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    json_resp = response.json()
    return json_resp[0]["generated_text"]




if __name__ == "__main__":
    print( get_response("where is pyramids of giza") )