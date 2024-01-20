# Exibir o dobro, triplo e raiz quadrada

n1 = int(input("Digite um número: "))

# Dobro
dob = n1 * 2

#Triplo
tri = n1 * 3

#Raiz Quadrada
rq = n1 ** (1/2)


print("O dobro de {} é: {} \nO triplo de {} é: {} \nA raiz quadrada de {} é: {:.2f} ".format(n1, dob, n1, tri, n1, rq))
