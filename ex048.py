#SOMA DE TODOS OS NÚMEROS ÍMPARES MÚLTIPLOS DE 3, DE 1 ATÉ 500.
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print('A soma de todos os {} números ímpares múltiplos de três é {}'.format(cont, soma))
