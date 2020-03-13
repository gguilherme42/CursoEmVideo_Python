'''
Exercício 107:
    Crie um módulo chamado moeda.py que tenha as funções aumentar(),
    diminuir(), dobro() e metade(). Faça também um programa que importe
    este módulo e algumas funções.
'''def aumentar(n, a):
    c = (n * a) / 100
    l = c + n
    return f'R${l:.2f}'


def diminuir(n, a):
    c = (n * a) / 100
    l = n - c
    return f'R${l:.2f}'


def dobro(n):
    d = n * 2
    return f'R${d:.2f}'


def metade(n):
    m = n / 2
    return f'R${m:.2f}'



