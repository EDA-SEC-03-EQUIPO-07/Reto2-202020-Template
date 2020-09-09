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

movies_casting = "MoviesCastingRaw-small.csv"
movies_details = "SmallMoviesDetailsCleaned.csv"


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________


# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información de peliculas")
    print("3- Descubrir productoras de cine")
    print("4- Conocer a un director")
    print("5- Conocer a un actor")
    print("6- Entender un género cinematográfico")
    print("7- Encontrar películas por país")
    print("0- Salir")


"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(cont, movies_casting, movies_details)
        print('Peliculas cargadas: ' + str(controller.MovieSize(cont)))
        print('Peliculas cargadas: ' + str(controller.CastingSize(cont)))
        #print('Géneros cargados: ' + str(controller.tagsSize(cont)))

    elif int(inputs[0]) == 3:
        name = input("Nombre de la productora de cine: ")
        #books = controller.getBooksYear(cont, int(number))
        # ·printBooksbyYear(books)

    elif int(inputs[0]) == 4:
        director_name = input("Nombre del director: ")
        #authorinfo = controller.getBooksByAuthor(cont, authorname)
        # printAuthorData(authorinfo)

    elif int(inputs[0]) == 5:
        actor_name = input("Nombre del actor: ")
        #books = controller.getBooksByTag(cont, label)
        # printBooksbyTag(books)

    elif int(inputs[0]) == 6:
        name = input("Nombre del genero cinematográfico: ")
        #books = controller.getBooksByTag(cont, label)
        # printBooksbyTag(books)

    elif int(inputs[0]) == 7:
        country_name = input("Nombre del país: ")
        #books = controller.getBooksByTag(cont, label)
        # printBooksbyTag(books)

    else:
        sys.exit(0)
sys.exit(0)
