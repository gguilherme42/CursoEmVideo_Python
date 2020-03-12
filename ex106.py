'''
Faça um mini-sistema que utilize o
Interactive Help do Python. O usuário
vai digitar o comando e o manual vai aparecer.
Quando o usuário digitar a palavra 'FIM' o programa
se encerrará.

Obs: Use cores.
'''
c = ('\033[1;30;44m',  # 0 - Fundo azul, letras brancas em negrito.
     '\033[1;30;43m',  # 1 - Fundo amarelo, letras brancas em negrito.
     '\033[1;30;7m',   # 2 - Fundo branco, letras pretas em negrito.
     '\033[m',   # 3 - Fundo e letras padrão.
     )


def tit(f, cor=3):
    global c
    t = len(f) + 4
    print(c[cor], end='')
    print('~' * t)
    print(f'    {f}')
    print('~' * t)
    print(c[3], end='')


def minis(n):
    from time import sleep
    tit(f'Acessoando o  comando {n}', 0)
    sleep(0.5)
    # Não se usa a função tit() no help, porque ele mostra um texto extenso
    print(c[2], end='')
    print(help(n))
    print(c[3], end='')


while True:
    tit('SISTEMA DE AJUDA PyHELP', 1)
    com = str(input('Função ou Biblioteca >'))
    if com.upper() == 'FIM':
        break
    else:
        minis(com)
tit('ATÉ LOGO!')
