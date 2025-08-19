matriz = [[], [], []]
k =0
j = 0



for i in range(0,9):
    if j == 3:
        k+=1
        j=0
    matriz[k].append(int(input(f'Digite o valor da posição [{k}, {j}]: ')))
    
    j +=1

print('-='*30)
l = 0
for c in matriz:
    if l == 3 or l == 6:
        print()
    for d in c:
        print(f'[ {d:^5} ]',end=' ')
        l +=1
print()
print('-='*30)
       
somapares = 0       
for g in matriz:
    for f in g:
        if f % 2 == 0:
            somapares += f
maior = 0
m =1
maior = matriz[1][0]
for seglin in matriz[1]:
    if seglin > maior:
        maior = seglin
    m +=1

soma3coluna = matriz[0][2] + matriz[1][2] + matriz[2][2]

print(f'A soma dos valores pares é {somapares}')
print(f'A soma dos valores da terceira coluna é {soma3coluna}')
print(f'O maior número da segunda linha é {maior}')

        