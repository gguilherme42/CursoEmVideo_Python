'''
Programa que leia 4 valores pelo teclado e guarde numa tupla
Mostrando:
a) Quantas vezes apareceu o valor 9;
b)Em que posição foi digitado o primeiro valor 3;
c) Quais foram os números pares.
'''
'''
@Guilherme
Minha resolução antes de ver o vídeo
'''
# Números inteiros a serem lidos:
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite outro número: '))
tupla = (n1, n2, n3, n4)
print(f'TUPLA: \n{tupla}')
# a)
print(f'O número 9 apareceu {tupla.count(9)} vez(es).')
# b)
# Teste para verificar se o valor 3 está na tupla
if 3 in tupla:
    print(f'O primeiro valor  3 foi digitado no índice {tupla.index(3)} da tupla.')
else:
    print('O valor 3 não foi digitado.')
# c)
# Declaração de variável simples para verificar se há algum número par
tempar = 0
# Repetição para percorrer a tupla e verificar se existe número(s) par.
for c in tupla:
    if c % 2 == 0:
        tempar += 1
# Se há números par, então:
if tempar != 0:
    print('Número(s) par:')
    for ind, c in enumerate(tupla):
        if c % 2 == 0:
            print(c, end=' ')
# Se não há, logo:
else:
    print('Não há número par.')
'''
Resolução do @Guanabara
núm = (int(input('Digite um número')), int(input('Digite um número')), int(input('Digite um número')), 
      int(input('Digite um número')), int(input('Digite um número')))
print(f'O número 9 apareceu {núm.count(9)} vez(es).') 
if 3 in núm:
    print(f'O primeiro valor  3 foi digitado no índice {núm.index(3)} da tupla.')
else:
    print('O valor 3 não foi digitado.')
for  n in núm:
    if n % 2 == 0:
        print(n, end=' ')
'''