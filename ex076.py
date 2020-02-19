'''
Programa com tupla única que contém nome e preço dos produtos
Mostrando:
a) Listagem dos preços organizando-os de forma tabular.
'''
'''
@Guilherme
Minha resolução antes de ver os vídeos dos exercícios
'''
tupla = ('Pão', 2.00, 'Suco', 2.50, 'Cerveja Skol', 5.50, 'Chocolate', 4.90)
# a) repetição genérica para funcionar para qualquer tupla
# A variável auxiliar 'c' irá começar no índice zero, o início, e percorrerá até o comprimento da tupla,
# isto é, percorrerá até o final da tupla, 'len(tupla)', com passo 2.
for c in range(0, len(tupla), 2):
    # Alinhamento da tupla com índice 'c' à esquerda com 20 caracteres de espaçamento,
    # preenchidos com '.'. O 'end = ''', serve para juntar o próximo print com este.
    print(f'{tupla[c]:.<20}', end='')
    # Condição para caso o Índice 'c' esteja no começo ou no fim, o indice seja somado com 1
    if c == 0 or c == len(tupla):
        print(f'R$ {tupla[c + 1]:3}')
    # Caso contrário, o Índice 'c' será subtraído com 1
    else:
        print(f'R$ {tupla[c - 1]:3}')
'''
Resolução do @Guanabara de forma resumida

tupla = ('Pão', 2.00, 'Suco', 2.50, 'Cerveja Skol', 5.50, 'Chocolate', 4.90)
for pos in range(0, len(tupla)):
    if pos % 2 == 0:
        print(f'{tupla[pos]:.<30}', end='')
    else:
        print(f'{tupla[pos]:>7.2f}')
'''
