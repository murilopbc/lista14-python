import requests
from bs4 import BeautifulSoup

tag = input("Digite o nome da tag desejada: ")

url = f"http://quotes.toscrape.com/tag/{tag}"
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all("span", class_="text")

if quotes:
    for quote in quotes:
        print(quote.get_text())
