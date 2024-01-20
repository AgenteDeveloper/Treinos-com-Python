from math import cos, sin, tan, radians
#Calculo feito por módulos de seno, cosceno e tangente de math

angulo = float(input("Insira o angulo que desejqa calcular: "))

seno = sin(radians(angulo))
print("O angulo {} possui o seno de {:.2f}".format(angulo, seno))

cosceno = cos(radians(angulo))
print("O angulo {} possui o cosceno de {:.2f}".format(angulo, cosceno))


tangente = tan(radians(angulo))
print("O angulo {} possui a tangente de {:.2f}".format(angulo, tangente))

# Calculo de seno, cosceno e tangente usando a biblioteca math





