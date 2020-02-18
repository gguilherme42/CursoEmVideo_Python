'''from random import choice
print('\033[1;34m===== Adivinhe o número ====\033[m'.upper())
print('\033[1;30mTente adivinhar um número entre 0 e 10\033[m')
num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tent = 0
resp = -1
while resp != choice(num):
    resp = int(input('\033[1mDigite um número inteiro entre 0 e 10: \033[m'))
    tent += 1
    if resp == choice(num):
        print('\033[1;36mVOCÊ VENCEU! NA {}ª TENTATIVA!\033[m'.format(tent))
    else:
        print('\033[mVOCÊ ERROU! Tente de novo!\033[m')'''
from random import randint
print('\033[1;34m===== Adivinhe o número ====\033[m'.upper())
print('\033[1;30mTente adivinhar um número entre 0 e 10\033[m')
pc = randint(0, 10)
esc = int(input('Palpite: '))
tent = 1
while esc != pc:
    tent += 1
    if esc < pc:
        print('Mais....')
    elif esc > pc:
        print('Menos...')
    esc = int(input('Palpite: '))
print('VOCÊ GANHOU NA {}ª TENTATIVA, PARABÉNS!'.format(tent))