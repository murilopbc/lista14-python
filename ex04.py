import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')
categorias = set()
for category in soup.find_all('a', {'class': 'tag'}):
    categorias.add(category.get_text())
    print("As categorias das citações da página https://quotes.toscrape.com/ são:")
    for categoria in categorias:
        print(categoria)

