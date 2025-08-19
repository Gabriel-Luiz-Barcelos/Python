from datetime import date

pessoa = dict()

ano_atual = date.today().year

nome = str(input('Digite seu nome: '))
ano_nasc = int(input('Digite seu ano de nascimento: '))
ctps = int(input('Digite número carteira de trabalho (0 não tem): '))
if ctps != 0:
    ano_contratação = int(input('Ano de contratação: '))
    salario = float(input('Digite seu salário: '))

    idade = ano_atual - ano_nasc
    idade_aposentadoria = (ano_contratação - ano_nasc) + 35

    pessoa['nome'] = nome
    pessoa['idade'] = idade
    pessoa['ctps'] = ctps
    pessoa['contratação'] = ano_contratação
    pessoa['salário'] = salario
    pessoa['aposentadoria'] = idade_aposentadoria

    for k,v in pessoa.items():
        print(f'- {k} tem o valor {v}')
else:
    idade = ano_atual - ano_nasc
    pessoa['nome'] = nome
    pessoa['idade'] = idade
    pessoa['ctps'] = ctps  

    for k,v in pessoa.items():
        print(f'- {k} tem o valor {v}')

