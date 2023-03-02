import mat
import os

# Limpa a tela do console
os.system('cls')

a = int(input("Entre o primeiro número: "))
b = int(input("Entre o segundo número: "))
resultado = mat.soma(a,b)
print(f"A soma dos dois é {resultado}")