import requests
from bs4 import BeautifulSoup

nome_autor = input("Digite o nome do autor: ")

response = requests.get('https://quotes.toscrape.com/')
soup = BeautifulSoup(response.text, 'html.parser')
citacoes = soup.find_all('span', {'class': 'text'}, text=True, string=True)
citacao_autor = []

for quote in citacoes:
    if nome_autor in quote.get_text():
        citacao_autor.append(quote.get_text())

if citacao_autor:
    print(f"Citações do autor '{nome_autor}': ")
    for quote in citacao_autor:
        print(quote)
else:
    print(f"Nenhuma citação encontrada para o autor '{nome_autor}'.")
