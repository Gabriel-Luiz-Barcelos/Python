nome = str(input('qual é seu nome: ')).lower()
if nome == 'gabriel':
    print('que nome bonito')
elif nome in ('ana claudia jessica juliana'):
    print('seu nome feminino é bonito')
else:
    print('seu nome é bem comum')    
print('tenha um bom dia {}'.format(nome))