'''
Programa onde o usuário possa digitar cinco valores numéricos e cadastre-os numa lista,
já na posição correta de inserção (sem usar o .sort()).
Mostrando:
a) A lista ordenada na tela.
'''
#@Guilherme
lista = []
# Contador:
x = 0
while x < 5:
    num = int(input('Digite um número: '))
    # Se a lista for vazia:
    if lista == []:
        lista.append(num)
    # Se maior que o maior número:
    elif num >= max(lista):
        lista.append(num)
    # Caso seja menor que o menor ou esta entre o maior e o menor,
    # usa-se de uma repetição para percorrer a lista.
    else:
        for posi, c in enumerate(lista):
            if num < c:
                lista.insert(posi, num)
                break
    x += 1
print(f'Lista ordenada sem o sorted(): {lista}')
