#jogo de adivinhação de número usando o loop for
import random

def jogar_adivinhacao():
    print("*********************************\nBem vindo ao jogo de adivinhação!\n*********************************")

    numero_secreto = random.randrange(1,101)
    #print(numero_secreto)
    pontos = 1000

    total_tentativas = 0
    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Defina o nível: "))
    if (nivel == 1):
        total_tentativas = 20
    elif (nivel == 2):
        total_tentativas = 10
    else:
        total_tentativas = 5

    for rodada in range(1,total_tentativas+1):
        print(f"Tentativa {rodada} de {total_tentativas}.")
        chute_str = input("Digite o seu número:")
        print("Você digitou: ", chute_str)
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue
        elif chute == numero_secreto:
            print(f"Você acertou e fez {pontos} pontos!")
            break
        else:
            if chute > numero_secreto:
                print("Você errou! O seu chute foi maior do que o número secreto.")
                if rodada == total_tentativas:
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos} pontos.")
            elif chute < numero_secreto:
                print("Você errou! O seu chute foi menor do que o número secreto.")
                if rodada == total_tentativas:
                    print(f"O número secreto era {numero_secreto}. Você fez {pontos} pontos.")

        pontos_perdidos = abs(numero_secreto - chute)
        pontos = pontos - pontos_perdidos
        print

    print("Fim do jogo.")
