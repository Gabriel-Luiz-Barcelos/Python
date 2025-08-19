from datetime import date

atual = date.today().year
demenor = 0
demaior = 0
for c in range(1,8):
    ano_nasc = int(input('Digite o ano de nascimento da {}° Pessoa: '.format(c)))
    idade = atual - ano_nasc
    if idade <21:
        demenor +=1
    elif idade >= 21: 
        demaior +=1      
print('O número de pessoas que não atingiram a maioridade é {}\ne os que atingiram a maioridade é {}'.format(demenor,demaior))        
