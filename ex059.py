n=0
soma = 0
mult = 0
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

while n != 5:
    
    escolha = int(input(""" Digite a opção que desejar
    [1] - Somar
    [2] - Multiplicar
    [3] - Maior     
    [4] - Novos números
    [5] - Sair do programa   
     >>>>>>> Qual é a sua escolha?                                         
    """))
    if escolha == 1:
        soma = n1 + n2
        print('A soma dos números {} e {} é {}'.format(n1,n2,soma))
    if escolha == 2:
        mult = n1 *n2 
        print('A multiplicação dos números {} X {} é {}'.format(n1,n2,mult))
    if escolha == 3:
        if n1 > n2:
            print('{} é maior que {}'.format(n1,n2)) 
        elif n2 > n1:
            print('{} é maior que {}'.format(n2,n1))       
        else:
            print('Os números {} e {} são iguais'.format(n1,n2))

    if escolha ==4:
        n1 = float(input('Digite um número: '))
        n2 = float(input('Digite outro número: '))
    if escolha == 5:
        n = 5        
    print('=-'*20)    
print('Você saiu do programa')        