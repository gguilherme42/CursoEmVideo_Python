print('\033[1;4;30m BOLETIM \033[m')
nt1 = float(input('\033[m Digite sua primeira nota: \033[m'))
nt2 = float(input('\033[m Digite sua segunda nota: \033[m'))
med = (nt1 + nt2) / 2
if med < 5:
    print('\033[1;32mREPROVADO!\033[m')
elif med < 7:
    print('\033[1;32mRECUPERAÇÃO!\033[m')
else:
    print('\033[1;32mAPROVADO!\033[m')

