'''
Exercício 087

Aprimore o desafio anterior (ex 086), mostrando no final:
a) A soma de todos os valores pares digitados;
b) A soma de todos os valores da terceira coluna:
c) O maior valor da segunda linha.
'''
matriz = [list(range(0, 3)), list(range(0, 3)), list(range(0, 3))]
somap = soma3 = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um número para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            somap += matriz[l][c]
        # Soma dos números da terceira coluna ([2]):
        if c == 2:
            soma3 += matriz[l][c]
# Matriz 3x3 na tela
print('-' * 30)
print(f'======{" MATRIZ 3 X 3 ":^4}=====')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'( {matriz[l][c]:^5} ) ', end='')
    print()
print('-' * 30)
# a)
print(f'A soma de todos os valores pares digitados é: {somap}')
# b)
print(f'A soma de todos os valores digitados na terceira coluna é: {soma3}')
# c)
# Segunda linha = matriz[1]
print(f'O maior valor da segunda linha  é: {max(matriz[1])}')


