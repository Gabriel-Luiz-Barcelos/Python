frase = input('Digite uma frase: ').lower().strip()

frase_tratada = frase.split()
frase_tratada = ''.join(frase_tratada)
print(frase_tratada)
inversa = ''

for c in range(len(frase_tratada) - 1,-1,-1):
    inversa += frase_tratada[c]
print(inversa)   

if frase_tratada == inversa:
    print('a frase é palíndromo')
else:
    print('a frase não é palíndromo')    

''' Se usasse essa linha abaixo não precisa do for e da variável inversa vazia
 no lugar do inverso colocaria 
 inversa = frase_tratada[::-1] Usando fatiamento, usando os :: é pra pegar do início ao fim, 
 e -1 pra começar do final e ir pra frente  
 '''   
