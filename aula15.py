soma =0

while True:
    num = int(input('Digite um número: '))
    if num ==999:
        break
    soma+=num
print(f'a soma é {soma}')  

nome = 'gabriel'
idade = 18
salario = 956.635
print(f'{nome[0]} tem {idade} anos e ganha R${salario:.2f}')