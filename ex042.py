m1 = float(input('digite a medida de ums dos lados: '))
m2 = float(input('digite a medida do outro lado: '))
m3 = float(input('digite a medida do outro lado: '))

if m1 == m2 ==m3:
    print('O triângulo é equilátero')
elif m1 != m2 != m3 and m1 != m3:
    print('O triangulo é escaleno')
else:
    print('Triangulo é isosceles')        