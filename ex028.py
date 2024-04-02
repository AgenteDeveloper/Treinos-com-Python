# Jogo de adivinhação 1.0v

import random

print("--" * 10)
print("Estou pensando em um numero de 0 a 5. Tente Adivinhar em que número estou pensando?")
print("--" * 10)

gerar = random.randint(0,5)

resposta = int(input("Em que numero estou pensando agora? "))

if resposta == gerar:
    print("Parábens! Você deve ser um vidente!")

else:
    print("Você errou, sinto muito. Você colocou {} mas eu pensei em {}".format(resposta,gerar))



