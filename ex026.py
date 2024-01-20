# Leitura de Frase

frase = str(input("Digite uma frase para ser analisada: ")).upper().strip()

print("Sua frase contem {} A no total".format(frase.count("A")))

print("A primeira ocorrencia de A na frase é na posição {}".format(frase.find("A") + 1))

print("A ultima aparição de A na frase é na posição {}".format(frase.rfind("A") + 1))

