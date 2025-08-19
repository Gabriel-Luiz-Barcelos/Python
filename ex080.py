valores = []

for c in range(0,5):
    num = int(input('Digite um número: '))
    
    if c == 0 or num> valores[-1]:
        valores.append(num)
        print('Inserido ao final da lista...')
    else:         
        pos =0
        while pos < len(valores):
            if num <= valores[pos]:
                valores.insert(pos,num)
                print(f'O valor foi inserido na posição {pos}')
                break
            pos+=1
print(f'Os valores digitadoe em ordem foram {valores}')         



