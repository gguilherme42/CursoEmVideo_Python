from ex110 import moeda
n = float(input('Digite um preço: R$'))
print(moeda.aumentar(n, 10, f=False))
print(f'{n} com aumento de 10% é igual a {moeda.aumentar(n, 10)}')
print(f'{n} menos 10% é igual a {moeda.diminuir(n, 10)}')
print(f'O dobro de {n} é igual a {moeda.dobro(n)}')
print(f'A metade de {n} é igual a {moeda.metade(n)}')
moeda.resumo(n, 10)
