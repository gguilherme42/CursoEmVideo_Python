'''
Crie um programa que tenha um função chamada voto()
que vai receber como parâmetro o ano de nascimento
de uma pessoa, retorando um valor litera indicanto
se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
nas eleições.
'''
from datetime import date


def voto(nasc):
    id = date.today().year - nasc
    if 18 > id >= 16:
        return print('Voto: OPCIONAL')
    elif 70 > id >= 18:
        return print('Voto: OBRIGATÓRIO')
    elif id < 16 or id > 70:
        return print('Voto: NEGADO')


n = int(input('Digite o ano de nascimento: '))
voto(n)
