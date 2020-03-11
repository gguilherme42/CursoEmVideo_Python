'''
Faça um programa que tenha uma função chamada
maior(), que receb vários parâmetros com valores inteiros.
Seu programa tem que analizar todos os valores e dizer qual deles
é o maior.
'''
from random import randint
from time import sleep


# Função com um único parâmetro, pois será passado uma lista como parâmetro.
def maior(num):
    mai = 0
    print('-'*30)
    # Se a lista tiver comprimento, então:
    if len(num) != 0:
        for i, n in enumerate(num):
            if i == 0:
                mai = n
            elif num[i] > mai:
                mai = num[i]
        print('Analisando valores...')
        sleep(0.5)
        for c in num:
            print(f'{c}', end=' ', flush=True)
            sleep(0.5)
        print()
        print(f'Total de números: {len(num)}')
        print(f'O maior número é: {mai}')
    else:
        print('Analisando valores...')
        sleep(0.5)
        print('Lista vazia')
    print('-'*30)


for c in range(0, 4):
    # Cria uma lista vazia, com comprimento gerado pelo randint
    lista = list(range(randint(0, 10)))
    # Repetição que percorre a lsita genéria
    for i, v in enumerate(lista):
        lista[i] = randint(0, 100)
    # Colocando na tela o maior número da lista para 4 listas diferentes
    maior(lista)
