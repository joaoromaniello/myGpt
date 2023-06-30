import openai
import requests
import json

import variables

API_ENDPOINT = "https://api.openai.com/v1/chat/completions"

API_KEY = variables.API_KEY
openai.api_key = variables.API_KEY


def generate_chat_completion(messages, model="gpt-3.5-turbo", temperature=0, max_tokens=None):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {API_KEY}",
    }

    data = {
        "model": model,
        "messages": messages,
        "temperature": temperature,
    }

    if max_tokens is not None:
        data["max_tokens"] = max_tokens

    response = requests.post(API_ENDPOINT, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Error {response.status_code}: {response.text}")


def main():
    messages = [
        {"role": "system",
         "content": "Você será um robô que me responderá me tratando igual um rei, e minha namorada (milena) como uma rainha. Meu nome é joão antônio.Você me dará apenas informações verdadeiras. NÃO PODE INVENTAR NEM MENTIR"},
        {"role": "user", "content": ""}
    ]

    print("========CHAT GPT========")

    while 1:
        _input = input("USER: ")
        messages[1]["content"] = _input
        response_text = generate_chat_completion(messages)
        print("SYSTEM: " + response_text)


if __name__ == "__main__":
    main()
