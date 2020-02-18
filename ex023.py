print('=== SEPARADOR DE DÍGITOS NUMÉRICOS')
num = int(input('Digite um número(de 0 à 9999): '))
u = num // 1 % 10
# '%' significa pegar o resto da divisão e através da matemática
#Pode-se fazer este script
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade: {} \n Dezena {} \n Centena: {} \n Milhar: {} '.format(u, d, c, m))


