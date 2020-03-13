'''
    Crie um código em Python que teste se o site
    Pudim está acessível pelo computador usado.
'''
import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Deu erro!')
else:
    print('Deu certo!')
