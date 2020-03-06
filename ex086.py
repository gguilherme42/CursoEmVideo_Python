'''
Exercício 086

Crie um programa que crie uma matriz de dimensão 3x3 e preencha
com valores lidos pelo teclado. No final, mostre a matriz na tela,
com a formatação correta.
'''
matriz = []
# Repetição dentro de repetição, pois uma matriz 3x3 tem:
# 3 linhas e 3 colunas, assim: 9 elemtentos e duas repetições, aninhadas.
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}]: '))
print('-' * 30)
print(f'======{" MATRIZ 3 X 3 ":^4}=====')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'( {matriz[l][c]:^5} ) ', end='')
    # Quando o número de colunas finalizar, será pulado uma linha
    print()
print('-' * 30)


