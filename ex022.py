# Analisador de Texto

nome = str(input("Insira o seu nome completo: ")).strip()

print("Seu nome com todas as letras maiusculas: {}".format(nome.upper()))

print("Seu nome com todas as letras minusculas: {}".format(nome.lower()))

print("Seu nome com as letras capitalizadas fica: {}".format(nome.capitalize()))

print("O seu nome completo possui ao todo {} letras".format(len(nome) - nome.count(' ')))

separar = nome.split()

print("O seu primeiro nome é {} e possui {} letras".format(separar[0],len(separar[0])))