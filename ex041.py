print('\033[1;30m+++\033[m'*15)
print('\033[1;4;30mCONFEDERAÇÃO DE NATAÇÃO\033[m')
print('\033[1;30m+++\033[m'*15)
nom = str(input('\033[1mDigite o nome completo do atleta: \033[m'))
id = int(input('\033[1mDigite a idade do atleada: \033[m'))
if id <= 9:
    print('\033[1;32mNOME: {} \nCATEGORIA: MIRIM\033[m'.format(nom))
elif id <= 14:
    print('\033[1;32mNOME: {} \nCATEGORIA: INFANTIL\033[m'.format(nom))
elif id <= 19:
    print('\033[1;32mNOME: {} \nCATEGORIA: JUVENIL\033[m'.format(nom))
elif id == 25:
    print('\033[1;32mNOME: {} \nCATEGORIA:SÊNIOR\033[m'.format(nom))
else:
    print('\033[1;32mNOME: {} \nCATEGORIA:MASTER\033[m'.format(nom))
