from random import randint
from time import sleep
print('-'*30)
print('       JOGA NA MEGA SENA       ')
print('-'*30)

lista = list()
dados = list()
jogadas = int(input('Quantos jogos deseja fazer: '))

for i in range(0,jogadas): 
    for d in range(0,6):
        num = (randint(1,60))
        if num in dados:
            num = (randint(1,60))
        dados.append(num)
    lista.append(dados[:])
    dados.clear()

print('-='*3,f'Sorteando {jogadas} jogos','-='*3)
j = 1
for c in lista:
    print(f'Jogo {j}: {c}')
    sleep(1)
    j+=1

print(f"{'-='*5}{' < Boa Sorte! > '}{'-='*5}")    
