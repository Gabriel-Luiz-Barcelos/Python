n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

total = n1 + r * 10
 

for i in range(n1,total,r):
    print(i, end=' → ')
print('ACABOU')    
          
        
        
    