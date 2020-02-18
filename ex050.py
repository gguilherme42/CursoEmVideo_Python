#LEITOR DE 6 NÚMEROS INTEIROS E SOMADOR DOS PARES.
som = 0
for c in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        som += n
print('A soma de todos os números pares digitados é: {}'. format(som))