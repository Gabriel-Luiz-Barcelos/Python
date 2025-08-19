from random import randint
n =11
cont = 0
num = randint(0,10)
while num != n:
    n = int(input('Tente adivinha o número de 1 a 10 que estou pensando: '))
    cont +=1
    if num != n:
        if n < num:
            print('Tente novamente, você errou, o número que pensei é maior')
        if n> num:
            print('Tenta novamente, você errou, o número que pensei é menor')    

print('Parabéns, você acertou o número {} que foi o que pensei em {} tentantivas'.format(num,cont))    