#MINHA RESOLUÇÃO:
from random import choice
from time import sleep
print('\033[1;35m-----\033[m'*40)
print('\033[1;32m  JOKENPÔ    \033[m'*15)
print('\033[1;35m-----\033[m'*40)
user = int(input('\033[1mESCOLHA: \n[1]PEDRA, [2] PAPEL OU [3] TESOURA \n'))
if user == 1:
    esc = 'PEDRA'
elif user == 2:
    esc = 'PAPEL'
elif user == 3:
    esc = 'TESOURA'
else:
    esc = 'INVÁLIDO'
list = ['PEDRA', 'PAPEL', 'TESOURA']
pc = choice(list)
print('\033[1mPROCESSANDO.....\033[m')
sleep(2)
print('\033[1m......\033[m')
sleep(1)
print('\033[1mESCOLHAS: \nUSURÁRIO: {} \nCOMPUTADOR: {}\033[m'.format(esc, pc))
    if (user == 1 and pc == 'PEDRA') or (user == 2 and pc == 'PAPEL') or (user == 3 and pc == 'TESOURA'):
        print('\033[1;33mEMPATOU!\033[m')
    elif (user == 2 and pc == 'PEDRA') or (user == 1 and pc == 'TESOURA') or (user == 3 and pc == 'PAPEL'):
        print('\033[1;33mVOCÊ GANHOU!\033[m')
    elif (user == 3 and pc == 'PEDRA') or (user == 2 and pc == 'TESOURA') or (user == 1 and pc == 'PAPEL'):
        print('\033[1;33mVOCÊ PERDEU!\033[m')
    else:
        print('VOCÊ NÃO FEZ UMA ESCOLHA CORRETA!')


#Começo do código do Guanabara:
'''
from rando import randint
itens = ('PEDRA', 'PAPEL', 'TESOURA')
pc = randint(0, 2)
print('''Sua opções
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual é a sua jogada? '))
print('PC JOGOU: {}'.format(itens[pc]))
print('VOCÊ JOGOU: {}'.format(itens[jogador]))
......(continuação).....'''
