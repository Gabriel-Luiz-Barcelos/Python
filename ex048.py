s = 0
cont = 0
for c in range(1,500):
    if c % 2 !=0 and c % 3 == 0:
        s += c
        cont += 1
print('A soma de todos os {} os é {}'.format(cont,s))
