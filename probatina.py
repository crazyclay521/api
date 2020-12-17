import requests

direccion = 'http://www.omdbapi.com/?apikey=eeb2fd4a&i=tt3896198'

#hacer peticion http

respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    print(respuesta.text)
    datos = respuesta.json()
    print(datos)
else:
    print('se ha producido un error', respuesta.status)


