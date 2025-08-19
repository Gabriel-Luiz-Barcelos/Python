aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média do {aluno["nome"]}: '))
if aluno['média'] >= 7.0:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >=5:
    aluno['situação'] = 'Recuperação'  
else:
    aluno['situação'] = 'Reprovado'    

for k,v in aluno.items():
    print(f'{k} é igual a {v}')