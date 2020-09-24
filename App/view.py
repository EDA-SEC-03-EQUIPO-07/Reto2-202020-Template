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
csvcasting = 'MoviesCastingRaw-small.csv'
csvmovies = 'SmallMoviesDetailsCleaned.csv'


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________
def mostrarCarga(lst):
    primeraPelicula = controller.darPrimero(lst)
    ultimaPelicula = controller.darUltimo(lst)

    print("El total de peliculas cargadas fue de: " + str(controller.darTamaño(lst)) + "\n"
          + "Primera pelicula: \n"
          + "Titulo: " + primeraPelicula['original_title']
          + " Fecha de estreno: " + primeraPelicula['release_date']
          + " Votación promedio: " + primeraPelicula['vote_average']
          + " Número de votos: " + primeraPelicula['vote_count']
          + " Idioma original: " + primeraPelicula['original_language'] + "\n"

          + "Ultima pelicula: \n"
          + "Titulo: " + ultimaPelicula['original_title'] +
          " Fecha de estreno: " + ultimaPelicula['release_date']
          + " Votación promedio: " + ultimaPelicula['vote_average']
          + " Número de votos: " + ultimaPelicula['vote_count']
          + " Idioma original: " + ultimaPelicula['original_language']
          )

# ___________________________________________________
#  Menu principal
# ___________________________________________________


def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Peliculas")
    print("2- Descubrir productoras de cine")
    print("3- Conocer a un director")
    print("4- Conocer a un actor")
    print("5- Entender un género cinematográfico")
    print("6- Encontrar películas por país")
    print("0- Salir")


def main():
    catalogo = None
    while True:
        printMenu()  # imprimir el menu de opciones en consola

        # leer opción ingresada
        inputs = input('Seleccione una opción para continuar\n')
        if len(inputs) > 0:
            if int(inputs[0]) == 1:  # opcion 1
                catalogo = controller.crearCatalogo()
                controller.loadMovies(catalogo, csvmovies)
                controller.loadCasting(catalogo, csvcasting)
            if int(inputs[0]) == 2:  # opcion 2
                criteria = str(input('Ingrese el nombre de la productora\n'))
                print(controller.moviesByProductionCompany(catalogo, criteria))
            if int(inputs[0]) == 3:  # opcion 3
                criteria = str(input('Ingrese el nombre del director\n'))
                print(controller.moviesbydirector(catalogo, criteria))
            if int(inputs[0]) == 4:  # opcion 4
                criteria = str(input('Ingrese el nombre del actor\n'))
                print(controller.moviesbyactor(catalogo, criteria))
            if int(inputs[0]) == 5:  # opcion 5
                criteria = str(input('Ingrese el genero\n'))
                print(controller.moviesbygenre(catalogo, criteria))
            if int(inputs[0]) == 6:  # opcion 6
                criteria = str(input('Ingrese el pais\n'))
                print(controller.moviesbycountry(catalogo, criteria))
            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


# Nos permite detectar si el archivo es un modulo que fue importado o no.
if __name__ == "__main__":
    main()
