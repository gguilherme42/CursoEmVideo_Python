'''
Programa que o usuário digita vários valores numéricos e cadastre-os em uma lista. Caso o número
já exista la dentro, ele não será adicionado.
No final, mostre:
a) Exibição de todos os valores único, digitados em ordem crescente.
'''
#@Guilherme
lista = []
while True:
    n = int(input('Digite um número: '))
    # Verificando se o número digitado já está na lista
    if n not in lista:
        lista.append(n)
    else:
        print('Valor repetido! ')
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    # Caso digite 'N':
    if r in 'N':
        break
print(lista)
# a)
print(sorted(lista))
