#GAME: computador vai “pensar” em um número entre 0 e 10.
#Ojogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
#foram necessários para vencer. (O usuário receberá dicas)
print(f"{'G  A  M  E':^50}\n=-=-=-ACERTE O NÚMERO QUE A MÁQUINA ESTÁ PENSANDO=-=-=-")
cont = 1 #o contador já começa com no mínimo um palpite, caso o usuário acerte na primeira.
from random import randint
maquina = randint(0,10)
while True:
    try:
        palpite = int(input("Palpite, até acertar:"))
        break
    except ValueError:
        print("Tem certeza que digitou um número inteiro?Digite corretamente!")
while palpite != maquina:
    cont += 1
    if palpite > maquina:
        print("SUPER DICA: A escolha da máquina é um número mais baixo...Tente novamente..")
    elif palpite < maquina:
        print("SUPER DICA: A escolha da máquina é um número mais alto...Tente novamente..")
    while True:
        try:
            palpite = int(input("Palpite, até acertar:"))
            break
        except ValueError:
            print("Tem certeza que digitou um número inteiro?Digite corretamente!")
print(f"Você acertou após {cont} palpites.")
print(f"O sorteio da máquina foi o número {maquina}, e você digitou {palpite}")


