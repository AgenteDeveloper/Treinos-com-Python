import random

n1 = input("Insira o nome do 1º aluno: ")
n2 = input("Insira o nome do 2º aluno: ")
n3 = input("Insira o nome do 3º aluno: ")
n4 = input("Insira o nome do 4º aluno: ")

alunos =  [n1, n2, n3, n4]

nomes = random.choice(alunos)

print("O aluno escolhido para limpar o quadro será: {} ".format(nomes))

# Sorteio de nomes aletorios usando random