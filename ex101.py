'''
Crie um programa que tenha um função chamada voto()
que vai receber como parâmetro o ano de nascimento
de uma pessoa, retorando um valor litera indicanto
se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
nas eleições.
'''


def voto(nasc):
    """
    -> Função para ver se o voto  eleitoral é é não obrigatório,
        obrigatório ou opcional.
        - Calcula a idade de acordo com o ano atual do sistema.
    :param nasc: ano de nascimento
    :return: retorna uma string dizendo a idade e a situação de voto
    """
    from datetime import date
    id = date.today().year - nasc
    if 18 > id >= 16 or id >= 65:
        return f'Com {id} anos: VOTO OPCIONAL'
    elif 65 > id >= 18:
        return f'Com {id} anos: VOTO OBRIGATÓRIO'
    elif id < 16:
        return f'Com {id} anos: VOTO NEGADO'


n = int(input('Digite o ano de nascimento: '))
print(voto(n))

help(voto)
