import requests
import json
import os

os.system("cls")

#Entre com seu token
token="c403c688b540a3c285325decb8e28d1c"
#Escolha a cidade e o estado
cidade="Ituiutaba"
estado="MG"
#Coloque aqui o endereço imutável da API
urlbase="http://apiadvisor.climatempo.com.br/api/v1"
#Monte a url final interpolada com as variáveis acima
url=f"{urlbase}/locale/city?name={cidade}&state={estado}&token={token}"

resposta = requests.get(url)
resposta_json=resposta.json()
print(resposta_json)
id_da_cidade= resposta_json[0]['id']

url2=f"{urlbase}/forecast/locale/{id_da_cidade}/hours/72?token={token}"
resposta = requests.get(url2)
resposta_json= resposta.json()["data"][0]
data=resposta_json['date']
chuva=resposta_json['rain']
temperatura=resposta_json['temperature']
umidade=resposta_json['humidity']

resposta_formatada=f"""
{data} : Na cidade de {cidade}, a temperatura hoje será : {temperatura} oCelsius
         A umidade é: {umidade}
         A precipitação de chuva é: {chuva}
"""

print(resposta_formatada)