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

import config as cf
from App import model
import csv


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


def initCatalog():
    """
    Llama la funcion de inicializacion del catalogo del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    catalog = model.newCatalog()
    return catalog


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________


def loadData(catalog, movies_casting, movies_details):
    """
    Carga los datos de los archivos en el modelo
    """
    loadarchive(catalog, movies_casting, True)
    loadarchive(catalog, movies_details, False)


def MoviesSize(catalog):

    return model.MoviesSize(catalog)


def CastingSize(catalog):

    return model.CastingSize(catalog)


def loadarchive(catalog, movies_data, escasting):
    movies_data = cf.data_dir + movies_data
    dialect = csv.excel()
    dialect.delimiter = ";"
    try:
        with open(movies_data, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader:
                if escasting == False:  # si es False carga el archivo movies_details
                    model.addpelicula(row)
                else:  # si es True carga el archivo movies_casting
                    model.addcasting(row)
    except:
        print("Se presento un error en la carga del archivo")
