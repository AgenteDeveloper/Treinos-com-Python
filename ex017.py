from math import hypot

# Hiportenusa importando apenas este modulo da biblioteca math

cat1 = float(input("Insira o comprimento do cateto oposto: "))
cat2 = float(input("Insira o comprimento do cateto adjacente: "))

hi = hypot(cat1, cat2)



print("A hipotenusa vai medir {:.2f}".format(hi))