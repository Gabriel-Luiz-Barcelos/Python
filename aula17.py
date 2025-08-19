comidas = ['pizza','hamburguer','picole']
print(comidas)
comidas.append('bolacha')
print(comidas)

comidas.insert(0,'cachorro quente') #usando o insert coloco na posição que quiser, no caso coloquei na posição 0
print(comidas)
comidas.insert(3,'suco')
print(comidas)

del comidas[1] # Dessa forma podemos excluir item pelp índice
print(comidas)

comidas.pop() # o pop por padrão sempre exclui o último item, mas posso colocar o índece dentro dele também comidas.pop(1)
print(comidas)

comidas.remove('suco') # e com o remove devemos digitar o valor, não o índice, ele remove só o primeiro que eu passar, se tiver dois iguais ele vai remover o primeiro
print(comidas)

valores = list(range(4,11))
print(valores)

valores2 = [8,2,5,4,9,3,0]
valores2.sort()
print(valores2)
valores2.sort(reverse=True) # pra mostrar em ordem decrescente 
print(valores2)
print(f'Essa lista tem {len(valores2)} elementos')

#Se tentar remover item que não ta na lista com o remove, ele dá erro, então usa if para validar e se tiver remove
if 1 in valores2:
    valores2.remove(1)

for most in valores2:
    print(most, end=' ')    
print()
valores3 = []
for cont in range(0,5):
    valores3.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores3):
    print(f'Na posição {c} tem o valor {v}')    

print('-'*30)

a = [2,5,7,4,3]
b =a 
b[2]=4 #Ele vai alterar a lista A também, porque está fazendo uma ligação entre as listas, não uma cópia
print(f'Lista A: {a}')
print(f'Lista B: {b}')  

a = [2,5,7,4,3]
b =a[:] 
b[2]=4 #Dessa forma ele pega os valores de a e joga em b, nesse caso fazendo a cópia
print(f'Lista A: {a}')
print(f'Lista B: {b}') 
