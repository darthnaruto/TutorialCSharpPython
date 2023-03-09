import requests
import json


def GetPiada():
    # Acessando a API do Chuck Norris para pegar uma piada randomizada
    url = 'https://api.chucknorris.io/jokes/random'
    response = requests.get(url)
    # texto em ingles, a resposta foi convertida de TEXTO para um object JSON
    json_data = response.json()
    piadaEmIngles = json_data['value']  # Aqui pegamos um dos campos chamado Value

    # substitua <sua_chave_api> pela chave de API fornecida pela OpenAI
    api_key = "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"
    url = "https://api.openai.com/v1/engines/text-davinci-003/completions"

    prompt = "Traduza para Portugues: " + piadaEmIngles
    params = {
        "prompt": prompt,
        "max_tokens": 200,
        "temperature": 0.7,
        "n": 1,
        "stop": None
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    response = requests.post(url, headers=headers, data=json.dumps(params))
    data = response.json()

    answer = data["choices"][0]["text"].strip()
    print(answer)
    return answer
