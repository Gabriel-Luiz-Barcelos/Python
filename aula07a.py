n1 = int(input('digite um valor: '))
n2 = int(input('digite outro numero: '))
s = n1+n2
m = n1 * n2
d = n1 / n2
di= n1 // n2
e = n1 ** n2

print('a soma é {} \n o produto é {} e \n a divisao é {:.3f}'.format(s,m,d, end='>>> '))
print('divisao inteira é {} exponenciação é {}'.format(di,e))