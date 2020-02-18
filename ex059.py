from time import sleep
resp = 0
esc = 0
n1 = 0
n2 = 0
while resp != 5:
    resp = 0
    n1 = int(input('\033[1mDigite um valor:\033[m '))
    n2 = int(input('\033[1mDigite outro valor:\033[m '))
    while resp != 4 and resp != 5:
        resp = int(input('''\033[1mESCOLHA:\033[m
\033[1;35m[1]\033[m \033[1;30mSOMAR\033[m
\033[1;35m[2]\033[m \033[1;30mMULTIPLICAR\033[m
\033[1;35m[3]\033[m \033[1;30mMAIOR\033[m
\033[1;35m[4]\033[m \033[1;30mNOVOS NÚMEROS\033[m
\033[1;35m[5]\033[m \033[1;30mSAIR\033[m\n '''))
        if resp == 1:
            esc = n1 + n2
            print('\033[1;30mA soma entre {} e {} é: {}\033[m'.format(n1, n2, esc))
        elif resp == 2:
            esc = n1*n2
            print('\033[1;30mA multiplicação entre {} e {} é: {}\033[m'.format(n1, n2, esc))
        elif resp == 3:
            if n1 > n2:
                esc = n1
                print('\033[1;30mEntre {} e {} o maior é: {}\033[m'.format(n1, n2, esc))
            elif n1 == n2:
                print('\033[1;30mOs dois número são iguais.\033[m')
            else:
                esc = n2
                print('\033[1;30m;30Entre {} e {} o maior é: {}\033[m'.format(n1, n2, esc))
        elif resp != 5 or 4 or 3 or 2 or 1:
                print('\033[1;31mOPÇÃO INVÁLIDA!\033[m')
        sleep(1)
print('\033[1;30mSAINDO...\033[m')
sleep(1)
