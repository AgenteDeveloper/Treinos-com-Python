# Maior e menor numero

a = int(input("Primeiro Valor: "))

b = int(input("Segundo Valor: "))

c = int(input("Terceiro Valor: "))

maior = a
menor = a
#Numero maior
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c

#Numero menor
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c

print("O maior numero inserido é: {}".format(maior))

print("O menor numero inserido é: {}".format(menor))

