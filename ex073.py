times = ('Flamengo',	
'Cruzeiro',
'Palmeiras',	
'Bahia',	
'Bragantino',	
'Botafogo',	
'Mirassol',	
'São Paulo',	
'Ceará',
'Internacional',	
'Corinthians',
'Fluminense',
'Atlético-MG',
'Grêmio',	
'Vitória',
'Vasco',
'Santos',
'Fortaleza',	
'Juventude',	
'Sport')
for cont in range(0,5):
    print(f'O {cont+1} colocado é {times[cont]}')
#print(f'os 5 primeiros colocados são {times[0:5]}')
print('-'*30)
print(f'Os 4 últimos colocados são:')
#print(times[-4:])

for contb in range(-5,-1):
    print(f'{times[contb]}')

print('-'*30)    
print('Os times em ordem alfábetica ficam: ')
print(sorted(times))



for d in range(0,len(times)):
    if times[d] == 'São Paulo':
        print(f'O São Paulo está na  {d+1}° posição')        
#Dava pra fazer desse jeito também usando o time.index() o index() traz a posição 
print(f'O São Paulo está na {times.index("São Paulo")+1} posição')        