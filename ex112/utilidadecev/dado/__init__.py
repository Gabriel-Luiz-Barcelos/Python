def leiaDinheiro(valor):
    valido = False
    while not valido:
        entrada = str(input(valor)).strip().replace(',','.')
        if entrada.isalpha() or entrada== '':
            print(f'\033[;31mERRO: \"{entrada}\"é um preco inválido!\033[m ')
        else:
            valido = True
            return float(entrada)
            
