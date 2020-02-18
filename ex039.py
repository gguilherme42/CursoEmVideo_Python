from datetime import date
print('\033[1;4;30m***\033[m'*10)
print('\033[1;33m         ALISTAMENTO \033[m')
print('\033[1;4;30m***\033[m'*10)
nom = str(input('\033[1m Digite seu nome completo: \033[m'))
nasc = int(input('\033[1m Digite seu ano de nascimento: \033[m'))
sex = str(input('\033[1mDigite seu sexo (H/M) \033[m'))
idade = date.today().year - nasc
if idade == 18:
    if sex == 'M' or sex == 'm':
        print('\033[1;m É HORA DE SE ALISTAR, JOVEM. MAS VOCÊ NÃO É OBRIGADA!\033[m')
    else:
        print('\033[1;m É HORA DE SE ALISTAR, JOVEM!\033[m')
elif idade < 18:
    if sex == 'M' or sex == 'm':
        print('\033[1mFALTAM {} ANO(S) PARA SE ALISTAR, JOVEM! MAS VOCÊ NÃO É OBRIGADA!\033[m'.format(18 - idade))
    else:
        print('\033[1mFALTAM {} ANO(S) PARA SE ALISTAR, JOVEM!\033[m'.format(18 - idade))
else:
    print('\033[1mJÁ PASSOU SEU TEMPO DE SE ALISTAR, JOVEM!\033[m')
