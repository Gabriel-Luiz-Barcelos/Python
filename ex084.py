pessoas = list()
dado = list()
while True:
    opcao = ' '
    dado.append(str(input('DIgite o nome da pessoa: ')))
    dado.append(float(input('Digite o peso da pessoa: ')))
    pessoas.append(dado[:])
    dado.clear()
    opcao = str(input('Deseja continuar: [S/N]')).upper().strip()
    if opcao in 'N':
        break
print(f'Você cadastrou {len(pessoas)} pessoas')
maispesado = menospesado = 0
nomepesado = []
nomeleve = []
cont = 0
for i in pessoas:
    if cont == 0:
        maispesado = maisleve = i[1]
        nomepesado.append(i[0])
        nomeleve.append(i[0])
    else:
        if i[1] > maispesado:
            maispesado = i[1]
            nomepesado.clear()
            nomepesado.append(i[0])
        elif i[1] < maisleve:
            maisleve = i[1]
            nomeleve.clear()
            nomeleve.append(i[0]) 
        elif i[1] == maispesado:
            nomepesado.append(i[0]) 
        elif i[1] == maisleve:
            nomeleve.append(i[0])       
    cont+=1              
print(f'O maior peso é {maispesado:.2f}. Peso de {nomepesado}')                 
print(f'O menor peso é {maisleve:.2f}. Peso de {nomeleve}')                 
