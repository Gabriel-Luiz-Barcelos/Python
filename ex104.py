def leiaint(num):
    if num.isnumeric():
        return num
    else:
        while True:
            print('\033[31mERRO! Digite um número inteiro válido\033[m')
            num = input('Digite um número: ')
            if num.isnumeric():
                return num
                         

n = leiaint(input('Digite um número: '))
print(f'Você acabou de digitar o número {n}')

