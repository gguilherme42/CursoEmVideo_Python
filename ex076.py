'''
Programa com tupla única que contém nome e preço dos produtos
Mostrando:
a) Listagem dos preços organizando-os de forma tabular.
'''
tupla = ('Pão', 2.00, 'Suco', 2.50, 'Cerveja Skol', 5.50, 'Chocolate', 4.90)
for c in range(0, len(tupla), 2):
    print(f'{tupla[c]:.<20}', end='')
    if c == 0 or c == 8:
        print(f'R$ {tupla[c + 1]:3}')
    else:
        print(f'R$ {tupla[c - 1]:3}')
