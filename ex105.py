'''
Faça um programa que tenha uma função notas()
que pode receber várias notas de alunos e vai
retornar um dicionário com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação(opcional)

Adicione também as docstrings da função
'''


def notas(*n, sit=False):
    t = len(n)
    s = mai = 0
    men = 0
    dicio = {}
    for i, c in enumerate(n):
        if i == 0:
            mai = men = c
        if n[i] > mai:
            mai = c
        if n[i] < men:
            men = c
        s += c
    med = s / t
    dicio['quantidade'] = t
    dicio['maior'] = mai
    dicio['menor'] = men
    dicio['média'] = med
    if sit == True:
        if med >= 7:
            dicio['situação'] = 'BOA'
        else:
            dicio['situação'] = 'RUIM'
    return print(dicio)


notas(1, 2, 3, 5, 6, 7, sit=True)
