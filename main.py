import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(response.text, 'html.parser')
titulo = soup.title.string

print("O título da página https://quotes.toscrape.com/ é: ", titulo)
