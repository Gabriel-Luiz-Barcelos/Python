salario = float(input('digite o seu salário atual: '))

if salario >= 1250.00:
    salario += salario * 10 / 100
    print('o valor do aumento é de {:.2f}'.format(salario))
else:
    salario += salario * 15 /100
    print('o valor do aumento é de {:.2f}'.format(salario))