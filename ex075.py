a = int(input('Digite um número: '))
b = int(input('Digite um número: '))
c = int(input('Digite um número: '))
d = int(input('Digite um número: '))

#num = (
#int(input('Digite um número: ))
#int(input('Digite um número: ))
#int(input('Digite um número: ))
#int(input('Digite um número: ))
#) dava pra fazer dessa forma também 

x = (a , b , c , d )
print(f'Você digitou os valores {x}')
vezes9ap = 0
posicao3 = 0
pares = 0
for c in range(0,len(x)):
    if x[c] == 9:
        vezes9ap +=1
    if x[c] == 3 and posicao3 == 0:
        posicao3 = c
    if x[c] % 2 == 0:
        pares +=1    
    


print(f'O valor 9 apareceu {vezes9ap} vezes') # dava pra usar {x.cont(9)}
if posicao3 == 0:
    print('O valor 3 não foi digitado em nenhuma posição ') 
else:
    print(f'O valor 3 apareceu na posição {posicao3+1}')      #dava pra usar {x.index(3) +1} 


print('Os números pares digitados foram: ')
for d in range(0,len(x)):
    if x[d] % 2 == 0:
        print(x[d],end=' ')

#pareslista = []
#for d in range(0,len(x)):
#    if x[d] % 2 == 0:
#        pareslista.append(x[d])
#print(f'Foi digitado {pares} números pares são eles {pareslista}')







