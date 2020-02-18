print('==== ANALISADOR DE TEXTOS ===')
n = str(input('Digite seu nome completo: ')).strip()
#pode-se colocar '.strip()' no final do input a fim de evitar espaços desnecessários
print('Seu nome em maiúsculo é: {}'.format(n.upper()))
print('Seu nome em minúsculo é: {}'.format(n.lower()))
print('Seu nome completo tem {} letras'.format(len(n) - n.count(' ')))
#Macete para subtrair o espaço entre as palavras
print('Seu primeiro nome tem {} letras'.format(n.find(' ')))
#O ".find(' ')" é um macete para contar o primeiro nome
#já que contará até achar o primeiro espaço, isto é,
#o espaço entre o primeiro e o segundo nome, no caso
#do exercício


