print('\033[1;30m -=-\033[m'*5)
print('\033[1;35m EMPRÉSTIMO BANCÁRIO \033[m')
print('\033[1;30m -=-\033[m'*5)
casa = float(input('Digite o valor da casa que deseja comprar: \033[32m R$ \033[m'))
sal = float(input('Digite o seu salário:\033[32m R$ \033[m'))
ano = int(input('Digite, por quantos anos deseja pagar: \033[32m '))
#Cálculo da prestação
prest = casa / (12 * ano)
#Cálculo de 30% do salário
trin = (30 * sal) / 100
#Condicional para a aprovação ou negação do empréstimo
if prest <= trin:
    print('\033[1mEMPRÉSTIMO APROVADO!!!')
else:
    print('\033[1mEmpréstimo negado, pois as prestações são maiosres que 30% do seu salário.')
