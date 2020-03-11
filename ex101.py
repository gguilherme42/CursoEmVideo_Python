'''
Crie um programa que tenha um função chamada voto()
que vai receber como parâmetro o ano de nascimento
de uma pessoa, retorando um valor litera indicanto
se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO
nas eleições.
'''


def voto(nasc):
    from datetime import date
    id = date.today().year - nasc
    if 18 > id >= 16 or id >= 65:
        print(f'Com {id} anos: VOTO OPCIONAL')
    elif 65 > id >= 18:
        print(f'Com {id} anos: VOTO OBRIGATÓRIO')
    elif id < 16:
        print(f'Com {id} anos: VOTO NEGADO')


n = int(input('Digite o ano de nascimento: '))
voto(n)
