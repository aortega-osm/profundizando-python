# leer contenido online
import urllib
from urllib.request import urlopen
palabra=[]
peticion = urllib.request.Request(
    'http://globalmentoring.com.mx/recursos/GlobalMentoring.txt',
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)
with urlopen(peticion) as mensaje:
 contenido = mensaje.read().decode('utf-8')
 # print(contenido)

    # si queremos leer palabra por palabra del texto
for linea in mensaje:
    palabras_por_linea = linea.split()
    for palabra in palabras_por_linea:
        palabra.append(palabra)
print(palabra)