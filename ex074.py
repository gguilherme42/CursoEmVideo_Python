'''
Programa que gera 5 números aleatórios em uma tupla.
Mostrando:
a) A listagem dos números;
b) O maior e o menor número.
'''
'''
@Guilherme
Minha primeira resolução, sem olhar os vídeos de exercícios: 
'''
from random import randint
# Variáveis simples receberam números aleatórios, dado que: tuplas são imutáveis
n1 = randint(0, 100)
n2 = randint(0, 100)
n3 = randint(0, 100)
n4 = randint(0, 100)
n5 = randint(0, 100)
tupla = (n1, n2, n3, n4, n5)
# a) Números listados em ordem
print(sorted(tupla))
# b)
# Declaração das variáveis simples maior e menor
maior = menor = 0
# Repetição para percorrer a tupla e indicar qual o maior e o menor número
#  'ind' representa o índice da tupla e 'c' a variável auxiliar para percorrer a tupla e mostrar o objeto dela
for ind, c in enumerate(tupla):
    # Se o índice da lista for igual à 1, então:
    if ind == 1:
        maior = c
        menor = c
    else:
        if c > maior:
            maior = c
        elif c < maior and c < menor:
            menor = c
print(f'O maior número é {maior} e o menor número é {menor}.')

'''
Resolução do @Guanabara:
from random import randint
numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'Os valores sorteados foram: {numeros}')
print(f'O maior valor foi: {max(numeros)}')
print(f'O menor valor foi: {min(numeros)}')
'''