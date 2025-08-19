n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA:'))

ultimo_termo = n1 + r * 10

while n1 < ultimo_termo:
    print('{} → '.format(n1),end='')
    n1 += r
print('FIM')