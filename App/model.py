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
    catalog = {'books': None,
               'bookIds': None,
               'authors': None,
               'tags': None,
               'tagIds': None,
               'years': None}

    catalog['books'] = lt.newList('SINGLE_LINKED', compareBookIds)
    catalog['bookIds'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareMapBookIds)
    catalog['authors'] = mp.newMap(200,
                                   maptype='PROBING',
                                   loadfactor=0.4,
                                   comparefunction=compareAuthorsByName)
    catalog['tags'] = mp.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=0.7,
                                comparefunction=compareTagNames)
    catalog['tagIds'] = mp.newMap(1000,
                                  maptype='CHAINING',
                                  loadfactor=0.7,
                                  comparefunction=compareTagIds)
    catalog['years'] = mp.newMap(500,
                                 maptype='CHAINING',
                                 loadfactor=0.7,
                                 comparefunction=compareMapYear)

    return catalog


def newAuthor(name):
    """
    Crea una nueva estructura para modelar los libros de un autor
    y su promedio de ratings
    """
    author = {'name': "", "books": None,  "average_rating": 0}
    author['name'] = name
    author['books'] = lt.newList('SINGLE_LINKED', compareAuthorsByName)
    return author


def newTagBook(name, id):
    """
    Esta estructura crea una relación entre un tag y los libros que han sido
    marcados con dicho tag.  Se guarga el total de libros y una lista con
    dichos libros.
    """
    tag = {'name': '',
           'tag_id': '',
           'total_books': 0,
           'books': None,
           'count': 0.0}
    tag['name'] = name
    tag['tag_id'] = id
    tag['books'] = lt.newList()
    return tag


# Funciones para agregar informacion al catalogo


# ==============================
# Funciones de consulta
# ==============================


# ==============================
# Funciones de Comparacion
# ==============================
