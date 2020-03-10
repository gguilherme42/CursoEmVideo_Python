'''
Aprimore o DESAFIO 093 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada
jogador.

'''
futebol = {}
jogadores = []
gol = []
totg = 0
while True:
    futebol['Nome'] = str(input('Nome do jogador(a): '))
    futebol['Partidas'] = int(input('Partidas jogadas: '))
    for c in range(0, futebol['Partidas']):
        gol.append(int(input(f'Gols na {c + 1}ª partida: ')))
        totg += gol[c]
    futebol['Gols'] = gol[:]
    futebol['Total de Gols'] = totg
    jogadores.append(futebol.copy())
    gol.clear()
    totg = 0
    perg = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if perg in 'N':
        break
print('=' * 35)
print(f'{"Nº":<}  {"NOME":<10}{"PARTIDAS":<10}{"TOTAL DE GOLS":>}')
for i, l in enumerate(jogadores):
    print(f'{i + 1:<}º  {l["Nome"]:<10} {l["Partidas"]:<10} {l["Total de Gols"]:>}')
print('=' * 35)

while True:
    perg1 = str(input('Quer ver o aproveitamento de cada jogador? [S/N] ')).strip().upper()[0]
    if perg1 in 'S':
        while True:
            jg = int(input('Qual jogador? 1, 2... '))
            if jg <= 0 or (jg - 1) > len(jogadores):
                print('Resposta inválida!')
            else:
                print('-' * 35)
                print(f'{"APROVEITAMENTO":^25}')
                print('-' * 35)
                print(f'{"Nº":<10}{"NOME":<10}{"GOLS":>10}')
                print(f'{jg:<10}{jogadores[jg - 1]["Nome"]}   {jogadores[jg - 1]["Gols"]}')
                break
    if perg1 in 'N':
        break