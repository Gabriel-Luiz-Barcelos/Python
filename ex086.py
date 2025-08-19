matriz = [[], [], []]
j =0
k=0

for i in range(1,10):
    if j == 3:
        k +=1
    if i == 4 or i == 7 or i == 10:
        j =0
    num = int(input(f'Digite um valor para [{k}][{j}]: '))
    matriz[k].append(num)
    j +=1

l = 0
for c in matriz:
    if l == 3 or l ==6:
        print()
    for d in c:
        print(f' ( {d:^5} )',end=' ')    
        l +=1 
      


