filme = {
    'titulo':'Star Wars',
    'ano': 1977,
    'diretor': 'George Lucas'
}

print(filme.values())
print(filme.keys())
print(filme.items())

print('-='*15)

for k,v in filme.items():
    print(f'O {k} é {v}')

print('-'*15)

locadora = list()    

locadora.append(filme)
print(locadora)
print(locadora[0]['titulo'])

print('-'*15)

pessoas = {'nome': 'Gustavo', 'sexo': 'M', 'idade': 19, 'altura':1.75}
print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos')

del pessoas['sexo']

for a in pessoas.values():
    print(a)
pessoas['nome'] = 'leandro'
pessoas['peso'] = 98.8
for b,c in pessoas.items():
    print(f'{b} = {c}')    

print('-'*15)

estado1 = {'uf': 'Rio de Janeiro', 'sigla': 'RJ'}
estado2 = {'uf': 'São Paulo', 'sigla': 'SP'}

listaestados = list()
listaestados.append(estado1)
listaestados.append(estado2)

print(listaestados)
print(listaestados[0])
print(listaestados[1])

print('-' * 15)

estado = dict()
brasil = list()

for c in range(0,3):
    estado['uf'] = str(input('Qual é o estado: '))
    estado['sigla'] = str(input('Qual o estado: '))
    brasil.append(estado.copy())

for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem o valor {v}') 

print('='*20)
