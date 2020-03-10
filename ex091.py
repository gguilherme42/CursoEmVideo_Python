'''
Crie um programa onde 4 jogadores joguem um dado e
tenha resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado.
'''

from random import randint
from time import sleep
jogadores = list(range(0, 4))
dados = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
         'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
for k, v in dados.items():
    print(f'{k:<} : {v:<5}')
    sleep(0.5)
for k, v in dados.items():
    if v == max(dados.values()):
        print(f'1º Lugar: {k} com {v}')









