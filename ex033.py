a1 = int(input('Primeiro valor: '))
b1 = int(input('Segundo valor: '))
c1 = int(input('Terceiro valor: '))
menor = a1
maior = c1
#Testando o menor
if c1 > b1 < a1:
    menor = b1
if b1 > c1 < a1:
    menor = c1
#Testando o maior
if c1 < b1 > a1:
    maior = b1
if c1 < a1 > b1:
    maior = a1
print('Dentrs os valores digitados {}, {}, {} '.format(a1, b1, c1))
print('O maior foi {} e o menor {}'.format(maior, menor))

