# Conversão de medidas

m1 = float(input("Insira um valor em metros para ser convertido: "))

cm = m1 * 100
mm = m1 * 1000

print("O valor de {}m em centrimetros se torna {:.0f}cm e em milimetros é {:.0f}mm".format(m1, cm, mm))
