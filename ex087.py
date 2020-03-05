'''
Exercício 087

Aprimore o desafio anterior (ex 086), mostrando no final:
a) A soma de todos os valores digitados;
b) A soma de todos os valores da terceira coluna:
c) O maior valor da segunda linha.
'''
dados = []
matriz = []
soma = soma3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        n = int(input('Digite um número: '))
        soma += n
        if c == 2:
            soma3 += n
        dados.append(n)
    matriz.append(dados[:])
    # Varre-se a lista 'dados' porque necessita de novos elementos, sem os anteriores
    # para a nova linha da matriz
    dados.clear()
# Matriz 3x3 na tela
print('-' * 30)
print(f'======{" MATRIZ 3 X 3 ":^4}=====')
for x in matriz:
    # 'x' vira uma lista, portando, deve-se percorre-lô
    for ind, n in enumerate(x):
        print(f'( {n:^4} ) ', end='')
        if ind == 2:
            print()
print('-' * 30)
# a)
print(f'A soma de todos os valores digitados é: {soma}')
# b)
print(f'A soma de todos os valores digitados é: {soma3}')
# c)
print(f'O maior valor da segunda linha  é: {max(matriz[1])}')


