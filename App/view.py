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

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

listCasting = 'MoviesCastingRaw-small.csv'
listMovies = 'SmallMoviesDetailsCleaned.csv'

# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def printInfo():
    print("La primera pelicula cargada es: " + str(controller.darPrimero(movies)['original_title']))
    print("La fecha de estreno fue: " + str(controller.darPrimero(movies)['release_date']))
    print("El promedio de votación fue: " + str(controller.darPrimero(movies)['vote_average']))
    print("El numero de votos fue: " + str(controller.darPrimero(movies)['vote_count']))
    print("El idioma original es: " + str(controller.darPrimero(movies)['original_language']))

    print("La última pelicula cargada es: " + str(controller.darUltimo(movies)['original_title']))
    print("La fecha de estreno fue: " + str(controller.darUltimo(movies)['release_date']))
    print("El promedio de votación fue: " + str(controller.darUltimo(movies)['vote_average']))
    print("El numero de votos fue: " + str(controller.darUltimo(movies)['vote_count']))
    print("El idioma original es: " + str(controller.darUltimo(movies)['original_language']))
    
# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("Bienvenido")
    print("1- Inicializar catálogo")
    print("2- Cargar peliculas en el catálogo")
    print("0- Salir")

while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        movies = controller.crearCatalogo()
        casting = controller.crearCatalogo()
        print("Catalogo inicializado")
    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadCSVFile(movies, listMovies)
        controller.loadCSVFile(casting, listCasting)
        print("Peliculas cargadas: " + str(controller.darTamaño(movies)))
        printInfo()
    else:
        sys.exit(0)
sys.exit(0)