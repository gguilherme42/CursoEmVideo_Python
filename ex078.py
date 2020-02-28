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
# a) Maior e menor valor com as funções max() e min () e posição com .index()
print(f'Maior valor: {max(lista)}, posição: {lista.index(max(lista))}')
print(f'Menor valor: {min(lista)}, posição: {lista.index(min(lista))}')

'''
# Resolução do Guanabara:
lista = []
mai = men = 0
for c in range(0, 5):
    lista.append(int(input(f'Digite um valor para a posição {c}:')))
    if c == 0:
        mai = men = lista[c]
    else:
        if lista[c] > mai:
            mai = lista[c]
        if lista[c] < men:
            men = lista[c]
print(f'Você digitou os valores {lista}')
print(f'O maior valor digitado foi {mai} na posição ', end='')
for i, v in enumerate(lista):
    if v == mai;
            print(f'{i}.... ', end='')
print()
print('O menor valor digitado foi {men} na posição ', end='')
for i, v in enumerate(lista):
    if v == mai;
            print(f'{i}.... ', end='')
print()
'''