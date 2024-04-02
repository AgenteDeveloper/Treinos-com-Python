#Calculo de viagem

distancia = float(input("Insira a distância de sua viagem: "))

print("Você irá começar uma viagem que tem a distancia de {:.2f}Km".format(distancia))

if distancia <= 200:
    preco = distancia * 0.50
    print("O valor total de sua viagem de {:.2f}Km será de R${:.2f}.".format(distancia, preco))

else:
    preco = distancia * 0.45
    print("O valor total de sua viagem de {:.2f}Km será de R${}.".format(distancia, preco))