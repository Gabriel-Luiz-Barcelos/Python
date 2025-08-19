lista = list()
nomes = list()
notas = list()
a = 0

while True:
    opcao = ' '
    nomes.append(str(input('Digite o nome do aluno: ')))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    
    lista.append(nomes[:])
    nomes.clear()

    lista[a].append(notas[:])
    notas.clear()


    while opcao not in 'SN':
        opcao = str(input('Quer continuar? ')).strip().upper()
    if opcao in 'N':
        break
    
    a += 1
c = 0
for b in lista:
    print(lista[c][0])       
    c += 1

listamedia = list()
media = 0
e = 0
for d in lista:
    media = ( lista[e][1][0] + lista[e][1][1] ) / 2
    listamedia.append(media)
    e += 1

for f in listamedia:
    print(f)

print('-=' * 20)    

print(f'{"No.":<4}',end=' ')
print(f'{"Nome":<10}',end=' ')
print(f'{"MÉDIA":>8}')
print('-'*30)
j = 0
for g in range(0,len(lista)):
    print(f'{g:<4}',end=' ')
    print(f'{lista[j][0]:<15}',end=' ')
    print(f'{listamedia[j]:.1f}')
    j+=1 

print('-'*30)


notasQuem = 0

while notasQuem != 999:
    notasQuem = int(input('Mostrar notas de qual aluno ? (999 interrompe): '))
    if notasQuem == 999:
        break
    print(f'Notas de {lista[notasQuem][0]} são {lista[notasQuem][1]}')

print('Programa finalizado')    
            