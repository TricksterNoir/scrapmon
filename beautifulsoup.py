import requests
from bs4 import BeautifulSoup
import requests

class BS4_Retorno:
    def __init__(self, url):
        self.url = url
    
    def abre_site(url):
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'}

        url_page = f'{url}'


        site = requests.get(url_page, headers = headers)
        soup = BeautifulSoup(site.content,'html.parser')

        return soup