teste = list()
teste.append('Gabriel')
teste.append(40)
print(teste)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
print('=-'*20)
pessoas = [['Joao',19], ['Ana',33], ['Joaquim',13 ],['Maria',45]]
print(pessoas[0][0])
print(pessoas[2][1])

for p in pessoas:
    print(f'{p[0]} com idade {p[1]}')

print('-='*30)    

outraspessoas = list()
dado = list()
totmaior = totmenor = 0
for c in range(0,3):
    dado.append(str(input('Digite o nome: ')))
    dado.append(int(input('Digite a idade: ')))
    outraspessoas.append(dado[:])
    dado.clear()
for r in outraspessoas:
    if r[1] >= 21:
        print(f'{r[0]} é de maior') 
        totmaior +=1
    else:
        print(f'{r[0]} é menor de idade')        
        totmenor +=1

print(f'Temos {totmaior} de maior')
print(f'Temos {totmenor} de menor')