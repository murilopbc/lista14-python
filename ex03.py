import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')
autor = soup.find_all(class_="author")
for author in autor:
    print("Os autores da página https://quotes.toscrape.com/ são: ", author.get_text())
