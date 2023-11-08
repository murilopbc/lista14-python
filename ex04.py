import requests
from bs4 import BeautifulSoup

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')
categoria = soup.find_all("div", class_="tags")
for tag in categoria:
    print(tag.get_text())
