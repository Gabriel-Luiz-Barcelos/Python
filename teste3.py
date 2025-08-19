dias = int(input('quantos dias você alugou o carro? '))
km = float(input('quantos km você rodou com o carro? '))

total = dias * 60 + km * 0.15

print('O total a pagar é: R$ {:.2f}'.format(total))