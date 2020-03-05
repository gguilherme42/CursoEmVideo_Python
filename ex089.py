'''
Exercício 089

Crie um programa que leia o nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostras as
notas de cada aluno individualmente.

Obs: Três níveis dentro de uma lista.
'''
alunos = []
dados = []
notas = []
media = soma = 0
while True:
    nome = str(input('Nome do aluno: '))
    dados.append(nome)
    for n in range(0, 2):
        n1 = int(input(f'Digite a {n}ª nota: '))
        notas.append(n1)
        # Soma das notas
        soma += n1
    # Adição das notas aos dados do aluno
    dados.append(notas[:])
    # Média:
    # A média é igual a soma das notas, divido pela quantidade de notas
    media = soma / len(notas)
    # Adição da média aos dados do aluno
    dados.append(media)
    # Adição do aluno ao conjunto de alunos
    alunos.append(dados[:])
    # Limpando a lista de notas
    notas.clear()
    # Limpando os dados do aluno cadastrado
    dados.clear()
    perg = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if perg in 'N':
        break
print('=' * 35)
print(f' {"BOLETIM":^10} ')
for b in alunos:
    for i, a in enumerate(b):
        if i != 1:
            if i == 0:
                print(f'Nome: {a} ', end='')
            elif i == 2:
                print(f'Média: {a} \n')
perg1 = str(input('Quer ver as notas separadamente? [S/N]'))
print('=' * 35)
if perg1 not in 'N':
    print('  NOTAS  ')
    for b in alunos:
        for i, a in enumerate(b):
            if a != 2:
                if i == 0:
                        print(f'Nome: {a} ', end='')
                elif i == 1:
                        print(f'Nota: {a} \n')
