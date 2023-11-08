import requests
from bs4 import BeautifulSoup

nome_autor = input("Digite o nome do autor: ")

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all("span", class_="text")

for quote in quotes:
    autor = quote.find_next("small", class_="author")
    author = autor.get_text()

    if nome_autor in author:
        print(quote.get_text())
