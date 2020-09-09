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
    print("0- Salir")


def main():
    lstmovies = controller.crearCatalogo()
    lstcasting = controller.crearCatalogo()
    while True:
        printMenu()  # imprimir el menu de opciones en consola

        # leer opción ingresada
        inputs = input('Seleccione una opción para continuar\n')
        if len(inputs) > 0:
            if int(inputs[0]) == 1:  # opcion 1
                controller.loadCSVFile(lstmovies, csvmovies)
                controller.loadCSVFile(lstcasting, csvcasting)
                mostrarCarga(lstmovies)
            elif int(inputs[0]) == 0:  # opcion 0, salir
                sys.exit(0)


# Nos permite detectar si el archivo es un modulo que fue importado o no.
if __name__ == "__main__":
    main()

