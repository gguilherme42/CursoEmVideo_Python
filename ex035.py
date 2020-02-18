
print('três retas formam um triângulo?'.upper())
a1 = float(input('Digite o comprimento da reta (mm): '))
a2 = float(input('Digite o comprimento da reta (mm): '))
a3 = float(input('Digite o comprimento da reta (mm): '))
if a1 < (a2 + a3) and a2 < (a1 + a3) and a3 < (a2 + a1):
    print('As retas formam um triângulo')
else:
    print('As retas não formam um triângulo')
'''Nenhuma reta pode ser maior que a soma de outras duas
para formar um triângulo'''
