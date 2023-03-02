import requests
import json

#Acessando a API do Chuck Norris para pegar uma piada randomizada
url = 'https://api.chucknorris.io/jokes/random'
response = requests.get(url)
json_data = response.json() #texto em infles, a resposta foi convertida de TEXTO para um object JSON
print("Objeto Json Convertido:", json_data) #imprimo ele na tela aqui
piadaEmIngles = json_data['value'] #Aqui pegamos um dos campos chamado Value
print("Piada em Ingles:", piadaEmIngles)


# substitua <sua_chave_api> pela chave de API fornecida pela OpenAI
api_key = "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"
url = "https://api.openai.com/v1/engines/text-davinci-003/completions"

prompt = "Traduza para Portugues: " + piadaEmIngles
params = {
    "prompt": prompt,
    "max_tokens": 150,
    "temperature": 0.7,
    "n": 1,
    "stop": None
}

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

response = requests.post(url, headers=headers, data=json.dumps(params))
response.raise_for_status()
data = response.json()

answer = data["choices"][0]["text"].strip()
print(f"Tradução: {answer}")