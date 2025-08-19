dadosjog = dict()
gols = list()
listadadosjog = list()

while True: 
    nome = str(input('Qual o nome do jogador: '))
    partidas = int(input(f'Quantas partidas o {nome} jogou? '))

    golstot = 0

    for c in range(1,partidas+1):
        golpart = int(input(f'Quantos gols na partida {c}: '))
        gols.append(golpart)
        golstot += golpart

    dadosjog['nome'] = nome
    dadosjog['gols'] = gols[:]
    dadosjog['total'] = golstot
    
    listadadosjog.append(dadosjog.copy())
    gols.clear()

    opcao = str(input('Quer continuar? [S/N]')).upper().strip()

    if opcao == 'N':
        break

    print('-'*30)

print('-='*20)
print(f'{"cod nome":<15}',end=' ')
print(f'{"gols":<15}',end=' ')
print('total')
print('-'*40)

cont = 0
for a in listadadosjog:
    print(cont,end=' ')
    print(f'{a['nome']:<13}',end=' ')
    print(f'{str(a['gols']):<17}',end=' ')
    print(a['total'])
    cont+=1

while True:
    cod = int(input('Mostrar dados de qual jogador? (999 para encerrar)'))
    for b,c in enumerate(listadadosjog):
        if b == cod:
            print(f'-- Levantamento do jogador {c['nome']}')  
            for d in range(0,len(c['gols'])):
                print(f'No jogo {d+1} fez {c['gols'][d]} gols')
    if cod == 999:
        break
    elif cod > len(listadadosjog):
        print(f'Erro! Não existe jogador com código {cod}! Tente novamente ')

print('<<VOLTE SEMPRE>>')




