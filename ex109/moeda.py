'''
Exercício 109:
'''


def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')


def aumentar(n=0, a=0, f=True):
    c = (n * a) / 100
    l = c + n
    if not f:
        return l
    else:
        return moeda(l)


def diminuir(n=0, a=0, f=True):
    c = (n * a) / 100
    l = n - c
    if not f:
        return l
    else:
        return moeda(l)


def dobro(n=0, f=True):
    d = n * 2
    if not f:
        return d
    else:
        return moeda(d)



def metade(n=0, f=True):
    m = n / 2
    if not f:
        return m
    else:
        return moeda(m)




