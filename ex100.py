'''
Faça um programa que tenha uma lista chamada
números e duas funções chamadas sorteia() e
somaPar(). A primeira função vai sortear 5 números e vai colocá-los
dentro da lista e a segunda função vai mostrar a soma entre todos os valores
PARES sorteador pela função anterior.
'''
from random import randint

# Função sorteia retorna valor, neste caso, uma lista com novos valores.
def sorteia(l):
    # Repetição genérica para sortear valor em qualquer lista
    for i, v in enumerate(l):
        v = randint(0, 100)
    return l


def somaPar(x):
    soma = 0
    for p in x:
        if p % 2 == 0:
            soma += p
    print(f'A soma dos pares é: {soma}')


lista = [randint(0, 100), randint(0, 100), randint(0, 100),
         randint(0, 100), randint(0, 100)]
print(lista)
print(f'A lista sorteda é:\n{sorteia(lista)}')
somaPar(lista)
