#leitor de peso de 5 pessoas, mostrando a mais pesada e o menos pesada.
mais = 0
menos = 0
for c in range(0, 5):
    peso = float(input('Digite o peso da {}ª pessoa (Kg): '.format(c)))
    if c == 1:
        #Se for a primeira pessoa, o peso é o menor e também o maior peso.
        mais = peso
        menos = peso
    else:
        if peso > mais:
            mais = peso
        elif peso < menos:
            menos = peso
print('O maior peso foi: {:.2f}Kg'.format(mais))
print('O menor peso foi: {:.2f}Kg'.format(menos))
