#REFAZER EX051 COM WHILE
'''MINHA RESOLUAÇÃO:
a1 = int(input('DIGITE O PRIMEIRO TERMO: '))
r = int(input('DIGITE A RAZÃO: '))
ultterm = a1 + ((10 - 1) * r)
c = a1
while c != ultterm + r:
    print(c, end='')
    print(' → ', end='')
    c += r
print('FIM!')'''

#Resolução do vídeo:
a1 = int(input('DIGITE O PRIMEIRO TERMO: '))
r = int(input('DIGITE A RAZÃO: '))
term = a1
cont = 1
while cont <= 10:
    print('{} → '.format(term), end='')
    term += r
    cont += 1
print('FIM!')
