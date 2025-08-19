import random
from time import sleep
num = random.randint(1,3)

if num == 1:
    jogada_maquina = 'tesoura'
elif num == 2:
    jogada_maquina = 'papel'
else: 
    jogada_maquina = 'pedra'    


jogada_jogador = input("""Escolha uma das opções para jogar
Pedra 🪨
Tesoura ✂️
Papel 📜
: """).lower().strip()



if jogada_jogador == 'pedra' or jogada_jogador == 'tesoura' or jogada_jogador == 'papel':
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)
    print(20 * '=-')
    if jogada_maquina == jogada_jogador:
        print('Os dois jogaram {}, então é empate'.format(jogada_maquina))
    elif jogada_maquina == 'pedra':
        if jogada_jogador == 'papel':
            print('você ganhou!\nCOmputador jogou pedra')
        else:
            print('Você perdeu!\nA máquina jogou pedra')
    elif jogada_maquina == 'papel':
        if jogada_jogador == 'pedra':
            print('Você perdeu!\nMáquina jogou papel')
        else:
            print('Você ganhou\nMáquina jogou papel')
    elif jogada_maquina == 'tesoura':
        if jogada_jogador == 'papel':
            print('Você perdeu!\nMáquina jogou tesoura')
        else:
            print('Você ganhou\nMáquina jogou tesoura')     
else:
    print('Opção inválida, você digitou errado')            
      
print('=-' * 20)


