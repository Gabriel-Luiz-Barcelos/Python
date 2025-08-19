n1 = int(input('digite um numero: '))
n2= int(input('digite um numero: '))
n3 = int(input('digite um numero: '))

if n1 > n2 and n1 >n3:
    if n2 > n3:
        print('o maior é {} e o menor é {}'.format(n1,n3))
    else:
        print('o maior é {} e o menor é {}'.format(n1,n2))    
if n2 > n1 and n2 > n3:
    if n1 > n3:
        print('o maior é {} e o menor é {}'.format(n2,n3))
    else:
        print('o maior é {} e o menor é {}'.format(n2,n1))    
if n3 > n1 and n3 > n2:
    if n1 > n2:
        print('o maior é {} e o menor é {}'.format(n3,n2))
    else:
        print('o maior é {} e o menor é {}'.format(n3,n1))     


  