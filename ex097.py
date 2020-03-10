'''
Faça um programa que tenha uma função chamada
escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável (as linhas de cima e de baixo
acompnham a frase).
Ex:
escreva('Olá, Mundo!')

Saída:
-----------
Olá, Mundo!
-----------
'''

def escreva(str):
    # Obtem-se o comprimento da string
    t = len(str)
    # Depois multiplica-se o traço pelo comprimento 't' da string
    print('-' * t)
    print(str)
    print('-' * t)


frase = str(input('Digite alguma frase: '))
escreva(frase)
