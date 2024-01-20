# Calculadora de pintura de paredes

lag = float(input("Insira a largura da parede: "))
alt = float(input("Insira a altura da parede:  "))

area = lag*alt

tinta = area / 2

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m² ".format(lag, alt, area))

print("Para pintar a sua parede, você irá precisar de {}l de tinta".format(tinta))