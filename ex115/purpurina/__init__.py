c = ('\033[1;30;44m',  # 0  Fundo azul, letras brancas em negrito.
     '\033[1;30;43m',  # 1  Fundo amarelo, letras brancas em negrito.
     '\033[1;30;7m',   # 2  Fundo branco, letras pretas em negrito.
     '\033[m',         # 3  Fundo e letras padrão.
     '\033[1;30m',     # 4  Branco - negrito
     '\033[1;34m',     # 5  Azul - negrito
     '\033[1m',        # 6  Negrito
     '\033[1;31m'      # 7 Vermelho - Negrito
     )


def cores(f, cor=4):
    global c
    return f'{c[cor]}{f}{c[3]}'


def escreve(msg='', ic='='):
    from time import sleep
    global c
    sleep(0.25)
    print(f'{cores(ic, 4)}'*30)
    print(f'{cores(msg, 4):^40}')
    print(f'{cores(ic, 4)}'*30)
    sleep(0.25)