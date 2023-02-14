caracteres = ['D','U','D','U']

for caractere in caracteres:
    numeroASCII = ord(caractere)
    numeroHexa= hex(numeroASCII)
    numeroBinario = bin(numeroASCII)
    print("O caractere", caractere, "tem o código ASCII", numeroASCII, "e em Hexa ", numeroHexa, " em binário ", numeroBinario )
