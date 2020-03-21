lista = []
pessoas = 0


def pedenome(msg='Nome: '):
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


def pedetelefone(msg='Idade: '):
    from purpurina import cores
    while True:
        try:
            idade = int(input(msg))
        except (ValueError, TypeError):
            print(f'{cores("-> Erro: Digite uma idade válida!", 7)}')
            # continue joga de novo para o while
            continue
        except KeyboardInterrupt:
            print('-> Programa parado!')
            break
        else:
            if 120 >= idade > 0:
                return idade
            else:
                print(f'{cores("-> Erro! Idade inválida", 7)}')


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
    idade = pedetelefone()
    # Trata o nome e o telefone como elementos uma lista
    lista.append([nome, idade])
    pessoas += 1


def menu():
    from purpurina import escreve, cores
    escreve('MENU PRINCIPAL', '-')
    print(f'{cores("1 -", 4)} {cores("Ver pessoas cadastradas", 5)}')
    print(f'{cores("2 -", 4)} {cores("Cadastras novas pessoas", 5)}')
    print(f'{cores("3 -", 4)} {cores("Sair do sistema", 5)}')
    print(f'{cores("-", 4) * 30}')
