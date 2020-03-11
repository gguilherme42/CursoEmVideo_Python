'''
Faça um programa que tenha um função chama ficha(),
que receba dois parâmetros opcionais: o nome de um
jogador e quantos gols ele marcou.

O programa deverá ser capaz de mostrar a ficha
dp jogador, mesmo que algum dado não tenha sido informado
corretamente

Obs: Caso não sejam informados, os dois parâmetros,
 coloca-se <desconhecido> e 0 gols
'''


def ficha(n='desconhecido', g=0):
    print(f'O jogador {n} fez {g} gols.')


nome = str(input('Nome do jogador: '))
gols = int(input('Gols: '))
ficha(nome, gols)
