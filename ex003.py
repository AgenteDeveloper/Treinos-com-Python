# Identificação de numero/texto em geral.

d = input("Insira algo: ")

print("Qual é a classe?", type(d) )
print("Pode ser imprimido?", d.isprintable())
print("É alfabetico?", d.isalpha())
print("Só contem espaços?", d.isspace())
print("É alfa-numerico?", d.isalnum())
print("Está escrito apenas em letras maiusculas?", d.isupper())
print("Está escrito apenas em letras minusculas?", d.islower())
print("É um identificador?", d.isidentifier())