
def notas(*num, sit=0):
    """ 
    -> Função para analisar notas e situações de vários alunos.
    :param num: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a turma 
    """

    dicNotas = dict()
    dicNotas['total'] = len(num)
    dicNotas['maior'] = max(num)
    dicNotas['menor'] = min(num)
    dicNotas['media'] = sum(num)/len(num) 
    if sit == True:
        if dicNotas['media'] > 7:
            dicNotas['situação'] = 'BOA'
        elif dicNotas['media'] <7 and dicNotas['media'] >5:
            dicNotas['situação'] = 'RAZOAVEL' 
        else:
            dicNotas['situação'] = 'RUIM'       

    return dicNotas

resp = notas(5.5, 2.5, 1.5,sit=True)
print(resp)   
help(notas) 
    
