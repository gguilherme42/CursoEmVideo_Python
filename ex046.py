#CONTAGEM REGRESSIVA PARA OS FOGOS DE ARTFÍCIOS
from time import sleep
for c in range(10, -1, -1):
    print('\033[1;35m{}\033[m'.format(c))
    sleep(1)
print('\033[1;33mKABUMMMM!\033[m')
