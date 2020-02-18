print('\033[1;33m CONVERSOR DE NÚMEROS \033[m')
num = int(input('\033[1m Digite um número inteiro: '))
resp = int(input('''\033[1m Quer converter para: \033[m
\033[1;32m[1] Binário 
[2] Decimal  
[3] Hexadecimal\033[m \n'''))
if resp == 1:
    print('\033[1m{}\033[m convertido para binário é \033[1m{}\033[m'.format(num, bin(num)[2:]))
elif resp == 2:
    print('\033[1m{}\033[m convertido para octal é \033[1m{}\033[m'.format(num, oct(num)[2:]))
# O fatiamento corta a consideração de octal do python e coloca somente o número em octal.
elif resp == 3:
    print('\033[1m{}\033[m convertido para hexadecimal é \033[1m{}\033[m'.format(num, hex(num)[2:]))
# O '[2:]' é um fatiamento feito para excluir o '0x' do python que
# ele considera como hexadecimal. Significando que começará no carctecere
# de posição 2 e irá até o final.
else:
    print('\033[1;31mVOCÊ DIGITOU UMA OPÇÃO INVÁLIDA!\033[m')
