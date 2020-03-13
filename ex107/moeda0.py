'''
Exercício 107:
    Crie um módulo chamado moeda0.py que tenha as funções aumentar(),
    diminuir(), dobro() e metade(). Faça também um programa que importe
    este módulo e algumas funções.
'''

def aumentar(n=0, a=0):
    c = (n * a) / 100
    l = c + n
    return l


def diminuir(n=0, a=0):
    c = (n * a) / 100
    l = n - c
    return f'R${l:.2f}'


def dobro(n):
    d = n * 2
    return f'R${d:.2f}'


def metade(n=0):
    m = n / 2
    return m



