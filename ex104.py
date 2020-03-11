'''
Crie um programa que tenha a função leiaInt(),
que vai funcionar de formar semelhante a função
inpput() do Python, só que fazendo a validação
para aceitar apenas um valor numérico

Ex.:
n = leiaInt('Digite um n')
'''


def leiaInt (f):
    """
    -> Função que lê número inteiros digitados pela teclado.
     Caso o valor digitado não seja inteiro, a função não retornará o valor
    :param f: Mensagem digitada para a leitura de valores inteiros
    :return valor: Retorna o valor inteiro digitado pela teclado
    """
    ok = False
    valor = 0
    while True:
        n = str(input(f))
        if n.isnumeric():
            valor = int(n)
            ok = True
            break
        else:
            print('Digite um valor inteiro')
    return valor


num = leiaInt('Digite um número: ')
