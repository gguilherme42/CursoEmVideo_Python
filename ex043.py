print('\033[1;4;30mIMC\033[m')
p = float(input('\033[1m DIGITE O SEU PESO (Kg): \033[m'))
alt = float(input('\033[1m DIGITE A SUA ALTURA (m): \033[m'))
IMC = p / (alt**2)
if IMC < 17:
    print('\033[1;31mVOCÊ ESTÁ COM A MASSA MUITO ABAIXO DO NORMAL! COM IMC DE {:.2f}\033[m'.format(IMC))
elif IMC <= 18.49:
    print('\033[1;32mVOCê ESTÁ COM A MASSA ABAIXO DO NORMAL! COM IMC DE {:.2f}\033[m'.format(IMC))
elif IMC <= 24.99:
    print('\033[1;30m VOCÊ ESTÁ COM A MASSA NORMAL! COM IMC DE {:.2f}\033[m'.format(IMC))
elif IMC <= 29.99:
    print('\033[1;33mVOCÊ ESTÁ COM A MASSA ACIMA DO NORMAL! COM IMC DE {:.2f}\033[m'.format(IMC))
elif IMC <= 34.99:
    print('\033[1;34mVOCÊ ESTÁ COM OBESIDADE 1! COM IMC DE {:.2f}\033[m'.format(IMC))
elif IMC <= 39.99:
    print('\033[1;35mVOCÊ ESTÁ COM OBESIDADE 2! COM IMC DE  {:.2f}\033[m'.format(IMC))
else:
    print('\033[1;36mVOCÊ ESTÁ COM OBESIDADE MÓRBIDA! COM IMC DE {:.2f}\033[m'.format(IMC))
