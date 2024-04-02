# Calculo de aumento de salário

salario = float(input("Qual o salário atual? R$ "))



if salario > 1250.00:
    novo = salario + (salario * 10 / 100)
    print("Antes você ganhava R${:.2f} e agora com um aumento de 10% você ganhará R${:.2f}.".format(salario, novo))

if salario <= 1250.00:
    novo = salario + (salario * 15 / 100)
    print("Antes você ganhava R${:.2f} e agora com um aumento de 15% você ganhará R${:.2f}.".format(salario, novo))



