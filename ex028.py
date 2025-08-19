import random

num = random.randint(1,5)
print(num)
num_usuario = int(input('adivinhe o número que estou pensando entre 0 e 5: '))

if num_usuario == num:
    print('voce acertou que pensei o numero {} parabens'.format(num))
else:
    print('voce errou')
