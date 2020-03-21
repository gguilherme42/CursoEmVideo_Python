lista = []
pessoas = 0


def pedenome(msg='Nome: '):
    from purpurina import cores
    global lista
    while True:
        try:
            nome = str(input(msg)).strip()
        except (ValueError, TypeError):
            print(f'{cores("-> Erro: Digite um nome válido!", 7)}')
            # continue joga de novo para o while
            continue
        except KeyboardInterrupt:
            print('-> Programa parado!')
            break
        else:
            # Se retornar None, o nome não foi cadastrado.
            if pesquisa(nome) is None:
                return nome
            else:
                print(f'{cores("Nome já cadastrado!", 7)}')


def pedeidade(msg='Idade: '):
    from purpurina import cores
    while True:
        try:
            idade = int(input(msg))
        except (ValueError, TypeError):
            print(f'{cores("-> Erro: idade válida!", 7)}')
            # continue joga de novo para o while
            continue
        except KeyboardInterrupt:
            print('-> Programa parado!')
            break
        else:
            if 120 >= idade > 0:
                return idade
            else:
                print(f'{cores("-> Erro: idade inválida", 7)}')


def pesquisa(nome):
    mnome = nome.lower()
    for i, v in enumerate(lista):
        t = v[0]
        if t.lower() == mnome:
            return i
    return None


def novo():
    global lista, pessoas
    nome = pedenome()
    idade = pedeidade()
    # Trata o nome e o telefone como elementos uma lista
    lista.append([nome, idade])
    pessoas += 1


def grava():
    from purpurina import cores
    global lista
    try:
        arquivo = open('sitema.txt', 'w', encoding='utf-8')
        arquivoSalvo = open('sitemasalvo.txt', 'w', encoding='utf-8')
    except Exception as erro:
        print(f'{cores("Erro:", 7)} {erro}')
    else:
        for i, v in enumerate(lista):
            arquivo.write(f'{v[0]}-{v[1]}')
            if pesquisa(v[0]) is None:
                arquivoSalvo.write(f'{v[0]}-{v[1]}')
        arquivo.close()
        arquivoSalvo.close()


def leitura():
    from purpurina import cores
    global lista
    lista = []
    try:
        arquivoSalvo = open('sitemasalvo.txt', 'r', encoding='utf-8')
    except:
        print(f'{cores("Não há arquivo.",7)}')
    else:
        for v in arquivoSalvo.readlines():
            nome, idade = v.strip().split('-')
            lista.append([nome, idade])
        arquivoSalvo.close()


def listagem():
    from time import sleep
    from purpurina import cores
    global lista
    sleep(0.25)
    print(f'{cores("-", 4) * 30}')
    for v in lista:
        print(f'{v[0]} {" " * 25} {v[1]}')
    print(f'{cores("-", 4) * 30}')
    sleep(0.25)


def menu():
    from time import sleep
    from purpurina import escreve, cores
    sleep(0.25)
    escreve('MENU PRINCIPAL', '-')
    print(f'{cores("1 -", 4)} {cores("Ver pessoas cadastradas", 5)}')
    print(f'{cores("2 -", 4)} {cores("Cadastras novas pessoas", 5)}')
    print(f'{cores("3 -", 4)} {cores("Sair do sistema", 5)}')
    print(f'{cores("-", 4) * 30}')
    sleep(0.25)
    return valida()


def valida(perg='Opção: ', inicio=1, fim=3):
    from purpurina import cores
    while True:
        try:
            valor = int(input(perg))
        except Exception as erro:
            print(f'Erro: {cores(erro, 7)}')
        else:
            if inicio <= valor <= fim:
                return valor
            else:
                print(f'{cores("Erro: Digite uma opção válida", 7)}')
