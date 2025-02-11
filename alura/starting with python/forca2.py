def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "pupunha".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    
    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas [index] = letra
                    index += 1
                    #print("Encontrei a letra {} na posição {}".format(letra, index))
                    print(f"Encontrei a letra {letra} na posição {index}")
                else:
                    erros += 1

        enforcou = erros == len(palavra_secreta)
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Tu ganhaste!")
    else:
        print("Tu perdeste!")

    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
