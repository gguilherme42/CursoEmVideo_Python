'''
lEITOR DO ANO DE NASCIMENTO DE 7 PESSOAS, MOSTRANDO QUANTAS NÃO ATINGIRAM A MAIOR IDADE
E QUANTAS ATIGINGIRAM
'''
from datetime import date
maior = 0
menor = 0
for c in range(1, 8):
    nasc = int(input('DIGITE O ANO DE NASCIMENTO DA {}ª PESSOA: '.format(c)))
    id = date.today().year - nasc
    if id >= 21:
        maior += 1
    elif id < 21:
        menor += 1
print('O TOTAL DE PESSOAS COM MAIOR IDADE É {}'.format(maior))
print('O TOTAAL DE PESSOAS COM MENOR IDADE É {}'.format(menor))





