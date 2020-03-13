'''
Exercício 110:
    Crie um pacote chamado utilidadezCeV que tenha dois
    módulos internos chamados moeda e dado.

    Transfira todas as funções utilizadas nos desafios 107,
    108 e 109 para o primeiro pacote e mantenha tudo funcionando.
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


def resumo(n, a=0, b=0, f=True):
    print('=' * 30)
    print(f' {"RESUMO":^25}  ')
    print('-' * 30)
    print(f'{"- Aumento:     ":<5} {aumentar(n, a, f):>10}')
    print(f'{"- Diminuição: ":<5} {diminuir(n, b, f):>10}')
    print(f'{"- Dobro:       ":<5} {dobro(n, f):>10}')
    print(f'{"- Metade:     ":<5} {metade(n, f):>10}')
    print('=' * 30)
