'''
Exercício 086

Crie um programa que crie uma matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado. No final, mostre a matriz na tela,
com a formatação correta.
'''
matriz = []
dados = []
# Repetição dentro de repetição, pois uma matriz 3x3 tem:
# 3 linhas e 3 colunas, assim: 9 elemtentos e duas repetições, aninhadas.
for l in range(0, 3):
    for c in range(0, 3):
        dados.append(int(input('Digite um número: ')))
    matriz.append(dados[:])
    # Varre-se a lista 'dados' porque necessita de novos elementos, sem os anteriores
    # para a nova linha da matriz
    dados.clear()
print('-' * 30)
print(f'======{" MATRIZ 3 X 3 ":^4}=====')
for x in matriz:
    # 'x' vira uma lista, portando, deve-se percorre-lô
    for ind, n in enumerate(x):
        print(f'( {n:^4} ) ', end='')
        if ind == 2:
            print()
print('-' * 30)
