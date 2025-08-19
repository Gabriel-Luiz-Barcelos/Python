def mensagem(msg):
    print('-'*20)
    print(msg)
    print('-'*20)

mensagem(str(input('Digite a mensagem: ')))
mensagem('Python')


def soma(a, b):
    print(f'A={a} e B={b}')
    soma = a + b
    print(f'a soma de A + B = {soma}')


soma(5,6)    
soma(8, 9)

print('-'*20)

def contador(* num):  #Asterisco serve para desempacotar, significa que eu não sei quantos parâmetros vou receber
    tam = len(num)                     # Num será uma tupla
    print(f'Recebi os números {num} por parâmetro, ao todo são {tam}')    

contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)


print('-'*20)

valores = [6, 3, 9, 1, 0, 2]

def dobra(lst):
    pos = 0
    while pos< len(lst):
        lst[pos] *= 2
        pos+=1

dobra(valores)
print(valores)

print('-'*20)

def soma2(* num): #desempacotamento também 
    s = 0
    for valor in num:
        s += valor
    print(f'A soma dos números {num} é {s}')    

soma2(2, 5, 3, 5)
soma2(8, 2)        