# tuplas
tupla = ('zero','um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
         'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
         'quinze', 'dezesseis', 'dezesete', 'dezoito', 'dezenove', 'vinte')
n = int(input('Digite um número inteiro entre 0 e 20: '))
# Validação da respota
while n < 0 or n > 20:
    n = int(input('Tente novamete. Digite um número inteiro entre 0 e 20: '))
# Número digitado corresponde ao item no índice 'n' na tupla. Ex.: 0 corresponde à zero
print(f'Você digitou o número {tupla[n]}')

