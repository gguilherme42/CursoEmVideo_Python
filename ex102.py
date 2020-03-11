'''
Crie um programa que tenha uma função fatorial() que
receba dois parâmetros: o primeiro que indique
o nḿero a calcular e o outro chamado show,
que será um valor lógico (opcional) indicando se
será mostrado ou não na tela o processo de cálculo fatorial.

obs: função deve ser documentada
'''


def fatorial(num=1, show=False):
    """
    -> Função para calcular o fatorial de um número
    :param num: O número a ser calculado.
    :param show: (opcional) Mostra ou não a conta.
    :return: retorna o valor do fatoria de um número.
    """
    f = 1
    if show == True:
        for c in range(num, 0, - 1):
            if c > 1:
                print(f'{c} x ', end='')
            else:
                print(f'{c} =', end=' ')
            f *= c
        return print(f'{f}')
    else:
        for c in range(num, 0, - 1):
            print(f'{c} x ', end='')
            f *= c
        return f


n = int(input('Fatorial de qual número: '))
p = str(input('Quer ver o processo? [S/N] ')).strip().upper()[0]
if p in 'S':
    fatorial(n, show=True)
else:
    fatorial(n)
