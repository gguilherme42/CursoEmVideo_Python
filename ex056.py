#LEITOR DE IDADE, NOME E SEXO DE 4 PESSOAS,
#MOSTRANDO: A MÉDIA DE IDADE, O NOME DO HOMEM MAIS VELHO
#E QUANTAS MULHERES TÊM MENOS DE 20 ANOS.
med = 0
mul = 0
homemid = 0
soma = 0
homemvelho = ''
for c in range(1, 5):
    print('\033[1m---- {}ª PESSOA ----\033[m'.format(c))
    nom = str(input('NOME: ')).strip()
    idade = int(input('IDADE: '))
    sex = str(input('SEXO [H/M]: ')).strip()
    if c == 1 and sex in 'Hh':
        homemvelho = nom
    if sex in 'Hh' and idade > homemid:
        homemvelho = nom
    if sex in 'Mm' and idade < 20:
        mul += 1
    soma += idade
med = soma/4
print('O nome do homem mais velho é \033[1m{}\033[m'.format(homemvelho))
print('A média da idade do grupo é \033[1m{}\033[m'.format(med))
print('\033[1m{}\033[m mulheres têm menos de 20 anos'.format(mul))
