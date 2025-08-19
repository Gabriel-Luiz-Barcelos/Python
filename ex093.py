dadosjog = dict()
gols = list()
nome = str(input('Qual o nome do jogador: '))
partidas = int(input(f'Quantas partidas o {nome} jogou? '))

golstot = 0

for c in range(0,partidas):
    golpart = int(input(f'Quantos gols na partida {c}: '))
    gols.append(golpart)
    golstot += golpart

dadosjog['nome'] = nome
dadosjog['gols'] = gols
dadosjog['total'] = golstot

print('-='*20)
print(dadosjog)

print('-='*20)
for k,v in dadosjog.items():
    print(f'O campo {k} tem o valor {v}')

print('-='*20)
print(f'O jogador {nome} jogou {partidas}.')
for d in range(0,partidas):
    print(f'=> Na partida {d}, fez {gols[d]} gols')
print(f'Foi um total de {golstot} gols.')    



