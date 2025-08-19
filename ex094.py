pessoas = dict()
listapessoas = list()
listamulheres = list()
listacimamedia = list()

somaidade = mediaidade = 0
while True:
    escolha = ' '

    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo: [M/F] ')).upper().strip()
    idade = int(input('Idade: '))
    somaidade += idade

    pessoas['idade'] = idade

    if pessoas['sexo'] == 'F':
        listamulheres.append(pessoas.copy())

    listapessoas.append(pessoas.copy())

    escolha = str(input('Quer continuar: [S/N]')).upper().strip()
    if escolha == 'N':
        break

mediaidade = somaidade / len(listapessoas)    

print('-='*20)

print(f'- O grupo tem {len(listapessoas)} pessoas.')
print(f'- A média de idade é de {mediaidade} anos.')
print(f'- As mulheres cadastradas foram: ',end=' ')
for e in listamulheres:
    print(e['nome'],end=' ')

for g in listapessoas:
    if g['idade'] > mediaidade:
        listacimamedia.append(g)

print('\n')
print(f'- Lista de pessoas que estão acima da média: \n')


for f in listacimamedia:
    for k,v in f.items():
        print(f'{k} = {v};',end=' ')
    print('\n')      
print('<<ENCERRADO>>')     








