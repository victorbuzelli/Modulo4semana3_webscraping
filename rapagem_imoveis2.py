import sqlite3
from requests_html import HTMLSession

# Define the URL to scrape
url = 'https://www.olx.com.br/imoveis/estado-go/grande-goiania-e-anapolis'

# Create an HTML session
session = HTMLSession()

# Send a GET request to the URL
response = session.get(url)

# Extract links to individual listings
links = response.html.find("#main-content section a")

# Create a list to store extracted data
imoveis = []

# Loop through the links and scrape data
for link in links:
    url_imovel = link.attrs['href']
    response_imovel = session.get(url_imovel)
    titulo = response_imovel.html.find('h1', first=True).text
    preco = response_imovel.html.find('h2')[0].text
    imoveis.append({
        'url': url_imovel,
        'titulo': titulo,
        'preco': preco
    })

# Connect to the SQLite database using a context manager
with sqlite3.connect('banco.sqlite3') as conexao:
    cursor = conexao.cursor()

    # Check if the "imovel" table exists and create it if it doesn't
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS imovel (
            id INTEGER PRIMARY KEY,
            url TEXT,
            titulo TEXT,
            preco TEXT
        )
    ''')

    # Insert data into the "imovel" table
    for imovel in imoveis:
        valores = (imovel['url'], imovel['titulo'], imovel['preco'])
        cursor.execute('INSERT INTO imovel (url, titulo, preco) VALUES (?, ?, ?)', valores)

# No need to commit or close the connection explicitly; it's done automatically

print("Data inserted successfully.")
