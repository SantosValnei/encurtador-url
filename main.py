import pyshorteners

url = input('Cole aqui a url: ')

carrega_lib = pyshorteners.Shortener()

gera_url = carrega_lib.tinyurl.short(url)

print(f'URL encurtada: {gera_url}')