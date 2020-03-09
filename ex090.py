'''
Faça um progrma que leia nome e média de um aluno,
guardando também a situação em um dicionário. No final,
mostre o conteúdo da estrutura na tela.

Obs: média 7 ou mais é aprovado.
'''

aluno = {}
aluno['Nome'] = str(input('Nome do aluno: ')).strip()
aluno['Media'] = float(input('Média do aluno: '))
if aluno['Media'] >= 7:
    aluno['Situação'] = 'APROVADO'
else:
    aluno['Situação'] = 'REPROVADO'
print('='*25)
for k, v in aluno.items():
    print(f'{k:<}: {v:<5}')
print('='*25)
