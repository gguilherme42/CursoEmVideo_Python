'''
Faça um programa que tenha uma função chamada
maior(), que receb vários parâmetros com valores inteiros.
Seu programa tem que analizar todos os valores e dizer qual deles
é o maior.
'''
# Função com um único parâmetro, pois será passado uma lista como parâmetro.
def maior(num):
    mai = 0
    for i, n in enumerate(num):
        if i == 0:
            mai = n
        elif num[i] > mai:
            mai = num[i]
    print(f'O maior número é: {mai}')

lista = []
while True:
    d = int(input('Digite um número: '))
    lista.append(d)
    # Validação da pergunta
    while True:
        p = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if p in 'SN':
            break
        else:
            print('Resposta inválida!')
    if p in 'N':
        break
# Colocando na tela o maior número da lista
maior(lista)
