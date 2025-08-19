n = 0
n2=0
s = 0
c=0
while n != 999:
    
    n1 = float(input('Digite um número [999 para parar] : '))
    if n1 != 999:
        n2 =n1
        print(n2)
        c +=1
        s += n2
    n=n1
    print(s)
    
print('A soma dos números digitados é {} e a quantidade de números digitados foi {}'.format(s,c))