import requests
from bs4 import BeautifulSoup

num_page = 1
while True:
    url = f'https://quotes.toscrape.com/page/{num_page}/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    quotes = soup.find_all("span", class_="text")
    for quote in quotes:
        print(f"As citações da página {num_page} {url} são: {quote.get_text()}")
    next_page = soup.find("li", class_="next")
    if next_page:
        num_page += 1
    else:
        break
