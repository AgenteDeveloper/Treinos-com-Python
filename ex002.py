# Calculo básico e uso de .format

n1 = int(input("Digite um numero: "))
n2 = int(input("Digite outro número: "))

soma = n1 + n2

# print("A soma do numero", n1, "e o numero", n2, "vale:", soma)
print("A soma entre {} e {} vale {}".format(n1, n2, soma))
