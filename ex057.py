s = 'J'

while s != 'M' and s != 'F':  #Podia usar while s not in 'MF'
    s = str(input('Digite seu sexo? [M/F]')).upper().strip()[0]
    
if s == 'M':
    print('Seu sexo é masculino')
else:
    print('Seu sexo é feminino')    