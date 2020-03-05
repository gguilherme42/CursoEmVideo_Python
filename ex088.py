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
for x in range(0, jogos):
    palpite = [randint(1, 60), randint(1, 60), randint(1, 60),
               randint(1, 60), randint(1, 60), randint(1, 60)]
    megasena.append(palpite[:])
    palpite.clear()
for ind, c in enumerate(megasena):
    print(f'Palpile {ind + 1}: \n{c}')
