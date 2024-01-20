#Leitura de digitos de um número

numero = int(input("Insira um numero de 0 a 9999: "))

n = str(numero)

u = numero // 1 % 10
d = numero // 10 % 10
c = numero // 100 % 10
milhar = numero // 1000 % 10

print("Numero em analise....")

print("Unidade: {}".format(u))
print("Dezena: {}".format(d))
print("Centena: {}".format(c))
print("Milhar: {}".format(milhar))