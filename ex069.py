maiores18 = 0
homenscadastrados = 0
mulheresmenores = 0
while True:
    print('-'*40)
    print('CADASTRE UM PESSOA')
    print('-'*40)
    sexo =' '
    escolha=' '
    
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = input('Sexo: [M/F]').upper().strip()
    print('-'*40)
    while escolha not in 'SN': 
        escolha = input('Quer continuar? [S/N]').upper().strip()

    if idade > 18:
        maiores18 +=1

    if sexo in 'M':
        homenscadastrados +=1

    if sexo in 'F' and idade < 20:
        mulheresmenores +=1

    if escolha in 'N':
        break

print(f'O número de pessoas maior de 18 anos é {maiores18}\nO número de homens cadastrados é {homenscadastrados}\nE o número de mulheres com idade inferior a 20 é {mulheresmenores} ')