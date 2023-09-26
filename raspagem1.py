 from requests_html import HTMLSession
 url = 'https://www.melhorcambio.com/dolar-hoje'
 sessao = HTMLSession()
 resposta = sessao.get(url)
 resposta.text