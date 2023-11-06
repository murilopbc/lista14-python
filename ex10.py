import requests
from bs4 import BeautifulSoup
import csv

num_page = 1
url = f'https://quotes.toscrape.com'
response = requests.get(url)

with open("citas.csv", "w", newline="") as csv_file:
    csv_writer = csv.writer(csv_file)
    while True:
        url = f"{url}/page/{num_page}/"

        # Faça uma solicitação HTTP para a URL
        response = requests.get(url)

        # Verifique se a página foi carregada com sucesso

        soup = BeautifulSoup(response.text, "html.parser")

        # Encontre todas as citações na página
        quotes = soup.find_all("span", class_="text")

        # Escreva cada citação em uma linha no arquivo CSV
        for quote in quotes:
            csv_writer.writerow([quote.get_text()])

        # Verifique se há uma próxima página
        next_page = soup.find("li", class_="next")
        if next_page:
            num_page += 1
        else:
            break

print("Citações foram salvas em 'citacao.csv'.")
