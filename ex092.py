'''
Crie um programa que leia nome, ano de nascimento e carteira de
trabalho e cadastre-os (com idade) em um dicionário se por acaso
a CTPS for diferente de ZERO, o dicionário receberá também o ano
de contratação e o salário. Calcule e acrescente, além da idade, com quantos
anos a pessoa vai se aposentar.

Obs: * carteira de trabalho igual à zero significa que não possuí;
* aposentadoria depois de 35 anos de contribuição (considerada no programa).

'''
from datetime import date
dicio = dict()
dicio['nome'] = str(input('Nome: ')).strip()
ano = int(input('Ano de nascimento: '))
dicio['idade'] = date.today().year - ano
dicio['CTPS'] = int(input('Carteira de trabalho (digite 0se não tem) '))
if dicio['CTPS'] != 0:
    dicio['Contratação'] = int(input('Ano de contratação: '))
    dicio['Salário'] = float(input('Salário: R$'))
    dicio['Aposentadoria'] = (dicio['Contratação'] - ano) + 35
print(dicio)
for k, v in dicio.items():
    print(f'- {k} tem valor {v}')



