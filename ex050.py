s = 0
for i in range(1,7):
    num = int(input('Digite o {} número: '.format(i)))
    if num  % 2 == 0:
        s += num
print('A soma dos números pares que você digitou é {}'.format(s))        