vel = float(input('Qual a velocidade do carro (Km/h)? '))
if vel > 80:
    multa = 7*(vel -80)
    print('Você foi multado por excesso de velocidade')
    print('Sua multa é de R${:.2f}'.format(multa))
print('Você andou com o carro na velocidade permitida!')



