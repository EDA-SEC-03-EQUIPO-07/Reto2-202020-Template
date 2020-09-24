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


"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""


# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________


def crearCatalogo():
    return model.crear("ARRAY_LIST", model.compareRecordIds)


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadCSVFile(lst, file):
    dialect = csv.excel()
    dialect.delimiter = ";"

    try:
        with open(cf.data_dir + file, encoding="utf-8") as csvfile:
            row = csv.DictReader(csvfile, dialect=dialect)
            for elemento in row:
                model.añadirAlFinal(lst, elemento)
    except:
        print("Hubo un error con la carga del archivo")
    return lst


# ___________________________________________________
#  Otras funciones
# ___________________________________________________
def darPrimero(lst):
    return model.darPrimero(lst)


def darUltimo(lst):
    return model.darUltimo(lst)


def darTamaño(lst):
    return model.darTamaño(lst)


def moviesByProductionCompany(catalog, producer_name):
    producer_info = model.getMoviesByProducer(catalog, producer_name)
    return producer_info


def moviesbydirector(catalog, director_name):
    director_info = model.getMoviesByDirector(catalog, director_name)
    return director_info


def moviesbyactor(catalog, actor_name):
    actor_info = model.getMoviesByActor(catalog, actor_name)
    return actor_info


def moviesbygenre(catalog, genre_name):
    genre_info = model.getMoviesByGenre(catalog, genre_name)
    return genre_info


def moviesbycountry(catalog, country_name):
    country_info = model.getMoviesByCountry(catalog, country_name)
    return country_info
