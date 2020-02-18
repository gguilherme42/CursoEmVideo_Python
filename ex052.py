#LEITOR DE NÚMERO INTEIRO, MOSTRANDO SE ELE É PRIMO OU NÃO
num = int(input('DIGITE UM NÚMERO: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        #Print para ver quantas vezes foi dividído o número digitado
        print('\033[32;1m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print('{} '.format(c), end=' ')
print('\n\033[mO número {} foi divisisível {} vezes '. format(num, tot))
if tot == 2:
    print('Então, ele é PRIMO!')
else:
    print('Então, ele NÃO É PRIMO!')

