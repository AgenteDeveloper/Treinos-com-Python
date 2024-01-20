#Reajuste de salário

salario = float(input("Insira o salário atual: R$"))

reajuste = salario + (salario * 15 / 100)

print("O seu salário era de R${:.2f} e agora com um aumento de 15% você passa a receber R${:.2f}".format(salario, reajuste))