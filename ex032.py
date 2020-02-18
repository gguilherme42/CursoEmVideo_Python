from datetime import date
print('ano bissexto'.upper())
ano = int(input('Digite um ano (caso queira analisar o ano atual, digite 0): '))
if ano == 0:
    ano = date.today().year #Pega o ano atual do SO.
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))
