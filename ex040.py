nota1 = float(input('Digite sua nota: '))
nota2 = float(input('Digite sua outra nota: '))

media = (nota1 + nota2) / 2

if media < 5.0:
    print('Você está reprovado')
elif media >= 5.0 and media < 7.0:
    print('Você está de recuperação, sua média foi {}'.format(media)) 
else:
    print('Você está aprovado')
   