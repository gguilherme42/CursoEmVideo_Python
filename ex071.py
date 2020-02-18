'''
CAIXA ELETRÔNICO
'''
cédulas = 0
valorced = 50
# Validação do valor
while True:
    valor = int(input('Digite o valor a ser sacado: R$'))
    if valor <= 0.00:
        print('\033[1;31mResposta inválida!\033[m')
    else:
        break
saque = valor
while True:
    if valorced <= saque:
        saque -= valorced
        cédulas += 1
    else:
        # Condição para não aparecer na tela '0 cédulas de R$50.00', por exemplo.
        if cédulas != 0:
            print(f'{cédulas} cédula(s) de R${valorced}')
        # condição para sair do loop
        if saque == 0:
            break
        if valorced == 50:
            valorced = 20
        elif valorced == 20:
            valorced = 10
        elif valorced == 10:
            valorced = 5
        elif valorced == 5:
            valorced = 1
        cédulas = 0
