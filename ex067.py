# MOSTRA A TABUADA DE UM NÚMERO QUE O USUÁRIO DIGITA
# O PROGRAMA É INTERROMPIDO QUANDO O NÚMERO DIGITADO FOR NEGATIVO
while True:
    n = int(input('''
     Digite um número para ver sua tabuada ou digite um núemro negativo para sair:\n 
     '''))
    if n < 0:
        break
    for tabuada in range (1,11):
        print(f'{n} X {tabuada} = {n * tabuada} ')
