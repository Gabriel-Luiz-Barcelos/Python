valores = []
for c in range(0,5):
    valores.append(int(input(f'Digite um valor para posição {c}: ')))
print(f'Você digitou os valores {valores}')
maior = 0
menor = 0
maiores = []
menores = []
for c in range(0,len(valores)):
    
    if c ==0:
        maior = menor = valores[c]
        maiores.append(c)
        menores.append(c)
    else:
        if valores[c] > maior:     
            maior =valores[c] 
            del maiores
            maiores = []
            maiores.append(c)
        elif valores[c] == maior:
            maiores.append(c)
        elif valores[c] <menor:     
            menor =valores[c] 
            del menores
            menores = []
            menores.append(c)
        elif valores[c] == menor:
            menores.append(c)
             
    c+=1              

if len(maiores) >1:
    print(f'O maior valor da lista é {maior} e estão nas posições {maiores}')
else:
    print(f'O maior valor da lista é {max(valores)} e está na posição {valores.index(max(valores))}')
if len(menores) >1:
    print(f'O menor valor da lista é {menor} e está na posição {menores}')
else:
    print(f'O menor valor da lista é {min(valores)} e está na posição {valores.index(min(valores))}')

