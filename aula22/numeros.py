import uteis

num=int(input('Digite um valor: '))
fat= uteis.fatorial(num)
print(f'O fatorial de {num} é {fat}')
print(f'O dobre de {num} é {uteis.dobro(num)}')
print(f'O fatorial de {num} é {uteis.triplo(num)}')

# Se eu usasse from uteis import fatorial, dobro por exemplo
#não precisaria colocar uteis.fatorial, só fatorial daí, mais recomendando usar import uteis 