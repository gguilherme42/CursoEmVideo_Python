'''
Faça um programa que tenha uma função chamada contador()
que receba três parâmetros: início, fim e passo e realize a
contagem.
Seu programa tem que realizar três contagens através da função criada
a) De 1 até 10, de 1 em 1;
b) De 10 até 0, de 2 em 2;
c) uma contagem personalizada (usuário digita os parâmetros).

Obs: passo = 0, vira 1
passo = negativo, vira positivo
'''
def esc():
    print()
    print('='*30)


def contador(i, f, p):
   if p == 0:
       p = 1
   if i > f:
       for l in range(i, f - p, - p):
            print(l, end=' ')
   else:
       for l in range(i, f + p, p):
            print(l, end=' ')

esc()
# a)
print('Contagem de 1 até 10, com passo 1: ')
contador(1, 10, 1)
esc()
# b)
print('Contagem de 10 até 0, com passo 2: ')
contador(10, 0, 2)
esc()
# c)
print('Contagem personalizada: ')
n1 = int(input('Digite o início: '))
n2 = int(input('Digite o fim: '))
n3 = int(input('Digite o passo: '))
contador(n1, n2, n3)
esc()
