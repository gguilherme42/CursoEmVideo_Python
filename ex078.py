'''
Programa que cria uma lista com 5 valores númericos lidos pelo teclado.
Mostrando:
a) O maior e o menor valor digitado e suas posições.
'''
#@Guilherme

# Criando a lista com 5 elementos:
lista = list(range(0, 5))
# Declaração de variável para percorrer a lista e atribuir valores inteiros lidos pelo teclado
x = 0
while x < len(lista):
    lista[x] = int(input('Digite um número: '))
    x += 1
print(lista)
# a) Maior e menor valor com as funções max() e min ()
print(f'O maior valor é: {max(lista)}')
print(f'O menor valor é: {min(lista)}')

