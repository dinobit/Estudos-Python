import urllib
import urllib.request
try:
    site = urllib.request.urlopen('10.16.240.47')
except urllib.error.URLError:
    print('O site Pudim não esta acessível no momento.')
else:
    print('Consegui acessar o site Pudim com sucesso!')
    print(site.read())