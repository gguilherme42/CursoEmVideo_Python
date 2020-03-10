'''
Crie um programa que gerencie o aproveitamento de um
jogador de futebol. O programa vai ler o nome do jogador
e quantas partidas ele jogou. Depois vai ler a quantidade de
gols feitos em cada partida. No final, tudo isso será guardado em um
dicionário, incluindo o total de gols durante o campeonato.

Obs: Aproveitamento deve ser uma lista, os gols nas partidas.
'''
futebol = {}
gol = []
totg = 0
futebol['Nome'] = str(input('Nome do jogador(a): '))
futebol['Partidas'] = int(input('Partidas jogadas: '))
for c in range(0, futebol['Partidas']):
    gol.append(int(input(f'Gols na {c + 1}ª partida: ')))
    totg += gol[c]
futebol['Gols'] = gol[:]
futebol['Total de Gols'] =totg
print('='*30)
print(futebol)
print('='*30)
for k, v in futebol.items():
    print(f'O campo {k} tem valor: {v}')
print('='*30)
print(f'O jogador(a) {futebol["Nome"]} jogou {futebol["Partidas"]} partidas.')
for i, c in enumerate(gol):
    print(f'{"→":>5} Na {i + 1}ª partida fez: {c} gols.')
print(f'Foi um total de {totg} gols.')
