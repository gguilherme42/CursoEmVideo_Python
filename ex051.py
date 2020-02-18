#LEITOR DE RAZÃO E PRIMEIRO TERMO DE UMA PA, MOSTRANDO OS 10 PRIMEIROS TERMOS.
a1 = int(input('DIGITE O PRIMEIRO TERMO: '))
r = int(input('DIGITE A RAZÃO: '))
decterm = a1 + ((10 - 1) * r)
for c in range(a1,  decterm + r, r):
    print(c, end=' ')
