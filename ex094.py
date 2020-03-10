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
print('='*30)
# a)
print(f'a) Total de pessoas cadastradas: {len(lista)}')
# b)
print(f'b) A média de idade do grupo: {med:.1f}')
# c)
print('c) As mulheres cadastradas foram: ', end='')
for i, f in enumerate(listaMu):
    print(f'{f["Nome"]} ', end='')
print()
# d)
for l in lista:
    for k, v in l.items():
        if k == 'Idade':
            if v > med:
                listaMed.append(l.copy())
print('d) Lista de pessoas acima da média: ')
for l in listaMed:
    for k, v in l.items():
        print(f'{k} = {v};', end=' ')
    print()
