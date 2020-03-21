'''
Exercício 115:
    Crie um pequena sistema modularizado que permita
    cadastrar pessoas pelo seu nome e idade em um arquivo
    de texto simples.

    O sistema só vai ter 2 opções: cadastras uma nova pessoa
    e listar todas as pessoas cadastradas.
'''
import funcionalidades
import purpurina
while True:
    op = funcionalidades.menu()
    if op == 1:
        purpurina.escreve('1 - LISTA')
        funcionalidades.leitura()
    elif op == 2:
        purpurina.escreve('2 - NOVO CADASTRO')
        funcionalidades.novo()
    elif op == 3:
        purpurina.escreve('3 - SAIR')
        break
