'''
Crie um programa que tenha a função leiaInt(),
que vai funcionar de formar semelhante a função
inpput() do Python, só que fazendo a validação
para aceitar apenas um valor numérico

Ex.:
n = leiaInt('Digite um n')
'''


def leiaInt(n):
    while True:
        n = input('Digite um número: ')
        if n != int:
            print('Digite um valor inteiro')
        else:
            break
    return n


num = leiaInt('Digite um número: ')

