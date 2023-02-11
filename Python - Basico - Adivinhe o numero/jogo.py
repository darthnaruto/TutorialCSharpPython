import random

def main():
  # Gerar número aleatório
  num = random.randint(0, 100)
  guess = None
  tries = 0

  # Loop para ler o chute do usuário
  while guess != num:
    guess = int(input("Adivinhe o número entre 0 e 100: "))
    tries += 1

    # Verificar se o chute é maior ou menor
    if guess > num:
      print("O número é menor.")
    elif guess < num:
      print("O número é maior.")
    else:
      print(f"Você acertou com {tries} tentativas!")

# Executar o programa
if __name__ == "__main__":
  main()
