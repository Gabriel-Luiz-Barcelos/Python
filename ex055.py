
peso_maior = 0
peso_menor = 0

for c in range(0,5):
    peso= float(input('Digite o peso da pessoa: '))
    if c == 0:
        peso_maior = peso
        peso_menor = peso
    else:    
        if peso > peso_maior:
            peso_maior = peso
        elif peso < peso_menor:
            peso_menor = peso
   
print('o maior peso dos {} é {} e o menor é {}'.format(c,peso_maior,peso_menor))                