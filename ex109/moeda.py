'''
Exercício 109:
    Modifique as funções que foram criadas o desafio 107 para que elas aceitem
    um parâmetro a mais, informando se o valor passado para elas vai ser ou não
    formatado pela função moeda() criada no exercício 108.
'''


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def aumentar(n=0, a=0, f=True):
    c = (n * a) / 100
    l = c + n
    return l if not f else moeda(l)


def diminuir(n=0, a=0, f=True):
    c = (n * a) / 100
    l = n - c
    return l if not f else moeda(l)


def dobro(n=0, f=True):
    d = n * 2
    return d if not f else moeda(d)


def metade(n=0, f=True):
    m = n / 2
    return m if not f else moeda(m)
