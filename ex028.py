from random import choice
print('===== Adivinhe o número ===='.upper())
print('Tente adivinhar um número entre 0 e 5')
resp = int(input('Digite um número inteiro entre 0 e 5: '))
num = [0, 1, 2, 3, 4, 5]
if resp == choice(num):
    print('VOCÊ VENCEU')
else:
    print('O COMPUTADOR VENCEU!')



