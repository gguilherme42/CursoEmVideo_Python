print('\033[1;4;30mTrês retas formam um triângulo? Se sim, qual tipo de triângulo?\033[m'.upper())
a1 = float(input('\033[1mDigite o comprimento da reta (mm): '))
a2 = float(input('Digite o comprimento da reta (mm): '))
a3 = float(input('Digite o comprimento da reta (mm): \033[m'))
if a1 < (a2 + a3) and a2 < (a1 + a3) and a3 < (a2 + a1):
    if a1 == a2 == a3:
        print('\033[1;33mAs retas formam um triângulo e ele é Equilátero.\033[m')
    elif a1 == a2 or a1 == a3 or a2 == a3:
        print('\033[1;33mAs retas formam um triângulo e ele é Isósceles.\033[m')
    else:
        print('\033[1;33mAs retas formam um triângulo e ele é Escaleno\033[m')
else:
    print('\033[1;33mAs retas não formam um triângulo\033[m')
