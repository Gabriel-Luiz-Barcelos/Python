def area(lar, compr):
    area = lar * compr
    print(f'A área de um terreno {lar}x{compr} é de {area}m²')

print('Controle de Terrenos')
print('-'*20)
lar = float(input('LARGURA (m): '))
compr = float(input('COMPRIMENTO (m): '))

area(lar, compr)