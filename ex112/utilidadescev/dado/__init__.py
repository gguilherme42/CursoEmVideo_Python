'''
Exercício 112:
   Dentro do pacote utilidadesCev que criamos no desafio 111,
    temos um módulo chamado dado. Crie um função chamada
    leiaDinheiro() que seja capaz de funcionar como a função
    input(), mas com uma validação de dados para aceitar apenas valores
    que sejam monetários.
'''


def leiaDinheiro(msg):
    while True:
        # Tratando os espaços em vão e as víruglas
        valor = str(input(msg)).replace(',', '.').strip()
        # Tratando o 'valor' alpha ou vazio
        if valor.isalpha() and valor == '':
            print('Erro: Digite um valor monetário!')
        else:
            break
    return float(valor)
