def fatorial(num, show=0):
    """
    fatorial(n, show=False)
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fat = 1
    for c in range(num,0,-1):
        fat *= c
        if show:
            if c ==1:
                print(f'{c} =',end=' ')
            else:        
                print(f'{c} x',end=' ')
    return fat    

print(fatorial(5,show=True))   

help(fatorial)