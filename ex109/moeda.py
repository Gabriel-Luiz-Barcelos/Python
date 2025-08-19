def moeda(param):
    return f'R${param:>8.2f}'.replace('.',',')

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