def moeda(param):
    return f'R${param:>8.2f}'.replace('.',',')

def  metade(n):
    return n /2

def  dobro(n):
    return n * 2

def  aumentar(n,aum):
    return n * (1 +(aum/100))

def  diminuir(n,dim):
    return n - ((n* dim) /100)    