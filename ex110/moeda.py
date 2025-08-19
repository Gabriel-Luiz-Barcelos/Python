def moeda(param):
    return f'R${param:.2f}'.replace('.',',')

def  metade(n,format=False):
    res = n /2 
    return res if format == False else moeda(res)

def  dobro(n,format=False):
    res = n * 2
    return res if format == False else moeda(res)
def  aumentar(n,aum,format=False):
    res = n * (1 +(aum/100))
    return res if format == False else moeda(res)
def  diminuir(n,dim,format=False):
    res = n - ((n* dim) /100)           
    return res if format == False else moeda(res)

def resumo(p, aumento=0,reducao=0):
    print('-'*35)
    print('          RESUMO DO VALOR')
    print('-'*35)
    print(f'Preco analisado: \t{moeda(p)}')  
    print(f'Dobro do preço: \t{dobro(p,True)}')  
    print(f'Metade do preço: \t{metade(p,True)}')  
    print(f'{aumento}% de aumento: \t{aumentar(p,aumento,True)}')  
    print(f'{reducao}% de redução: \t{diminuir(p,reducao,True)}')  
    print('-'*35)
