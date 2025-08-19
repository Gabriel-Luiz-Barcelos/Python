numeros = (
    'zero', 0, 'um', 1, 'dois', 2, 'tres', 3, 'quatro', 4, 'cinco', 5, 
    'seis', 6, 'sete', 7, 'oito', 8, 'nove', 9, 'dez', 10, 'onze', 11, 
    'doze', 12, 'treze', 13, 'quatorze', 14, 'quinze', 15, 'dezesseis', 16, 
    'dezessete', 17, 'dezoito', 18, 'dezenove', 19, 'vinte', 20
)
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    escolha = ' '
    while True:
        if num <= 20 and num > 0:
            break
        else:        
            num = int(input('Tente novamente. Digite um número entre 0 e 20: '))

    for cont in range(0,len(numeros)):
        if num == numeros[cont]:
            print(f'O número digitado foi {numeros[cont-1]}')

    while escolha not in 'SN':
        escolha = str(input('Você deseja continuar: [S/N] ')).upper().strip()[0]

    if escolha in 'N':
        break       
print('Programa encerrado')         