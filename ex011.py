#Calculo de descontos de produtos

produt = float(input("Insira o valor do produto: R$"))

descont = produt - (produt * 5 / 100)

print("O produto possuia o valor de R${:.2f} e após um desconto de 5% ele agora possui o valor de R${:.2f} ".format(produt, descont))

