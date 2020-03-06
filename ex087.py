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
        n = int(input(f'Digite um número para [{l}, {c}]: '))
        if n % 2 == 0:
            somap += n
        # Soma dos números da terceira coluna:
        if c == 2:
            soma3 += n
        matriz[l][c] = n
# Matriz 3x3 na tela
print('-' * 30)
print(f'======{" MATRIZ 3 X 3 ":^4}=====')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'( {matriz[l][c]:^5} ) ', end='')
    print()
print('-' * 30)
# a)
print(f'A soma de todos os valores digitados é: {somap}')
# b)
print(f'A soma de todos os valores digitados é: {soma3}')
# c)
print(f'O maior valor da segunda linha  é: {max(matriz[1])}')


