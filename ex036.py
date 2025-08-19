casa = float(input('Qual o valor da casa: '))
salario = float(input('Digite seu salario: '))
anos = int(input('Em quantos anos você vai pagar: '))

prestacao = casa / (anos * 12)
print(prestacao)
if salario * 30 /100 >= prestacao:
    print('exemprestimo aprovado, o valor da parcela é {:.2f} para pagar em {} anos a casa de {:.2f}'.format(prestacao,anos,casa))
else:
    print('Para pagar uma casa de {:.2f} em {} anos a prestação será de R${:.2f}\nempréstimo negado!'.format(casa,anos,prestacao))    