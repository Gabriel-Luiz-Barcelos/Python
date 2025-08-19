from time import sleep

def maior(* num):
    maior = 0
    
    for i in range(0,len(num)):
        if i == 0:
            maior = num[i]
        else:
            if num[i] > maior:
                maior = num[i]
      
    print('-=' * 20)
    print('Analisando os valores passados ...') 
    for c in num:
        print(c,end=' ',flush=True)  
        sleep(0.5)             
    print(f'Foram informados {len(num)} valores ao todo')
    print(f'O maior valor informado foi {maior}')        

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1,2)
maior(6)
maior()

