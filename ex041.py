import datetime

ano_atual = datetime.date.today().year

ano_nasc = int(input('digite o ano em que nasceu: '))
idade = ano_atual - ano_nasc
if idade <= 9:
    print('Sua categoria é a MIRIM')
elif idade > 9 and idade <= 14:
    print('Sua categoria é a INFANTIL')
elif idade > 14 and idade <= 19:
    print('Sua categoria é a JUNIOR')       
elif idade == 20:
    print('Sua categoria é a SÊNIOR')
else:
    print('Sua categoria é a MASTER')    