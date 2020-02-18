a1 = int(input('DIGITE O PRIMEIRO TERMO: '))
r = int(input('DIGITE A RAZÃO: '))
term = a1
cont = 1
total = 0
resp = 10
while resp != 0:
    total += resp
    while cont <= total:
        print('{} → '.format(term), end='')
        term += r
        cont += 1
    print('PAUSE!')
    resp = int(input('Quantos termos você quer mostrar a mais? '))
print('FIM! {} termos no total.'.format(total))




