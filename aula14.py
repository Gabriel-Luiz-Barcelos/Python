n =1
totpares = 0
totimpares = 0
while n != 0:
    num = int(input('Digite um número: '))
    print('Digite 0 para parar o programa')
    if num % 2 ==0:
        totpares +=1
    else:
        totimpares += 1
    

print('O número de pares é {}\nE o número de ímpares é {}'.format(totpares,totimpares))      
