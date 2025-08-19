numeros = []
while True:
    numeros.append(int(input('Digite um número: ')))
    escolha = str(input('Deseja continuar? [S/N]')).strip().upper()[0]
    if escolha in 'N':
        break

print(f'O número de itens digitados é {len(numeros)}')
numeros.sort(reverse=True)
print(f'A lista de valores em ordem decrescente é {numeros}')


if 5 in numeros:
    print(f'O número 5 foi digitado e está na lista na posição {numeros.index(5)}') 
else:print('O número 5 não foi digitado e não está na lista')       