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
     É calculado a maior nota.
     É calculado a menor nota.
     É calculado a média.
     É calculado a situação.
    :param *n: múltiplos parâmetros numéricos.
    :param sit: (opcional) se True, mostra a situação de acordo com as notas.
    :return: retorna um dicionário com o que foi calculado.
    """
    l = dict()
    l['quantidade'] = len(n)
    l['maior'] = max(n)
    l['menor'] = min(n)
    l['média'] = sum(n) / l['quantidade']
    # Se 'sit' for verdadeiro
    if sit:
        if l['média'] >= 7:
            l['situação'] = 'BOA'
        elif l['média'] >= 5:
            l['situação'] = 'RAZOÁVEL'
        else:
            l['situação'] = 'RUIM'
    return l


notas(1, 2, 3, 5, 6, 7)
print(notas)
