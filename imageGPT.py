import openai
import requests
import random

import textGPT
import variables

API_ENDPOINT = "https://api.openai.com/v1/images/generations"

openai.api_key = variables.API_KEY

messages = [
    {"role": "system",
     "content": "Você será um robô capaz de gerar nomes para meus arquivos (imagens) baseado no prompt que eu utilizei para gera-las. Responderá apenas com o nome sem extensão, nada mais"},
    {"role": "user", "content": ""}
]

def generateImg(imageContext, options, img_name):
    response = openai.Image.create(
        prompt=imageContext,
        n=options,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    response = requests.get(image_url)

    with open("imagem/" + img_name + ".jpg", "wb") as f:
        f.write(response.content)


_input = input("Descreva a imagem que deseja criar:")

messages[1]["content"] = _input

name = textGPT.generate_chat_completion(messages, model="gpt-3.5-turbo", temperature=1, max_tokens=None)

generateImg(_input, options=1, img_name=name)
