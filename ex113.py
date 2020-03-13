'''
    Reescreva a função leiaInt() do ex104 incluindo, agora,
    a possibilidade de digitação de um número do tipo inválido.
    Aproveite e crie também um função leaiFloat() com a mesma
    funcionalidade.
'''


def leiaInt (f):
    """
    -> Função que lê número inteiros digitados pela teclado.
     Caso o valor digitado não seja inteiro, a função não retornará o valor
    :param f: Mensagem digitada para a leitura de valores inteiros
    :return valor: Retorna o valor inteiro digitado pela teclado
    """
    while True:
        try:
            valor = int(input(f))
        except (ValueError, TypeError):
            print('Erro: Digite um valor inteiro!')
            # continue joga de novo para o while
            continue
        except KeyboardInterrupt:
            return 0
        else:
            # O return quebra o laço
            return valor


def leiaFloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('Erro: Digite um valor real!')
            continue
        except KeyboardInterrupt:
            return 0
        else:
            return valor


n = leiaFloat('Digite um valor real: ')
print(n)
n = leiaInt('Digite um valor inteiro: ')
print(n)
