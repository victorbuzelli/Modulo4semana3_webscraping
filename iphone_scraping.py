from requests_html import HTMLSession
 
sessao = HTMLSession()

url = 'https://www.olx.com.br/eletronicos-e-celulares/estado-sp?q=iphone'

resposta = sessao.get(url)

links = resposta.html.find('#ad-list li a')

for link in links:
    titulo = link.attrs['title']
    print(titulo)

