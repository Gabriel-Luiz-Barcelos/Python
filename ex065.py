condicao= True
soma =0
media = 0
contador = 0
maior = menor = 0 

while condicao == True:
    n1= float(input('Digite um número: '))
    escolha = str(input('Deseja continuar: [S/N]')).upper()
    if escolha == 'N':
        condicao = False

    if contador ==0:
        maior = n1
        menor =n1
    soma += n1
    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor =n1
    contador +=1        
media = soma / contador

print('A soma dos {} números digitados é {}\nE a média dos números é {:.2f}'.format(contador,soma,media))
print('O maior número digitado é {} e o menor é {}'.format(maior,menor))

