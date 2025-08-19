from random import randint
print('=-'*20,'\nVamos Jogar PAR ou IMPAR\n','=-'*20)
total = 0
vitorias =0
while True:
    num = int(input('Jogue um número: '))
    escolha =' '
    while escolha not in 'PI':
        escolha = input('Escolha PAR ou IMPAR: [P/I]').upper().strip()[0]
    jogadamaquina = randint(0,10)
    total = num + jogadamaquina

    print('-'*20)
    print(f'Você jogou {num} e o computador {jogadamaquina}. Total deu {total}')
    print('-'*20)

    if total % 2 == 0 and escolha[0] == 'P':
        print('Você venceu!\n','=-'*20,'\nVamos jogar de novo')
        vitorias +=1
    elif total % 2 != 0 and escolha[0] == 'I':
        print('Você venceu!\n','=-'*20,'\nVamos jogar de novo')
        vitorias +=1 
    else:    
        print('Você Perdeu!')   
        break

print(f'GAME OVER! Você ganhou o total de {vitorias} partidas')
