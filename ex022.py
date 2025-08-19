nome = input('digite seu nome completo: ')

nome_maiusculo = nome.upper()
nome_minusculo = nome.lower()
 

primeiro_nome = nome.split()
letras_totais = ''.join(primeiro_nome)


print(nome_maiusculo)
print(nome_minusculo)

print(len(primeiro_nome[0]))
print(len(letras_totais))