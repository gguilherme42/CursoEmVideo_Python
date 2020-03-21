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
        funcionalidades.leitura()
        funcionalidades.listagem()
    elif op == 2:
        funcionalidades.novo()
        funcionalidades.grava()
    elif op == 3:
        purpurina.escreve('Saindo...')
        break
