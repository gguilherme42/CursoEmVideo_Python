'''
Exercício 110:
    Adicione ao módulo moeda.py criado nos desafios anteriores,
    uma função chamada resumo(), que mostre na tela algumas informações
    geradas pela funções que já temos no módulo criado até aqui.
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


def resumo(n, a):
    print('=' * 30)
    print(f' {"RESUMO":^30}  ')
    print('-' * 30)
    print(f'{"- Aumento:     ":<5} {aumentar(n, a):>10}')
    print(f'{"- Diminuição: ":<5} {diminuir(n, a):>10}')
    print(f'{"- Dobro:       ":<5} {dobro(n):>10}')
    print(f'{"- Metade:     ":<5} {metade(n):>10}')
    print('=' * 30)


