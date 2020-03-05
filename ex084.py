'''
Exercício 084

Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em
uma lista. No final, mostre:
a) Quantas pessoas foram cadastradas;
b) Uma listagem com as pessoas pesadas;
c) Uma listagem com as pessoas leves.

pesado: 100kg
leve: 60kg
'''

pessoas = []
p = []
totp = maisl = maisp = 0
while True:
    p.append(str(input('Nome da pessoa: ')))
    p.append(int(input('Peso da pessoa: [Kg]')))
    # Copiando os valores de 'p' para 'pessoas'
    pessoas.append(p[:])
    # Quantida de pessoas pesadas
    if p[1] >= 100:
        maisp += 1
    # Quantidade de pessoas leves
    if p[1] <= 60:
        maisl += 1
    # Limpando a lista
    p.clear()
    # Quantidade de pessoas cadastradas
    totp += 1
    perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    # Sáida do loop
    if perg in 'N':
        break
print('-'*30)
# a)
print(f'Pessoas cadastradas: \n{pessoas}')
print(f'Total de pessoas cadastradas: {totp}')
# b)
print(f'Total de pessoas pesadas: {maisp}')
# c)
print(f'Total de pessoas leves: {maisl}')
