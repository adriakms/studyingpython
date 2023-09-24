#jogo de adivinhação de número usando o loop for

print("*********************************\nBem vindo ao jogo de adivinhação!\n*********************************")

numero_secreto = 42
total_tentativas = 3

for rodada in range(1,total_tentativas+1):
    print(f"Tentativa {rodada} de {total_tentativas}.")
    chute_str = input("Digite o seu número:")
    print("Você digitou: ", chute_str)
    chute = int(chute_str)

    if chute == numero_secreto:
        print("Você acertou!")
    else:
        if chute > numero_secreto:
            print("Você errou! O seu chute foi maior do que o número secreto.")
        elif chute < numero_secreto:
            print("Você errou! O seu chute foi menor do que o número secreto.")

print("Fim do jogo.")