# Analise de Triangulo
r1 = float(input("Primeiro lado: "))

r2 = float(input("Segundo lado: "))

r3 = float(input("Terceiro lado: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("Os lados acima formam um triângulo!")
else:
    print("Os lados acima não formam um triângulo!")