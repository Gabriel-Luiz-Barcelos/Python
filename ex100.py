from random import randint
from time import sleep

numeros = []

def sorteia(numeros):
    for i in range(0,5):
        numeros.append(randint(0,9))
    print('Sorteando os valores da lista: ',end='')    
    for d in numeros:
        print(d,end=' ',flush=True)  
        sleep(0.5)
    print('Pronto')       

def somaPar(* num):
    soma = 0
    for c in numeros:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores pares de {num} temos {soma} ')          

sorteia(numeros)

   

somaPar(numeros)      