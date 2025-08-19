numeros = []

while True:
    escolha = ' '
    num = int(input('Digite um número: '))
    if num not in numeros:
        numeros.append(num)
        print('Valor adicionado com sucesso...')
    else:
         print('Valor duplicado! Não vou adicionar...')    
       
    while escolha not in 'SN':
        escolha = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if escolha in 'N':
            break
          
numeros.sort()    
print(f'Os números digitados foram {numeros}')    

