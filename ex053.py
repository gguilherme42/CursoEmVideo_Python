#LEITOR DE FRASE PALINDROMA, DESCONSIDERANDO ESPAÇOS E ACENTOS
fr = str(input('DIGITE UMA FRASE: ')).strip().upper()
plvras = fr.split()
#O "''.join()" junta todas as palavras que foram separadas, tornando-se uma coleção
#pelo ".split()" anterior sem espaços entre elas.
junto = ''.join(plvras)
# Dar a variável inverso o valor de '',  é como se atribuí-se a
#ela zero.
inverso = ''
#O seguinte for faz com que se conte a palavra do final para o começo
for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]
print(junto, inverso)
if inverso == junto:
    print('TEMO UM PALÍNDROMO!')
else:
    print('Não temos um palíndromo!')
