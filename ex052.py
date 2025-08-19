


#for i in range(2, num // 2+1):
#    if num % i == 0:
#        eh_primo = False
#        break
#if eh_primo:
#    print('o número é primo')
#else:
#    print('Não é primo')

num = int(input('Digite um número: '))
tot= 0
eh_primo = True

for c in range(2, num // 2 + 1):
    if num % c == 0:
        print('\033[33m{}\033[m'.format(c),end=' ') 
        eh_primo = False
        tot += 1
    else:
        print('\33[31m{}\33[m'.format(c),end=' ')   
if eh_primo == False:
    print('\nO número {} não é primo e foi divisível {} vezes'.format(num,tot+2))
else:
    print('\nO número {} é primo porque foi divisível apenas 2 vezes vezes, por 1 e por ele mesmo'.format(num))

