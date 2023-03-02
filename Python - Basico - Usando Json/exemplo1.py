import json
import os

os.system('cls')

texto='{"nome":"Eduardo","apelido":"Dudu","idade":"21"}'
json_convertido = json.loads(texto)
print("Olá, meu nome é: "+json_convertido["nome"]+" e eu tenho "+json_convertido["idade"]+ " anos")
