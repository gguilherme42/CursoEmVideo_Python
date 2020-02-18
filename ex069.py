mais18 = qhomem = qm20 = pessoa = 0
while True:
    # Pegando somente um caractere de resposta do usuário e transformando em maiúsculo
    perg = str(input('Quer realizar um cadastro? [S/N]')).strip().upper()[0]
    # Teste para continuar caso a respostas seja 'S'
    if perg == 'S':
        pessoa += 1
        while True:
            # Validação da idade da pessoa
            while True:
                id = int(input(f'Idade da {pessoa}ª pessoa: '))
                if id <= 0 or id > 115:
                    print('\033[1;31mRespota inválida!\033[m')
                else:
                    break
            # Validação do sexo da pessoa
            while True:
                # Pegando somente um caractere de resposta do usuário e transformando em maiúsculo
                sex = str(input('Qual o sexo: [M/F]')).strip().upper()[0]
                # Validando resposta
                while sex not in 'MF':
                    print('\033[1;31mRespota inválida!\033[m')
            # Quantos homens foram cadastrados
            if sex == 'M':
                qhomem += 1
            # Quantas pessoas são maiores de 18 anos
            if id > 18:
                mais18 += 1
            #Quantas mulheres tem menos de 20
            if sex == 'F' and id < 20:
                qm20 += 1
            break
    elif perg == 'N':
        break
    else:
        print('\033[1;31mRespota inválida!\033[m')
print(f'''
TOTAL DE PESSOAS CADASTRADAS: {pessoa}
a) TOTAL DE PESSOAS COM MAIS DE 18: {mais18}
b) TOTAL DE HOMENS: {qhomem}
c) TOTAL DE MULHERES COM MENOS DE 20 ANOS: {qm20}
''')
