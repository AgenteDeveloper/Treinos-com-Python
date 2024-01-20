# Leitura de nome usando modificação de string

nome = str(input("Insira seu nome completo: ")).strip().split()

print("Muito prazer em conhece-lo: {}".format(nome))

print("Seu primeiro nome é {}".format(nome[0]))

print("Seu ultimo nome é {}".format(nome[-1]))