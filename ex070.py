print('-'*30,'\nLOJA SUPER BARATÃO\n','-'*30)
total =0
maisquemil = 0
maisbarato= 0
nomembarato =''

contador = 0
while True:
    nproduto = str(input('Digite o nome do produto: '))
    preco = float(input('Digite o preço do produto: '))
    escolha =' '
    while escolha not in 'SN':
        escolha = input('Quer continuar: [S/N]').upper().strip()[0]
    total += preco
    contador+=1
    if contador ==1:
        maisbarato = preco
        nomembarato = nproduto
    if preco > 1000:
        maisquemil +=1
    if preco < maisbarato:
        maisbarato = preco
        nomembarato = nproduto
    if escolha in 'N':
        break
    
print(f'O total gasto na compra é {total}\n{maisquemil} produtos custam mais que R$1000 reais\nO nome do produto mais barato é {nomembarato} custando R${maisbarato:.2f} ')    

