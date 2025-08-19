from datetime import date

ano_atual = date.today().year

def voto(ano):
    idade = ano_atual - ano
    if idade >= 18 and idade < 65:
        return 'VOTO OBRIGATÓRIO'
    elif idade < 18:
        return 'NÃO VOTA'
    else:
        return 'VOTO OPCIONAL'
    
ano = int(input('Em que ano você nasceu? '))
idade = ano_atual - ano
print(f'Com {idade} anos: {voto(ano)}')    
    