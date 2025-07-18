# editor/utils.py

import requests

def check_grammar(text):
    url = "https://api.languagetoolplus.com/v2/check"

    payload = {
        'text': text,
        'language': 'en-US'
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        return response.json()['matches']
    return []
