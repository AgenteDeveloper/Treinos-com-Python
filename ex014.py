#Calculadora para aluguel de carros

dias = int(input("Por quantos dias foi alugado? "))

quilometro = float(input("Quantos Km foram rodados? "))

preco = (60 * dias ) + (quilometro * 0.15)

print("O total a ser pago será R${:.2f}".format(preco))


