import random
nomes = input('digite os nomes separados por vírgulas: ')
lista = nomes.split(',')
print('o nome sorteado é {}'.format(random.choice(lista)))
