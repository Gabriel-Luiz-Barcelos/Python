from datetime import date

ano = int(input('digite o ano: '))

ano_100 = ano % 100
print(ano_100)
if ano == 0:
    ano = date.today().year
if ano_100 == 0:
    if ano % 400 == 0:
        print('ano {} é bissexto'.format(ano)) 
    else:
        print('ano {} não é bissexto'.format(ano))
elif ano_100 != 0:
    if ano % 4 == 0:
        print('ano {} é bissexto'.format(ano))
    else:
        print('ano {} não é bissexto'.format(ano))



