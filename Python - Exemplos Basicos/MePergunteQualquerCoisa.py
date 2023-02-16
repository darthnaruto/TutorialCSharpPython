import requests
import json
import os

# Limpa a tela do console
os.system('cls' if os.name == 'nt' else 'clear')

# substitua <sua_chave_api> pela chave de API fornecida pela OpenAI
api_key = "digite_sua_api_aqui"
url = "https://api.openai.com/v1/engines/text-davinci-003/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}


prompt = input("Oá, eu sou DEUS! Me pergunte qualquer coisa: ") + " , e seja sucinto na resposta"
params = {
    "prompt": prompt,
    "max_tokens": 300,
    "temperature": 0.7,
    "n": 1,
    "stop": None
}

response = requests.post(url, headers=headers, data=json.dumps(params))
response.raise_for_status()
data = response.json()

answer = data["choices"][0]["text"].strip()
print("Resposta:",answer)