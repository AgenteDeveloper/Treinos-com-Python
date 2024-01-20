# Conversão de Moeda
# Objetivo: Converter o valor que o usuário tiver em reais para dolar e vice-versa, com sinais basicos matematicos

reais = float(input("Insira o valor que você deseja cambiar para dolares: R$"))

dolar = reais / 4.83

euro = reais / 5.36

print("Com R${:.2f} você pode obter US{:.2f} e pode obter {:.2f} euros ".format(reais, dolar, euro))