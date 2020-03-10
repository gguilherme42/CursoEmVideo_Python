'''
Faça um programa que tenha uma função chama área(), que receba as
dimensões de um terreno retangular(largura e comprimento) e mostre a área
do terreno.
'''
def área(x, y):
    a = x * y
    print(f'Largura: {x} m')
    print(f'Comprimento: {y} m')
    print(f'Área: {a:.1f} m²')


l = float(input('Qual a largura do terrerno?  '))
c = float(input('Qual o comprimento do terrerno?  '))
área(l, c)
