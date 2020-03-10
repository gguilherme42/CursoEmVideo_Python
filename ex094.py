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
med = soma = 0
while True:
    pessoas['Nome'] = str(input('Nome: '))
    # Validação do sexo
    while True:
        pessoas['Sexo'] = str(input('Sexp: [F/M]')).strip().upper()[0]
        if pessoas['Sexo'] not in 'FM':
            print('Erro: Digite F ou M')
        else:
            break
    # Validação da idade
    while True:
        pessoas['Idade'] = int(input('Idade: '))
        if pessoas['Idade'] <= 0:
            print('Erro: Digite uma idade válida.')
        else:
            break
    lista.append(pessoas.copy())
    soma += pessoas['Idade']
    # Validação da pergunta
    while True:
        per = str(input('Quer continuar? [S/N]')).strip().upper()[0]
        if per not in 'NS':
            print('Erro: Digite S ou N')
        else:
            break
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
for f in lista:
    if f['Sexo'] in 'F':
        print(f'{f["Nome"]} ', end='')
    print()
# d)
print('d) Lista de pessoas acima da média: ')
for l in lista:
    for k, v in l.items():
        if l['Idade'] >= med:
            print(f'{k} = {v};', end=' ')
        print()
