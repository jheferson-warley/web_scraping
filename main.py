import requests
from bs4 import BeautifulSoup
import csv


url = "http://quotes.toscrape.com"

# Fazendo a requisição ao site
response = requests.get(url)


if response.status_code == 200:

    html_content = response.text

 
    soup = BeautifulSoup(html_content, 'html.parser')

    quotes = soup.find_all('div', class_='quote')


    with open('citacoes.csv', mode='w', newline='', encoding='utf-8-sig') as file:
        writer = csv.writer(file)
        
      
        writer.writerow(['Citação', 'Autor'])

        
        for quote in quotes:
            text = quote.find('span', class_='text').get_text()
            author = quote.find('small', class_='author').get_text()
            writer.writerow([text, author])

    print("As citações e autores foram salvos no arquivo 'citacoes.csv' com sucesso!")

else:
    print(f"Erro ao acessar o site. Código de status: {response.status_code}")
