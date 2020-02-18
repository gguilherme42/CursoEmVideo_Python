#TABUADA DO EX009 REFEITA COM 'FOR'.
n = int(input('DIGITE UM NÚMERO PARA VER SUA TABUADA: '))
for c in range(1, 11):
    print('{} X {:2} = {}'.format(n, c, n*c))
