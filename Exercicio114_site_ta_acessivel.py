import urllib
import urllib3
import requests

try:
    site = input('Insira o site: ')
    check = requests.get(site)
    print('site acessível')

except:
    print('site está indisponível')
