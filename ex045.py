# Pedra, papel ou tesoura

from random import choice

print('{:=^20}'.format(' Jokenpo! '))

#Escolhe uma das opções aleatóriamente
jogo = ["Pedra", "Papel", "Tesoura"]

print(''' Suas opções:
[1] - Pedra
[2] - Papel
[3] - Tesoura
''')

opcao = int(input("Esccolha uma das opções: "))


# Versão 1.5 (Melhorada com unico bloco de if e else com condições aninhadas, menos linhas, mais legivel)
if opcao not in [1, 2, 3]:
    print("Opção Inválida, tente novamente mais tarde!")

else :
    jogador = jogo [opcao - 1]
    computador = choice(jogo)

    print("Você escolheu:",jogador)
    print("Máquina escolheu:",computador)

    if jogador == computador:
        print("EMPATE!")

    elif (jogador == "Pedra" and computador == "Tesoura") or (jogador == "Papel" and computador == "Pedra") or (jogador == "Tesoura" and computador == "Papel"):
        print("Você Ganhou!")

    else:
        print("Máquina Ganhou!")




# Versão 1.0 (Feita com blocos de condição separados por cada opção
"""if opcao == 1 and jogo == "Pedra":
    print("Empatamos, vamos tentar novamente?")

elif opcao == 1 and jogo == "Papel":
    print("Eu Ganhei! Escolhi Papel.")

elif opcao == 1 and jogo == "Tesoura":
    print("Você Ganhou! Escolhi Tesoura.")

#Opção de Papel
if opcao == 2 and jogo == "Pedra":
    print("Você Ganhou! Escolhi Pedra")

elif opcao == 2 and jogo == "Papel":
    print("Empatamos, vamos tentar novamente?")

elif opcao == 2 and jogo == "Tesoura":
    print("Eu Ganhei! Escolhi Tesoura!")

#Opção de Tesoura

if opcao == 3 and jogo == "Pedra":
    print("Eu Ganhei! Escolhi Pedra")

elif opcao == 3 and jogo == "Papel":
    print("Você Ganhou! Escolhi Papel")

elif opcao == 3 and jogo == "Tesoura":
    print("Empatamos, vamos tentar novamnente?")"""

