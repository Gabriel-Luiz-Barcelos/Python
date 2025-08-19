import json
import os
from time import sleep



arquivo = 'pessoas.txt'

def carregarPessoas():
    if os.path.exists(arquivo):
        with open(arquivo, 'r', encoding='utf-8') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []


def salvarPessoas(lista):
    with open(arquivo, 'w', encoding='utf-8') as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)


def adicionarPessoas(lista,nome,idade):
    pessoa = {'nome': nome, 'idade':idade}
    lista.append(pessoa)
    salvarPessoas(lista)
    print('Pessoa adicionada com sucesso!\n')

def removerPessoas():
    situacao = False
    lista = carregarPessoas()

    nome = str(input('Nome para remover: '))
    for i in lista:
        if i['nome'].lower() == nome.lower():
            lista.remove(i)
            salvarPessoas(lista)
            print('Pessoa removida com sucesso') 
            situacao = True
            break    

    if not situacao:
        print(f'Nenhuma pessoa com o nome {nome}')
              
    
               

def mostrarPessoas(lista):
    if not lista:
        print('Nenhuma pessoa adicionada! ') 
    else:
        print('Pessoas cadastradas: ')
        for i, pessoa in enumerate(lista, start=1):
            print(f"{i}. Nome: {pessoa['nome']}, Idade: {pessoa['idade']}") 
        print()            


def menuPrincipal(num):
    listaPessoas = carregarPessoas()

    int(num)
    if num == 1:
        sleep(1)
        mostrarPessoas(listaPessoas)   
        sleep(1)
    if num == 2:
        sleep(1)
        nome = str(input('Nome: '))
        idade = input('Idade: ')
        while True:                
            if idade.isnumeric():
                idade = int(idade)
                break
            else:    
                print('Digite uma idade válida!')
                idade = input('Idade: ')
        adicionarPessoas(listaPessoas,nome,idade)     
    if num == 4:
        removerPessoas()       
          
    
def escritas():
    while True:             
        print('-'*30)
        print('         MENU PRINCIPAL')
        print('-'*30)
        print('1 - Ver pessoas cadastradas')
        print('2 - Cadastrar nova pessoa')
        print('3 - Sair do Sistema')
        print('4 - Remover pessoa do sistema')
        while True:
            num =input('Sua opção: ')   
            try:
                num = int(num)
                if num == 1 or num == 2 or num == 3 or num ==4:
                    break
                else:
                    print('ERRO! Digite novamente!')                
            except:
                print('ERRO! Digite um número inteiro válido')
        if num == 3:
            print('Programa encerrado!')
            break
        menuPrincipal(num)

escritas()
    

