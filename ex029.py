# Radar de velocidade

velocidade = float(input("Qual a sua velocidade atual? De 0 a 300Km/H: "))

if velocidade > 80:
    print("Você excedeu o limite de velocidade!\nVocê estava a {} e sua multa será R${:.2f}".format(velocidade,(velocidade-80)*7))
    print("Dirija com cuidado nas estradas e tenha um bom dia!")

else:
    print("Você está na velocidade permitida!\nDirija com cuidado nas estradas e tenha um bom dia!")