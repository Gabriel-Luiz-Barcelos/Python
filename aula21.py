print(input.__doc__)
help(input) 
# Comandos para ver a documentação dos métodos

print('-'*30)

def contador(ini,fim,pas):
    """
    -> Faz um contagem e mostra na tela.
    :param ini: inicia a contagem
    :param fim: termina a contagem
    :param pas: é o passo da contagem
    :return: sem retorno 
    """
    cont = ini
    while cont <= fim:
        print(f'{cont}',end=' ')
        cont +=pas
    print('FIM!')

contador(0,100,10)   

help(contador)
#Usando as 3 aspas dentro da função podemos fazer uma documentação da função, e usando o help(nome da funcao)
#Mostro a documentação

print('-'*30)

def somar(a=0,b=0,c=0):
    """
    -> Faz a soma de três valores e mostra o resultado na tela 
    :parâmetro a: o primeiro valor
    :parâmetro a: o segundo valor
    :parâmetro a: o terceiro valor
    como foi colocado os parametros iguais a 0, quando chamar a função não é obrigado a passar todos os parâmetros,
    caso não recebe um parâmetro els será 0
    """
    soma = a + b + c
    print(f'a soma vale {soma}')
somar(4,5,3)
somar(5,2)    
help(somar)

print('-'*20)

def teste(b):
    b +=4
    print(b)
a =5
teste(a)

print('-'*20)
def funcao():
    n1 =4
    print(f'N1 dentro(local) vale {n1}')
n1 =2 
funcao()
print(f'N1 fora(global) vale {n1}')    

print('-'*20)
def funcao(b):
    global a
    a =8
    print(f'Como usei global a, ele não vai criar variavel local,e vai trocar a variavel global de a por um novo valor')
    print(f'A vale {a}')
a =5 
funcao(a)
print(f'A fora(global) vale também {a}')   

print('-'*20)

def soma(a=0,b=0,c=0):
    s = a + b + c
    return s

r1 =soma(2, 3, 5)
r2 =soma(5, 4)
r3 =soma(6)
print(f'as somas deram {r1}, {r2} e {r3}')

print('-'*20)

def fatorial(num =1):
    f=1
    for c in range(num,0,-1):
        f *= c
    return f

n1 = int(input('Digite um número para saber o fatorial: '))
print(f'O fatorial do número {n1} é {fatorial(n1)}')
