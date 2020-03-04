'''
Programa onde o usuário digita uma expressão matemática qualquer que use parênteses.
O aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
 na ordem correta.
 Obs: Só se considera os parênteses, não seguindo regras das expressões matemáticas.
'''
#Resuloção do Guanabara comentada.
expres = input('Digite uma expressão matemática: ').strip()
# Na lista criada serão adicionados apenas os parênteses da expressão
lista = []
for paren in expres:
    # Caso 'paren' seja igual a um parênteses fechado,
    # será adicionado a 'lista'
    if paren == '(':
        lista.append('(')
    # Caso 'paren' seja igual a um parênteses aberto,

    elif paren == ')':
        # E a lsita não estiver vazia, será removido o último elemento da lista.
        # Pois se um parêntes aberto existir antes,
        # este será deletado e a lista ficará vazia.
        if len(lista) > 0:
            lista.pop()
        # Do contráio
        else:
            # Será adicionado o parênteses aberto na lista, invalidando-a
            lista.append(')')
            break
# Para expressão ser válida, a lista deve estar vazia
if len(lista) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')