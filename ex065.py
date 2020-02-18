resp = 'S'
n = med = tot = dig = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número inteiro: '))
    dig += 1
    tot += n
    if dig == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar?[S/N] ')).upper().strip()[0]
#MEDIA É SÓ CALCULADA UMA VEZ, PORTANTO, FORA DO WHILE
med = tot / dig
print('O total de número digitados foi {} e a média é: {}'.format(dig, med))
print('O menor número é {} e o maior é {}'.format(menor, maior))
