num = int(input('Digite um número para saber seu fatorial: '))

fat = 1

while num >0:
    
    fat *= num  
    print('{}'.format(num),end='')    
    print(' x ' if num >1 else ' = ',end='')    
    num -= 1
    
print(fat)    
