km = int(input('digite a velocidade: '))

if km > 80:
    multa = (km -80) * 7.0
    print('você ultrapassou o limite de 80Km, sua velocidade foi {}, \nvocê precisa pagar uma multa de R$ {}'.format(km,multa))
else:
    print('sua velocidade foi dentro do permitido')     