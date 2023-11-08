import requests
from bs4 import BeautifulSoup
import csv

base_url = 'https://quotes.toscrape.com'
page_number = 1

with open("citacao.csv", "w", newline="", encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    while True:
        url = f'{base_url}/page/{page_number}/'

        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        quotes = soup.find_all("span", class_="text")

        for quote in quotes:
            csv_writer.writerow([quote.get_text()])

        next_page = soup.find("li", class_="next")
        if next_page:
            page_number += 1
        else:
            break

print("Citações foram salvas em 'citacao.csv'")
