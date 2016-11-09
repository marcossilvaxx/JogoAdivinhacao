def JogoAdivinhacao():
    import random
    import time
    for i in range(4):
        print("Iniciando Jogo da Adivinhação" + "." * i)
        time.sleep(1)
    print('''\nBem vindo ao jogo da adivinhação!
\nTente adivinhar um número entre 1 e 100!
Lembrando que você só tem 3 chances para acertar o número!
\nBoa sorte! :)\n''')
    numSort = random.randint(1, 100)
    for i in range(3):
        palpite = eval(input("Escolha um número inteiro de 1 a 100:\n"))
        if palpite == numSort:
            if i == 0:
                print("Parabéns! Você acertou de primeira! :D")
            elif i == 1:
                print("Parabéns! Você acertou de segunda! :)")
            elif i == 2:
                print("Parabéns! Você demorou um pouco pra acertar mas pelo menos acertou! :P")
        else:
            if i == 0:
                print("Você errou! Tente novamente! :( Chances restantes: 2")
                if palpite > numSort:
                    print("O número sorteado é menor que o número que você escolheu.")
                else:
                    print("O número sorteado é maior que o número que você escolheu.")
            elif i == 1:
                print("Você errou de novo! Tente novamente! :C Chances restantes: 1")
                if palpite > numSort:
                    print("O número sorteado é menor que o número que você escolheu.")
                else:
                    print("O número sorteado é maior que o número que você escolheu.")
            elif i == 2:
                print("Você errou de novo! Você é azarado! :D Chances restantes: 0")
                print("O número era:", numSort)
    pergunta = str(input("Deseja jogar novamente?\n"))
    if pergunta[0].lower() == "s":
        JogoAdivinhacao()
    elif pergunta[0].lower() == "n":
        print("Programa encerrado. Até mais!")
    else:
        print("Comando desconhecido.")

JogoAdivinhacao()
