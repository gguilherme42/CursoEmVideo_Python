'''
Crie um programa que tenha a função leiaInt(),
que vai funcionar de formar semelhante a função
inpput() do Python, só que fazendo a validação
para aceitar apenas um valor numérico

Ex.:
n = leiaInt('Digite um n')
'''


def leiaInt(f, n=0):
    while True:
        n = input(f)
        if type(n) != int:
            print('Digite um valor inteiro')
        else:
            break
    return n


num = leiaInt('Digite um número: ')

