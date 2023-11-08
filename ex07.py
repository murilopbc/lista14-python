import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')
citacao = soup.find_all("span", class_="text")
autor = soup.find_all("small", class_="author")
categoria = soup.find_all("div", class_="tags")
for quote, author, category in zip(citacao, autor, categoria):
    print(f"\nCitação: {quote.get_text()}")
    print(f"Autor: {author.get_text()}")
    print(f"{category.get_text()}\n")
