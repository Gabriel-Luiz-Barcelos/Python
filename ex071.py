print('='*30,'\nBANCO CEV\n','='*30)


notas50 = notas20 = notas10 = notas5 =notas2 =0


valor = int(input('Qual valor você quer sacar? R$ '))
while True:
    if valor // 50 !=0:
        notas50 +=1
        valor -= 50
    elif valor // 20 !=0:
        notas20 +=1
        valor -= 20
    elif valor // 10 != 0:
        notas10 += 1
        valor -= 10
    elif valor // 5 !=0:
        notas5 +=1    
        valor -= 5
    elif valor // 2 !=0:
        notas2 +=1
        valor -= 2

    if valor == 0:
        break    
print(f'Total de {notas50} cédulas de R$ 50')    
print(f'Total de {notas20} cédulas de R$ 20')  
print(f'Total de {notas10} cédulas de R$ 10')  
print(f'Total de {notas5} cédulas de R$ 5')  
print(f'Total de {notas2} cédulas de R$ 2')  
print('='*30)
print('Volte sempre ao banco CEV! Tenha um ótimo dia')    
