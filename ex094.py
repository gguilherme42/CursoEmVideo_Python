'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os
dados em um dicionário e todos os dicionários em uma lista.
No final, mostre:
a) Quantas pessoas foram cadastradas;
b) A média de idade de idade do grupo;
c) Um lista com todas as mulheres;
d) Uma lista com todas as pessoas com idade acima da média.
'''
pessoas = {}
lista = []
listaMu = []
listaMed = []
med = soma = 0
while True:
    pessoas['Nome'] = str(input('Nome: '))
    pessoas['Sexo'] = str(input('Sexp: [F/M]')).strip().upper()[0]
    pessoas['Idade'] = int(input('Idade: '))
    if pessoas['Sexo'] == 'F':
        listaMu.append(pessoas.copy())
    lista.append(pessoas.copy())
    soma += pessoas['Idade']
    per = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if per in 'N':
        break
med = soma / (len(lista))
print(lista)
print()
# a)
print('a)')
print(f'Total de pessoas cadastradas: {len(lista)}')
print()
# b)
print('b)')
print(f'A média de idade do grupo: {med:.1f}')
print()
# c)
print('c)')
for f in listaMu:
    for k, v in f.items():
        print(f'{k}: {v}')
print(listaMu)
print()
# d)
print('d)')
for l in lista:
    for k, v in l.items():
        if k == 'Idade':
            if v > med:
                listaMed.append(l.copy())
print(listaMed)

