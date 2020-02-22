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
if lista in '()':
    if lista.count('(') == lista.count(')'):

    else:
        print('Expressão errada!')
