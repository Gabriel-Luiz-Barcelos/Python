n1 = int(input('Difgite o primeiro termo: '))
n2 =n1
r = int(input('Digite a razão da PA: '))
x =10
soma_escolha = 10
escolha = 1
while escolha != 0:
    ultimo_termo = n1 + r * x
    while n1 < ultimo_termo:    
        print('{} → '.format(n1), end=' ')
        n1 += r
    print('PAUSA')    
    escolha = int(input('\nMais quatas posições deseja ver? Se não deseja seguir digite 0: '))    
    if escolha != 0:
        x = escolha 
    soma_escolha += escolha    
       
print('Programa encerrado, com {} termos mostrado'.format(soma_escolha))    

