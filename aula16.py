#toda tupla é IMUTAVEL e fica entre parentêses
lanche = ('Hamburguer','Suco','Pizza','Pudim','Batata Frita')
print(lanche[-2:])

for c in lanche:
    print(f'Eu vou comer {c}')
print('-'*30)
#Outra forma de fazer
for cont in range(0,len(lanche)):
   print(f'Comi {lanche[cont]}')    

print('-'*30)
# sorte coloca em ordem
print(sorted(lanche))

print('-'*30)

a = (1,5,4)
b =(5,8,1,2)
c= a+b #junta as duas tuplas, se for b+ a por exemplo fica ao na ordem diferente
print(c)
print(c.count(5)) # conta quantos 5 apareceu
print(c.index(4)) # com o index ele mostra a posição do número 4 nesse exemplo
print(c.index(1,1)) #vai mostrar na posição 5, porque eu marquei depois da virgula para começar na posição 1

print('-'*30)

#dentro das tuplas em python pode ter tipo de vaiáveis diferentes, string, int, float
pessoa = ('gabriel', 18,'M',1.75)


