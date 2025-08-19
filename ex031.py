km = int(input('quantos km é a viagem? '))

if km <= 200:
    valor = km *0.50
else:
    valor = km *0.45
print('O valor total da viagem é R$ {:.2f}'.format(valor))

