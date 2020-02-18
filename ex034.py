sal = float(input('Digite seu salário: R$'))
if sal <= 1250:
    aum = (sal*15)/100
    print('Você receberá um aumento de R${:.2f} \nFicando com o salário total de R${:.2f}'.format(aum, (sal + aum)))
if sal > 1250:
    aum = (sal*10)/100
    print('Você receberá um aumento de R${:.2f} \nFicando com o salário total de R${:.2f}'.format(aum, (sal + aum)))



