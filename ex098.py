from time import sleep

def contagem(ini, fim, passo):
    print('-=' *20)
    print(f'Contagem de {ini} até {fim} em {passo}')
    if passo < 0:
        passo *= -1
    elif passo == 0:
        passo =1    
    if ini > fim:
        passo *= -1 
        fim -= 1
    else:
        fim +=1             
    for i in range(ini,fim,passo):
        print(i, end=' ', flush=True)
        sleep(0.3)
    print('FIM!')  

contagem(1,10,1)       
contagem(10,0,2) 

print('Agora é sua vez de personalizar a contagem! ')
ini = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))

contagem(ini,fim,passo)
