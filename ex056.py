soma = 0
homem_mais_velho = 0
nome_h_maisvelhor = ''
mulheres = 0
for c in range(1,5):
    print('-'*10,'Nome {} pessoa'.format(c),'-'*10 )
    nome = input('Digite o nome: ')
    idade = int(input('Digite a idade: '))
    sexo = int(input('Digite o sexo: \n1 - Homem\n2 - Mulher \n: '))
    soma += idade
    if sexo == 1 and idade > homem_mais_velho:
        homem_mais_velho = idade
        nome_h_maisvelho = nome
    if sexo == 2 and idade < 20:
        mulheres += 1    
media = soma / 4
print('A média de idade é {:.2f}\nO nome do homem mais velho é {} e tem {} anos\nO número de mulheres de menor são {}'.format(media,nome_h_maisvelho,homem_mais_velho,mulheres))


