print('=== PREÇO DA PASSAGEM ===')
dis = float(input('Qual a distância da sua viagem (Km): '))
if dis <= 200:
    pas = 0.5 * dis
    print('O preço da sua passagem é de R${:.2f}'.format(pas))
if dis > 200:
    pas = 0.45 * dis
    print('O preço da sua passagem é de R@{:.2f}'.format(pas))
'''Comando feito por mim'''
