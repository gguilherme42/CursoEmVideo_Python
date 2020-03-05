'''
Exercício 088

Faça um programa que ajude um jogador da MEGA SENA a criar
palpites. O programa vai perguntar quantos jogos serão
gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''
from random import randint
megasena = []
jogos = int(input('Quantos jogos serão gerados? '))
# Validação da respota, pois esta deve ser maior que zero.
if jogos != 0 and not(jogos < 0):
    # Repetição de palpites para quantidades de jogos
    for x in range(0, jogos):
        # Geradção dos 6 números de 1 até 6 na lista
        palpite = [randint(1, 60), randint(1, 60), randint(1, 60),
                   randint(1, 60), randint(1, 60), randint(1, 60)]
        # Adição do palpite em outra lista
        megasena.append(palpite[:])
        # Limpando o palpite passado
        palpite.clear()
    # Usa-se de um índice para dizer o palpite de cada jogo
    for ind, c in enumerate(megasena):
        print(f'Palpite para o jogo {ind + 1}: \n{c}')
else:
    print('Não pode-se gerar palpites para zero jogos ou menos que zero jogos ')