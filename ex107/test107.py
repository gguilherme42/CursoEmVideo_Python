from ex107 import moeda0
n = float(input('Digite um preço: R$'))
print(f'{n} com aumento de 10% é igual a {moeda0.aumentar(n, 10)}')
print(f'{n} menos 10% é igual a {moeda0.diminuir(n, 10)}')
print(f'O dobro de {n} é igual a {moeda0.dobro(n)}')
print(f'A metade de {n} é igual a {moeda0.metade(n)}')
