num = int(input('Digite um número para ser convertido: '))
opcao = int(input("""Escolha uma das opções para ser convertido
1 - Digite 1 para Binário
2 - Digite 2 para Octal
3 - Digite 3 para Hexadecimal
 """))

if opcao == 1:
    print('O número {} convertido para Binário é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('O número {} convertido para Octal é {}'.format(num, oct(num)[2:]))    
elif opcao == 3:
    print('O número {} convertido para Hexidecimal é '.format(num,hex(num)[2:]))    
else:
    print('Opção inválida')    