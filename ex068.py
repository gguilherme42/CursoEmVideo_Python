'''
PAR OU IMPAR COM O COMPUTADOR
'''
# Importando função para 'sortear' números
from random import randint
from time import sleep
pc = randint(0, 2)
v = 0
#loop central do jogo
while True:
    print('\033[1m=\033[m'*20)
    print(' PAR OU IMPAR ')
    print('\033[1m=\033[m' * 20)
    # Validação da resposta
    while True:
        poi = int(input('''\033[1mEscolha: \033[1;33m[1]\033[1;30m IMPAR \033[1;33m[2]\033[1;30m PAR\033[m\n'''))
        if poi != 1 and poi != 2:
            print('Resposta inválida!')
        else:
            break
    # Validação da resposta
    while True:
        n = int(input('Digite 0, 1 ou 2: '))
        if n != 1 and n != 2:
            print('\033[1;31mResposta inválida!\033[m')
        else:
            break
    sleep(1)
    print('\033[1;34mProcessando... \033[m')
    sleep(1)
    print('\033[30m--\033[m'*10)
    # Mostrar na tela as escolhas
    if poi == 2:
        print('\033[1;33mUsuário \033[1;30m[PAR]: %d\033[m' % n)
        print('\033[1;33mPC    \033[1;30m[IMPAR]: %d\033[m' % pc)
    else:
        print('\033[1;30mUsuário [PAR]: \033[1m%d \033[m' % n)
        print('\033[1;30mPC    [IMPAR]: \033[1m%d \033[m' % pc)
    print('\033[30m--\033[m'*10)
    sleep(1)
    print('\033[1;34mCalculando resultado... \033[m')
    sleep(1)
    # Condição para vitória, caso o usuário escolha PAR
    if poi == 2 and ((pc + n) == 4 or (pc + n) == 2):
        print('\033[1;33mVocê venceu!\033[m')
        v += 1
    # Condição para vitória, caso o usuário escolha IMPAR
    if poi == 1 and ((pc + n) == 3 or (pc + n) == 1):
        print('\033[1;33mVocê venceu!\033[m')
        v += 1
    else:
        print('\033[1;33mVocê perdeu! \033[m')
        break
print('''
\033[mTotal de vitórias: \033[1;30m%d \033[m
''' % v)
