import math
ang = int(input('digite o valor do ângulo: '))
ang_graus = math.radians(ang)
seno = math.sin(ang_graus)
cosseno = math.cos(ang_graus)
tangente = math.tan(ang_graus)
print('o cosseno do número {} é {:.2f} \no seno é {:.2f}\ne a tangente é {:.2f}'.format(ang,cosseno,seno,tangente))