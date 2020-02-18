print('\033[1;35m COMPARADOR DE NÚMEROS \033[m')
n1 = int(input('\033[1m Digite um número inteiro: \033[m'))
n2 = int(input('\033[1m Digite outro número inteiro: \033[m'))
if n1 == n2:
    print('\033[1;32m Não existe valor maior, os dois são iguais.')
elif n1 > n2:
    print('\033[1;32m O primerio número é maior, isto é, {} \033[m'.format(n1))
else:
    print('\033[1;32m O segundo número é maior, isto é, o 10{} \033[m'.format(n2))





