numeros = []

while True:
    opcao = ' '
    numeros.append(int(input('Digite um número: ')))
    
    while opcao not in 'NS':
        opcao = str(input('Deseja continuar: [S/N]')).strip().upper()[0]
    if opcao == 'N':
        break

pares = []
impares = []

for par in numeros:
    if par %2 == 0:
        pares.append(par)

for imp in numeros:
    if imp %2 != 0:
        impares.append(imp)        

print('=-'*30)
print(f'A lista completa é {numeros}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
