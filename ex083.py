lista = []
paresq= paredir = 0
expressao = str(input('Digite a expressão: '))

for d in expressao:
    if d == '(':
        paresq +=1
    elif d == ')':
        paredir +=1
if paredir == paresq:
    print('Sua expressao está certa!') 
else:
    print('Sua expressao está errada!')               