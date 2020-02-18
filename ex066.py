# Leitor de número inteiros com flag no 999
soma = q = 0
while True:
    n = int(input('Digite um número ou 999 para sair do programa\n '))
    if n == 999:
        break
    soma += n
    q += 1
print(f'''
Total de números digitados: {q}
Soma dos números digitados: {soma}
''' )
