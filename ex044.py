preco = float(input('digite o preço do produto: '))
opcao = int(input("""Você deseja pagar no dinheiro ou no cartão?
Digite 1 para dinheiro ou 2 para cartão: """ ))

if opcao == 1:
    preco = preco - (preco * 10 /100)
    print('O valor a ser pago à vista no dinheiro é {:.2f}'.format(preco))
elif opcao == 2:
    opcao2 = input('Você gostaria de pagar à vista no cartão? (y/n)')
    if opcao2 == 'y':
        preco = preco - (preco * 5/100)
        print('O valor a ser pagao à vista no cartão é {:.2f}'.format(preco))
    elif opcao2 == 'n':
        opcao3 = int(input('quantas vezes no cartão? '))
        if opcao3 <= 2:
            print('O preco a ser pago parcelado no cartão até 2 vezes é de {}'.format(preco))   
        elif opcao3 > 2:
            preco = preco + (preco * 20 /100)
            print('O preco a ser pago parcelado no cartão em mais de 2 vezes é {}'.format(preco))    
        else:
            print('opção inválida')
    else:
            print('opção inválida')
else:
            print('opção inválida')            