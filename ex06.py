import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')
citacao = soup.find_all("span", class_="text")
autor = soup.find_all("small", class_="author")
for quote, author in zip(citacao, autor):
    print(f"\nCitação: {quote.get_text()}")
    print(f"Autor: {author.get_text()}\n")
