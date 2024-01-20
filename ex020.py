from random import shuffle

n1 = str(input("Insira o 1º nome de um aluno: "))
n2 = str(input("Insira o 2º nome de um aluno: "))
n3 = str(input("Insira o 3º nome de um aluno: "))
n4 = str(input("Insira o 4º nome de um aluno: "))

nomes = [n1, n2, n3, n4]

shuffle(nomes)

print("A ordem das apresentações dos alunos será:")
print(nomes)

# listagem de nomes aleatorios usando random