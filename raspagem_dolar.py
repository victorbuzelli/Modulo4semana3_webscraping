from requests_html import HTMLSession

sessao = HTMLSession()

campo = '#taxa-comercial'
url = 'https://www.melhorcambio.com/dolar-hoje'

resposta = sessao.get(url)

dolar = resposta.html.find(campo, first=True)

print(dolar)

print(dolar.attrs['value'])