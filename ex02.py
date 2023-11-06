import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')
quotes = soup.find_all(class_="text")
for quote in quotes:
    print("As citações da página https://quotes.toscrape.com/ são: ", quote.get_text())
