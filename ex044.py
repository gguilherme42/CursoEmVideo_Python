print('\033[1;33m--------\033[m'*20)
print('         \033[1;30mCAIXA ELETRÔNICO     \033[m'*20)
print('\033[1;33m--------\033[m'*20)
pro = float(input('\033[1mINFORME O VALOR DO PRUDTO: R$\033[m'))
pag = int(input('\033[1mFORMA DE PAGAMAENTO:\033[m \n\033[1;32m[1] À vista/cheque \n[2] Cartão \n[3] 2x no céredito \n[4] 3x ou mais no cartão\n\033[m'))
if pag == 1:
    desc = (pro*10)/100
    print('\033[1;32mO preço total à se pagar é de R${:.2f}\033[m'.format(pro - desc))
elif pag == 2:
    desc = (pro*5)/100
    print('\033[1;30mO preço total à se pagar é de R${:.2f}\033[m'.format(pro - desc))
elif pag == 4:
    vez = int(input('Deseja parcelar em quantas vezes? '))
    juros = (pro*20*vez)/100
    print('\033[1;30mO preço total à se pagar é de R${:.2f}\033[m'.format(pro + juros))
else:
    print('\033[1;30mO preço total à se pagar é de R${:.2f}\033[m'.format(pro))
