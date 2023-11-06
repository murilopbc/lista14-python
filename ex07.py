import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')
citacao = soup.find_all('span', {'class': 'text'})
autor = soup.find_all('small', {'class': 'author'})
categoria = soup.find_all('a', {'class': 'tag'})
for quote, author, category in zip(citacao, autor, categoria):
    print(f"Citação: {quote.get_text()}")
    print(f"Autor: {author.get_text()}")
    print(f"Categoria: {category.get_text()}\n")
