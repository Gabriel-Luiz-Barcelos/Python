def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[;31mValor digitado inválido, digite outro valor correto:\033[m ')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuários')
            return 0
        else: 
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[;31mValor digitado inválido, digite outro valor correto:\033[m ')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuários')
            return 0
        else: 
            return n
       
numint = leiaint('Digite um valor: ')
numfloat = leiafloat('Digite um número real: ')
print(f'O número inteiro digitado foi {numint} e o número real {numfloat}')


