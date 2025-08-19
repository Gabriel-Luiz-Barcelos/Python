for c in range(6,0,-1):
    print(c)  
print('-' * 20)
for c in range(0,7,2):
    print(c)      
print('-' * 20)
n = int(input('Digite um número: '))
for c in range(1,n+1):
    print(c)
print('-'*20)
i = int(input('Digite o inicio: '))
f = int(input('Digite o fim: ')) 
passo = int(input('digite o passo: '))

for c in range(i,f+1,passo):
    print(c)

print('-'*20)
soma = 0
for c in range(0,4):
    num = int(input('Digite um número: ')) 
    soma += num
print(soma)            