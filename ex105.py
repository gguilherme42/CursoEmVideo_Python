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
    """
    -> Função para calcular notas, onde:
        - É calculado a maior nota
        - É calculado a menor nota
        - É calculado a média
        - É calculado a situação
    :param *n: múltiplos parâmetros numéricos
    :param sit: (opcional) se True, mostra a situação de acordo com as notas
    :return: retorna um dicionário com o que foi calculado
    """
    dicio = {}
    dicio['quantidade'] = len(n)
    dicio['maior'] = max(n)
    dicio['menor'] = min(n)
    dicio['média'] = sum(n) / dicio['quantidade']
    # Se 'sit' for verdadeiro
    if sit:
        if dicio['média'] >= 7:
            dicio['situação'] = 'BOA'
        elif 4 > dicio['média'] < 7:
            dicio['situação'] = 'RAZOÁVEL'
        else:
            dicio['situação'] = 'RUIM'
    return dicio


notas(1, 2, 3, 5, 6, 7, sit=True)
print(notas)

