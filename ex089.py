'''
Exercício 089

Crie um programa que leia o nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa mostras as
notas de cada aluno individualmente.

Obs: Três níveis dentro de uma lista.
'''
alunos = []
notas = []
media = soma = 0
while True:
    nome = str(input('Nome do aluno: '))
    for n in range(0, 2):
        # Validação da nota, nota máx. é 10.
        while True:
            n1 = float(input(f'Digite a {n + 1}ª nota: [0 à 10] '))
            if n1 < 0 or n1 > 10:
                print('Nota inválida!')
            else:
                break
        notas.append(n1)
        soma += n1
        media = soma / (n + 1)
    soma = 0
    # Cadastrando o aluno dentro da lista 'alunos'
    alunos.append([nome, [notas[:]], media])
    # Varre-se os dados de 'dados' e 'notas'
    notas.clear()
    # Validação da resposta para continuar
    while True:
        perg = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if perg in 'N':
            break
        elif perg in 'S':
            break
        elif perg not in 'S':
            print('Resposta inválida!')
    if perg in 'N':
        break
# -----------------
# Boletim na tela
print('=' * 35)
print()
print('-' * 35)
print(f' {"BOLETIM":^25} ')
print('-' * 35)
print(f'{"Nº":<10}{"NOME":<10}{"MÉDIA":>10}')
for i, a in enumerate(alunos):
    print(f'{i + 1:<10}{a[0]:<10}{a[2]:>10.1f}')
print('-' * 35)
print('=' * 35)
# ----------------
# Notas
# Validação da resposta da pergunta
while True:
    perg1 = str(input('Quer ver as notas individuais? [S/N] ')).strip().upper()[0]
    if perg1 in 'S':
        # Validação do aluno
        while True:
            al = int(input('De qual aluno? 1, 2... '))
            if al <= 0 or (al - 1) > len(alunos):
                print('Resposta inválida!')
            else:
                print('-' * 35)
                print(f'{"NOTAS":^25}')
                print('-' * 35)
                print(f'{"Nº":<10}{"ALUNO":<10}{"NOTA":>10}')
                print(f'{al:<10} {alunos[al - 1][0]} {alunos[al - 1][1]}')
                break
    if perg1 in 'N':
        break
