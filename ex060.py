'''RESOLUÇÃO RESUMIDA:
from math import factorial
num = int(input('Digite um número para fatoriá-lo: '))
f = factorial(num)
print('O fatorial de {} é {}'.format(num, f))'''

num = int(input('Digite um número para fatoriá-lo: '))
n = num
f = 1
print('Fatorial: {}! = '.format(num), end='')
while n > 0:
    print('{}'.format(n), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= n
    n -= 1
print('{:0f}'.format(f))
