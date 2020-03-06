'''
Exercício 085

Crie um programa onde o usuário possa digitar sete valores numéricos e
cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.

'''
par = []
ímpar = []
# Repetição para digitar sete números
for x in range(0, 7):
    n = int(input('Digite um número: '))
    # Se o número do resto da divisão por 2 for igual à zero,
    # então é par
    if n % 2 == 0:
        par.append(n)
    # Se não, ímpar
    else:
        ímpar.append(n)
# Copiando os valores das listas dentro de outra lista
números = [[par[:]], [ímpar[:]]]
print('-'*30)
print(f'Números: {números}')
print(f'Pares: {sorted(par)}')
print(f'Ímpares: {sorted(ímpar)}')
