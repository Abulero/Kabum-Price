import requests
from bs4 import BeautifulSoup as bs


class KabumScraping:
    def __init__(self, product):
        product_url = product.replace(' ', '%20')

        self.url = "https://www.kabum.com.br/cgi-local/site/listagem/listagem.cgi?ordem=3&limite=30&pagina=1&string={product}".format(product=product_url)
        self.url_html = requests.get(self.url).content

    def get_price(self, n):
        self.soup = bs(self.url_html, 'html.parser')

        name_element_list = self.soup.find_all('h2', class_='H-titulo')
        price_element_list = self.soup.find_all('div', class_='listagem-preco')

        if n > len(price_element_list) or n > len(name_element_list):
            return None

        return name_element_list[n].text, price_element_list[n].text
