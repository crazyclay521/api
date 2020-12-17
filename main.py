import requests

pregunta = input('titulo de la pelicula:')

API_KEY = 'eeb2fd4a'
direccion = f'http://www.omdbapi.com/?apikey={API_KEY}&s={pregunta}'

respuesta = requests.get(direccion)

if respuesta.status_code == 200:
    datos = respuesta.json()
    if datos['Response'] == 'False':
        print(datos['Error'])
    else:
        primera_peli = datos['Search'][0]
        clave = primera_peli['imdbID']
        otra_direccion = 'http://www.omdbapi.com/?apikey={}&i={}'.format(API_KEY, clave)
        nueva_respuesta = requests.get(otra_direccion)
        if nueva_respuesta.status_code == 200:
            datos = nueva_respuesta.json()
            if datos['Response'] == 'False':
                print(datos['Error'])
            else:
                titulo = datos['Title']
                año = datos['Year']
                director = datos['Director']
                print('La peli {}, estrenada en el año {}, fue dirigida por {}'.format(titulo,año,director))
        else:
            print('error en consulta', nueva_respuesta.status_code)
else:
    print('error en consulta', respuesta.status_code)
