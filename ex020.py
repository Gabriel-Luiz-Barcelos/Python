# import random
# nome = input('digite os nomes separados por vírgulas: ')
# lista = nome.split(',')
# random.shuffle(lista)
# print('a lista dos nomes para apresentar é {}'.format(lista))

import random
n1 = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 = input('ultimo aluno: ')
lista = [n1,n2,n3,n4]
random.shuffle(lista)
print('o sorteio dos alunos é {}'.format(lista))