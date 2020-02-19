'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são suas vogais.

Resulução do @Guanabara resumida
'''
tupla = ('pao', 'mochila', 'roupa')
for palavra in tupla:
    print(f'\nNa palavras {palavra.upper()} temos: ', end='')
    for letra in palavra:
        if letra.lower() in 'aeiou':
            print(f'{letra}', end=' ')
