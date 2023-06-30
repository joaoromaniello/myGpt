import openai
import requests
import random
import variables

API_ENDPOINT = "https://api.openai.com/v1/images/generations"

openai.api_key = variables.API_KEY


def generateImg(imageContext, options):
    response = openai.Image.create(
        prompt=imageContext,
        n=options,
        size="1024x1024"
    )
    image_url = response['data'][0]['url']
    response = requests.get(image_url)

    with open("imagem/image" + str(random.randint(0, 400)) + ".jpg", "wb") as f:
        f.write(response.content)


generateImg("Uma cadela feliz descendo em um escorregador", options=1)
