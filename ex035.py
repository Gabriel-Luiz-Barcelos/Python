r1 = float(input('digite o valor da primeira reta: '))
r2 = float(input('digite o valor da segunda reta: '))
r3 = float(input('digite o valor da terceira reta: '))

if r1 + r2 < r3 or r2 +r3 < r1 or r1 + r3 < r2:
    print('não pode formar um triangulo com as medidas')
else:
    print('pode formar um triangulo com as medidas')    