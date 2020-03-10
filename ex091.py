'''
Crie um programa onde 4 jogadores joguem um dado e
tenha resultados aleatórios. Guarde esses resultados em um dicionário.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior
número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter
dados = {'jogador1': randint(1, 6), 'jogador2': randint(1, 6),
         'jogador3': randint(1, 6), 'jogador4': randint(1, 6)}
rank = list()
rank = sorted(dados.items(), key=itemgetter(1), reverse=True)
# Valor do dado de cada jogador
print('='*30)
for k, v in dados.items():
    print(f'{k:<} : {v:<5}')
    sleep(0.5)
# Ranking de jogadores, decrescente
print('='*30)
for i, v in enumerate(rank):
    print(f'{i+1}º Lugar: {v[0]}')
    sleep(0.5)











