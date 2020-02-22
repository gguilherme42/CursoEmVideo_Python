'''
Programa que o usuário digita vários valores numéricos e cadastre-os em uma lista. Caso o número
já exista la dentro, ele não será adicionado.
No final, mostre:
a) Exibição de todos os valores único, digitados em ordem crescente.
'''
#@Guilherme
lista = []
while True:
    num = int(input('Digite um número: '))
    # Verificação caso o número digitado já esteja na lista
    while True:
        # Condição para o começo do programa
        if lista == []:
            break
        # Se o número digitado já estiver na lista, então:
        if num in lista:
            print('Número repetido!', end='')
            num = int(input('Digite um número: '))
        # Do contrário:
        else:
            break
    # Adição do número digitado na lista
    lista.append(num)
    # Pergunta para continuação do programa
    perg = str(input('Quer continuar? [S/N] ')).strip()[0].upper()
    # Consequências da resposta
    if perg in 'Nn':
        break
    if perg not in 'NnSs':
        print('Respota inválida!')
print(f'Lista em ordem crescente: {sorted(lista)}')
