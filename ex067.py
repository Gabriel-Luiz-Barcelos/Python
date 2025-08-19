cont =1

while True:
    if cont ==1 or cont == 11:
        print('-'*30)
        num = int(input('Quer saber a tabuada de qual número: '))
        print('-'*30)
        cont =1
        if num <0:
            break
    print(f'{num} X {cont} = {num*cont}')
    cont+=1
print('Programa encerrado')    