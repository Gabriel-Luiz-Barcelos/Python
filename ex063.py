n = int(input('Digite um número: '))
m = 0
auxiliar = 0
lista = []


while m < n :
   if m == 1:
      auxiliar = 1
   print(auxiliar,end=' → ')
   lista.append(auxiliar)
   auxiliar += lista[m-1]
   m +=1
print('FIM')  

#Outro jeito sem fazer uma lista que dava pra fazer era
#receber o número de termos n= int(input('digite o numero '))
# t1 =0 e t2=1
#print no t1 e t2
#começa um contador no 3 cont =3
#começa um while cont <=n:
#dentro do while t3 = t1 +t2
#print no t3
#depois atribui t1 =t2 e t2=t3
#cont +=1
#dessa forma em cada loop o t3 vai receber a soma dos dois últimos termos 
# e t1 vai passar a valer o t2 e o t2 vai passar a valer o t3, assim caminhando para frente até o 
# contador chegarno no número digitado pelo usuário