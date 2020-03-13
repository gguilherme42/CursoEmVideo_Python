'''
Adapte o código do ex107, criando uma função adicionnal
chamada moeda() que consiga mostrar os valores como um valor
monetário formatado.
'''

def aumentar(n, a):
    c = (n * a) / 100
    l = c + n
    return l


def diminuir(n, a):
    c = (n * a) / 100
    l = n - c
    return l


def dobro(n):
    d = n * 2
    return d


def metade(n):
    m = n / 2
    return m


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
