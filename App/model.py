"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------


def newCatalog():
    """ Inicializa el catálogo de libros
    Crea una lista vacia para guardar todos los libros
    Se crean indices (Maps) por los siguientes criterios:
    Autores
    ID libros
    Tags
    Año de publicacion
    Retorna el catalogo inicializado.
    """
    catalog = {'peliculas': None,
               'peliculasID': None,
               'casting': None,
               'castingID': None,
               'genero': None,
               'año': None,
               'director': None,
               'actor': None,
               'productora': None,
               'pais': None}

    catalog['peliculas'] = lt.newList('SINGLE_LINKED', compareElements)
    catalog['peliculasID'] = mp.newMap(2000,
                                       maptype='CHAINING',
                                       loadfactor=0.5,
                                       comparefunction=compareRecordIds)
    catalog['casting'] = lt.newList('P', compareElements)
    catalog['castingID'] = mp.newMap(2000,
                                     maptype='CHAINING',
                                     loadfactor=0.5,
                                     comparefunction=compareRecordIds)
    catalog['director'] = mp.newMap(200,
                                    maptype='CHAINING',
                                    loadfactor=0.4,
                                    comparefunction=compareRecordIds)
    catalog['actor'] = mp.newMap(600,
                                 maptype='CHAINING',
                                 loadfactor=0.4,
                                 comparefunction=compareRecordIds)
    catalog['productora'] = mp.newMap(200,
                                      maptype='CHAINING',
                                      loadfactor=0.4,
                                      comparefunction=compareRecordIds)
    catalog['pais'] = mp.newMap(194,
                                maptype='CHAINING',
                                loadfactor=0.5,
                                comparefunction=compareRecordCountry)
    catalog['año'] = mp.newMap(150,
                               maptype='CHAINING',
                               loadfactor=0.5,
                               comparefunction=compareRecordYear)
    catalog['genero'] = mp.newMap(150,
                                  maptype='CHAINING',
                                  loadfactor=0.5,
                                  comparefunction=compareRecordIds)

    return catalog

# Funciones para agregar informacion al catalogo


def cargarPeliculas(catalogo, element):
    peliculas = catalogo['peliculas']
    peliculasID = catalogo['peliculasID']
    genero = catalogo['genero']
    año = catalogo['año']
    productora = catalogo['productora']
    pais = catalogo['pais']

    addGenre(genero, element)
    addYear(año, element)
    addProduction(productora, element)
    addCountry(pais, element)

    añadirAlFinal(peliculas, element)
    addMap(peliculasID, element['id'], element)


def cargarCasting(catalogo, element):
    casting = catalogo['casting']
    castingID = catalogo['castingID']
    director = catalogo['director']
    actor = catalogo['actor']

    addActor(actor, element)
    addDirector(director, element)

    añadirAlFinal(casting, element)
    addMap(castingID, element['id'], element)


def addActor(map, element):
    id = element['id']

    for i in range(1, 6):
        actor_name = element['actor'+str(i)+'_name']
        if actor_name != 'none':
            existactor = mp.contains(map, actor_name)
            if existactor:
                entry = mp.get(map, actor_name)
                añadirAlFinal(me.getValue(entry), id)
            else:
                lst = lt.newList('SINGLE_LINKED', compareElements)
                añadirAlFinal(lst, id)
                addMap(map, actor_name, lst)


def addDirector(map, element):
    id = element['id']
    director_name = element['director_name']
    existdrector = mp.contains(map, director_name)
    if existdrector:
        entry = mp.get(map, director_name)
        añadirAlFinal(me.getValue(entry), id)
    else:
        lst = lt.newList('SINGLE_LINKED', compareElements)
        añadirAlFinal(lst, id)
        addMap(map, director_name, lst)


def addGenre(map, element):
    generos = element['genres'].split('|')
    for i in range(len(generos)):
        genero = generos[i]
        existgenero = mp.contains(map, genero)
        mov = {}

        if existgenero:
            value = me.getValue(mp.get(map, genero))
            value['vote'] = prom(value['vote'], element['vote_count'])
            value['avg'] = prom(value['avg'], element['vote_average'])
            value['size'] = int(value['size']) + 1
            añadirAlFinal(value['table'], element)
        else:
            lst = lt.newList('SINGLE_LINKED', compareElements)
            añadirAlFinal(lst, element)
            mov['vote'] = prom(0.0, element['vote_count'])
            mov['avg'] = prom(0.0, element['vote_average'])
            mov['size'] = 1
            mov['table'] = lst
            addMap(map, genero, mov)


def addYear(map, element):
    year = getYear(element['release_date'])
    existyear = mp.contains(map, year)
    mov = {}

    if existyear:
        value = me.getValue(mp.get(map, year))
        value['vote'] = prom(value['vote'], element['vote_count'])
        value['avg'] = prom(value['avg'], element['vote_average'])
        value['size'] = int(value['size']) + 1
        añadirAlFinal(value['table'], element)
    else:
        lst = lt.newList('SINGLE_LINKED', compareElements)
        añadirAlFinal(lst, element)
        mov['vote'] = prom(0.0, element['vote_count'])
        mov['avg'] = prom(0.0, element['vote_average'])
        mov['size'] = 1
        mov['table'] = lst

        addMap(map, year, mov)


def addProduction(map, element):
    productora = element['production_companies']
    existproductora = mp.contains(map, productora)
    mov = {}

    if existproductora:
        value = me.getValue(mp.get(map, productora))
        value['vote'] = prom(value['vote'], element['vote_count'])
        value['avg'] = prom(value['avg'], element['vote_average'])
        value['size'] = int(value['size']) + 1
        añadirAlFinal(value['table'], element)
    else:
        lst = lt.newList('SINGLE_LINKED', compareElements)
        añadirAlFinal(lst, element)
        mov['vote'] = prom(0.0, element['vote_count'])
        mov['avg'] = prom(0.0, element['vote_average'])
        mov['size'] = 1
        mov['table'] = lst

        addMap(map, productora, mov)


def addCountry(map, element):
    country = element['production_countries']
    existcountry = mp.contains(map, country)
    mov = {}
    if existcountry:
        value = me.getValue(mp.get(map, country))
        value['vote'] = prom(value['vote'], element['vote_count'])
        value['avg'] = prom(value['avg'], element['vote_average'])
        value['size'] = int(value['size']) + 1
        añadirAlFinal(value['table'], element)
    else:
        lst = lt.newList('SINGLE_LINKED', compareRecordCountry)
        añadirAlFinal(lst, element)
        mov['vote'] = prom(0.0, element['vote_count'])
        mov['avg'] = prom(0.0, element['vote_average'])
        mov['size'] = 1
        mov['table'] = lst

        addMap(map, country, mov)


def añadir(lst, element):
    lt.addFirst(lst, element)


def añadirAlFinal(lst, element):
    lt.addLast(lst, element)


def insertarElemento(lst, elemento, pos):
    lt.insertElement(lst, elemento, pos)


def addMap(map, key, value):
    mp.put(map, key, value)

# ==============================
# Funciones de consulta
# ==============================


def darPrimero(lst):
    return lt.firstElement(lst)


def darUltimo(lst):
    return lt.lastElement(lst)


def darElemento(lst, pos):
    return lt.getElement(lst, pos)


def darTamaño(lst):
    return lt.size(lst)


# ==============================
# Funciones de Comparacion
# ==============================
def compareRecordIds(id, recordB):
    if str(id) == str(recordB['key']):
        return 0
    elif str(id) > str(recordB['key']):
        return 1
    return - 1


def compareRecordTitle(title, recordB):
    if str(title) == str(recordB['key']):
        return 0
    elif str(title) > str(recordB['key']):
        return 1
    return - 1


def compareElements(recordA, recordB):
    if recordA == recordB:
        return 0
    return - 1


def compareRecordCountry(country, recordB):
    if str(country) == str(recordB['key']):
        return 0
    elif str(country) > str(recordB['key']):
        return 1
    return - 1


def compareRecordYear(year, recordB):
    if str(year) == str(recordB['key']):
        return 0
    elif str(year) > str(recordB['key']):
        return 1
    return - 1

# ==============================
# Funciones de ayuda
# ==============================


def getYear(str):
    year = None
    y = str.split('/')
    if len(y) == 3:
        year = y[2]

    return year


def prom(num1, num2):
    promedio = float(num1)
    if float(num2):
        n2 = float(num2)
        if num1 == 0.0:
            promedio = n2
        return (promedio+n2)/2.0
    else:
        return promedio

# ==============================
# Requerimientos
# ==============================

# REQ. 1: Descubrir productoras de cine


def getMoviesByProducer(catalog, producer_name):
    producer_info = mp.get(catalog['productora'], producer_name)
    movies = None
    if producer_info:
        movies = me.getValue(producer_info)

    size = 0
    avg = 0.0
    if movies:
        size = movies['size']
        avg = movies['avg']

    return movies['table'], size, avg

# REQ. 2: Conocer a un director


def getMoviesByDirector(catalog, director_name):
    director_info = mp.get(catalog['director'], director_name)
    peliculasID = catalog['peliculasID']
    movies = None
    if director_info:
        movies = me.getValue(director_info)

    size = -1
    avg = 0.0
    myMov = lt.newList('SINGLE_LINKED', compareRecordIds)
    if movies:
        size = lt.size(movies)
        for i in range(1, size + 1):
            mov = me.getValue(mp.get(peliculasID, darElemento(movies, i)))
            lt.addLast(myMov, mov)
            avg = avg + float(mov['vote_average'])

    return myMov, size, avg/size

# REQ. 3: Conocer a un actor


def getMoviesByActor(catalog, actor_name):
    actor_info = mp.get(catalog['actor'], actor_name)
    peliculasID = catalog['peliculasID']
    castingID = catalog['castingID']
    movies = None

    if actor_info:
        movies = me.getValue(actor_info)

    size = -1
    avg = 0.0
    myDirector = {}
    directorName = ''
    directorCols = 0
    myMov = lt.newList('SINGLE_LINKED', compareRecordIds)

    if movies:
        size = lt.size(movies)
        for i in range(1, size + 1):
            mov = me.getValue(mp.get(peliculasID, darElemento(movies, i)))
            lt.addLast(myMov, mov)
            avg = avg + float(mov['vote_average'])

            cast = me.getValue(mp.get(castingID, darElemento(movies, i)))
            dir_name = cast['director_name']

            # revisa si la llave existe
            if dir_name in myDirector:
                myDirector[dir_name] = int(myDirector[dir_name]) + 1
                if directorCols < int(myDirector[dir_name]):
                    directorCols = int(myDirector[dir_name])
                    directorName = dir_name
            else:
                myDirector[dir_name] = 1

    return myMov, size, avg/size, directorName


# REQ. 4: Entender un género cinematográfico


def getMoviesByGenre(catalog, genre_name):
    genre_info = mp.get(catalog['genero'], genre_name)
    movies = None
    if genre_info:
        movies = me.getValue(genre_info)

    size = 0
    vote = 0.0
    if movies:
        size = movies['size']
        vote = movies['vote']

    return movies['table'], size, vote


# REQ. 5: Encontrar películas por país


def getMoviesByCountry(catalog, country_name):
    country_info = mp.get(catalog['pais'], country_name)
    movies = None
    if country_info:
        movies = me.getValue(country_info)

    theMovies = lt.newList('SINGLE_LINKED', compareRecordTitle)
    if movies:
        size = int(movies['size'])
        for i in range(1, size + 1):
            mov = {}
            title = darElemento(movies['table'], i)['title']
            year = getYear(darElemento(movies['table'], i)['release_date'])
            director = me.getValue(
                mp.get(catalog['castingID'], darElemento(movies['table'], i)['id']))['director_name']

            mov['title'] = title
            mov['year'] = year
            mov['director'] = director

            añadirAlFinal(theMovies, mov)

    return theMovies
