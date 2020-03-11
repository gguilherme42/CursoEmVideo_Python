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
from time import sleep


def contador(i, f, p):
   print('=' * 30)
   print(f'Contagem de {i} até {f} com passo {p} ')
   if p == 0:
   # Ou: if p < 0:
   #    p *= - 1
       p = 1
   elif - p:
       p = abs(p)
   if i > f:
       for l in range(i, f - p, - p):
            # Coloca-se o flush=True para não usar um 'buffer de tela'
            print(l, end=' ', flush=True)
            sleep(0.5)
       print('FIM!')
   elif i == f:
       print('Não há contagem, pois o início e fim são iguais.')
   else:
        for l in range(i, f + p, p):
            print(l, end=' ', flush=True)
            sleep(0.5)
        print('FIM!')
   print('=' * 30)

# a)
contador(1, 10, 1)
# b)
contador(10, 0, 2)
# c)
print('Contagem personalizada: ')
n1 = int(input('Digite o início: '))
n2 = int(input('Digite o fim: '))
n3 = int(input('Digite o passo: '))
contador(n1, n2, n3)

