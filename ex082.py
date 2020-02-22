'''
Programa que lê vários números e coloque-os numa lista.
Depois disso, cria duas listas: uma com valores pares e outra com os ímpares digitados.
No final, mostre:
a) O conteúdo das listas.
'''
#@Guilherme
lista = []
par = []
impar = []
while True:
    num = int(input('Digite um número: '))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
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
print(f'''
Conteúdo das listas:
Lista principal:
{lista}
Lista de números pares:
{par}
Lista de números ímpares:
{impar}
''')