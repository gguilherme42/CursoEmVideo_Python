'''
Programa que lê vários valores numéricos e coloque-os numa lista.
Mostrando:
a) Quantos números foram digitados;
b) A lista ordenada de forma decrescente;
c) Se o valor 5 está ou não na lista.
'''
#@Guilherme
lista = []
# Contador para números digitados
x = 0
print('++'*20)
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    x += 1
    # Pergunta para continuação do programa
    while True:
        perg = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
        # Consequências da resposta
        if perg in 'NnSs':
            break
        else:
            print('Resposta inválida!')
    if perg in 'Nn':
        break
print('++' * 20)
# a)
print(f'Quantidade de números digitados: {x}')
# b)
print(f'Lista em ordem crescente: {sorted(lista)}')
print(f'Lista em ordem decrescente: {sorted(lista, reverse=True)}')
# c)
if 5 in lista:
    print('O número 5 está na lista!')
else:
    print('O número 5 está na lista!')
# Resulução similar com  do Guanabara