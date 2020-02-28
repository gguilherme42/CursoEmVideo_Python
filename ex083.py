'''
Programa onde o usuário digita uma expressão matemática qualquer que use parênteses.
O aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados
 na ordem correta.
'''
#@Guilherme
expres = input('Digite uma expressão matemática: ').strip()
lista = []
soma = divi = mult = sub = 0
for l in expres:
    if l not in ' ':
        lista.append(l)
    if l == '+':
        soma = 1
    elif l == '*':
        mult = 1
    elif l == '-':
        sub = 0
    elif l == '/':
        divi = 1
print(lista)
if '012345678910' in lista and '+-/*' in lista:
        if '()' in lista:
            if lista.count('(') == lista.count(')'):
                if (lista.index(0, '(') and lista.index(-1, ')')) or lista.index(0, ')'):
                    print('Expressão inválida!')
            else:
                print('Expressão inválida!')
else:
    print('Expressão inválida!')
