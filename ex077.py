lista = ('aprender','programar','linguagem','python','curso','curso','gratis','estudar','praticar',
         'estudar','praticar','trabalhar','mercado','programar','futuro')


for c in lista:
    f = ' '
    for d in c:
        if d in 'aeiou':
            f +=d + ' '
    print(f'Na palavra {c.upper()} temos as vogais {f}')
