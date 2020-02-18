'''
Tupla com os 20 primeiros colocados do Campeonato Brasileiro de Futebol, na ordem de colocação
Mostrando:
a) Apenas os 5 primeiros colocados;
b) Os últimos 4 colocados da tabela;
c) Lista em ordem alfabética;
d) Em que posição está o time da Chapecoense.
'''
# CBF = Campeonato Brasileiro de Futebol
# Lista de 2019 em:
# https://pt.wikipedia.org/wiki/Lista_dos_20_primeiros_colocados_do_Ranking_Nacional_de_Clubes_por_ano
# Tupla está entre parênteses para ser didático
cbf = ('Palmeiras', 'Cruzeiro', 'Grêmio', 'Santos', 'Corinthians',
       'Flamengo', 'Atlético Mineiro', 'Atlético Paranaense',
       'Internacional', 'Chapecoense', 'Botafogo', 'São Paulo',
       'Fluminense', 'Vasco da Gama', 'Bahia', 'Sport', 'Vitória',
       'Ponto Preta', 'América', 'Coritiba')
# Colocação dos times
print('-=-'*10)
for lug, c in enumerate(cbf):
    print(f'{lug + 1}º lugar: {c}')
print('-=-'*10)
# a)
print(f'* Os cinco primeiros colocados: {cbf[:6]}')
# b)
print(f'* Os últimos 4 colocados: {cbf[-4:]}')
# c)
print(f'* Lista em ordem alfabética: \n{sorted(cbf)}')
# d)
# Variável para imprimir a colocação do Chapecoense
i = cbf.index('Chapecoense')
print(f'* Chapecoense está em {i + 1}º lugar.')
