produto = totalgasto = maisdemil = maisbarto = barato = 0
produtobarato = str
while True:
    # Pegando somente um caractere de resposta do usuário e transformando em maiúsculo
    perg = str(input('Quer realizar o cadastro de um prodoto? [S/N]')).strip().upper()[0]
    # Teste para continuar caso a respostas seja 'S'
    if perg == 'S':
        produto += 1
        while True:
            nome = str(input('Informe o nome do produto: ')).strip()
            # Validação do preço
            while True:
                preço = float(input('Preço: R$'))
                if preço <= 0.00:
                    print('\033[1;31mRespota inválida!\033[m')
                else:
                    break
            # Total gasto
            totalgasto += preço
            # Produtos que custam mais de R$1000.00
            if preço > 1000:
                maisdemil += 1
            # Nome do produto mais barato
            if barato == 0:
                barato = preço
                produtobarato = nome
            elif preço < barato:
                barato = preço
                produtobarato = nome
            break
    elif perg == 'N':
        break
    else:
        print('\033[1;31mRespota inválida!\033[m')
print(f'''
a) TOTAL DE PRODUTOS CADASTRADOS: {produto}
b) TOTAL GASTO NA(S) COMPRA(S): {totalgasto}
c) NOME DO PRODUTO MAIS BARATO: {produtobarato}
''')
