from datetime import date

ano = date.today().year
ano_nasc = int(input('Em que ano você nasceu? '))
idade = ano - ano_nasc

if idade < 18:
    anos_falt = 18 - idade
    print('Voce nasceu em {} e deverá se alistar em {} anos'.format(ano_nasc,anos_falt))
elif idade == 18:
    print('Você nasceu em {} e  tem {} anos e deve se alistar esse ano'.format(ano_nasc,idade))    
elif idade > 18:
    print('Você ja passou da data de se alistar, tem {} anos'.format(idade))
    alistou = input('Você já se alistou? (y/n)')
    if alistou == 'y':
        print('Parabéns, está regular') 
    else:
        print('se apresente ao quartel o quanto antes')   
else:
    print('Digito inválido')            