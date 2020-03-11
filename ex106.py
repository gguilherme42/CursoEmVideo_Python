'''
Faça um mini-sistema que utilize o
Interactive Help do Python. O usuário
vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM' o programa
se encerrará.

Obs: Use cores.
'''
dicio = {'fAzul': '\033[1;30;44m', 'fAma': '\033[1;30;43m',
        'fBran': '\033[1;7;30m', 'fP': '\033[m'}

def sys(f):
    global dicio
    c = len(f)
    print(end=f'{dicio["fP"]}')
    print(f'{dicio["fAma"]}~' * c)
    print(f'{f}')
    print('~' * c)
    print(end=f'{dicio["fP"]}')

def minis(n):
    global dicio
    fra = f'Acessando o manual do comeando {n}'
    t = len(fra)
    print(f'{dicio["fAzul"]}~' * t)
    print(f'{fra}')
    print('~' * t)
    print(f'{dicio["fP"]}', end='')
    print(f'{dicio["fBran"]}')
    print(f'{help(n)}')


while True:
    sys('   SISTEMA DE AJUDA PyHELP   ')
    sis = str(input('Função ou Biblioteca >'))
    if sis in 'FIM':
        break
    else:
        minis(sis)
