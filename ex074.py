from random import randint 

a = (randint(1,10))
b = (randint(1,10))
c = (randint(1,10))
d = (randint(1,10))
e = (randint(1,10))

#n = (randint(1,10) ,randint(1,10) ,randint(1,10) ,randint(1,10) ,randint(1,10)  )  Dava pra fazer assim também 

x = (a , b , c , d , e)
print(f'Os valores sorteados foram {x}')
print('-='*20)
print(f'Os valores sorteados foram: ')
for c in x:
    print(f'{c}',end=' ')
print()    
print('-='*20)
menor = maior = 0
for c in range(0,len(x)):
    if c == 0:
        menor = x[c]
        maior = x[c]
    if x[c] < menor:
        menor = x[c]
    if x[c] > maior:
        maior = x[c]
print(f'O maior valor sorteado foi {maior}')                
print(f'O menor valor sorteador foi {menor}')
print('=-'*20)
print(f'O maior valor sorteado for {max(x)}') # dava pra usar o mac e min ao invés das validações 
print(f'O maior valor sorteado for {min(x)}')
        
    