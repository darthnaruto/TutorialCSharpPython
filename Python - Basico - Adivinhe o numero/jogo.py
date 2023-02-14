import random

def main():
  # Gerar número aleatório
  numeroRandomico = random.randint(0, 100)
  guess = None
  tries = 0

  # Loop para ler o chute do usuário
  while guess != numeroRandomico:
    guess = int(input("Adivinhe o número entre 0 e 100: "))
    tries += 1

    # Verificar se o chute é maior ou menor
    if guess > numeroRandomico:
      print("O número é menor.")
    elif guess < numeroRandomico:
      print("O número é maior.")
    else:
      print(f"Você acertou com {tries} tentativas!")

# Executar o programa
if __name__ == "__main__":
  main()
