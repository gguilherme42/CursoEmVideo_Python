from ex108 import moeda1
n = float(input('Digite um preço: R$'))
print(moeda1.moeda(n))
print(f'{n} com aumento de 10% é igual a {moeda1.moeda(moeda1.aumentar(n, 10))}')
print(f'{n} menos 10% é igual a {moeda1.moeda(moeda1.diminuir(n, 10))}')
print(f'O dobro de {n} é igual a {moeda1.moeda(moeda1.dobro(n))}')
print(f'A metade de {n} é igual a {moeda1.moeda(moeda1.metade(n))}')
