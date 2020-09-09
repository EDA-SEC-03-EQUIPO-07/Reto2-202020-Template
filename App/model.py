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


def crear(tipo, comparador):
    return lt.newList(tipo, comparador)

# Funciones para agregar informacion al catalogo


def añadir(lst, element):
    lt.addFirst(lst, element)


def añadirAlFinal(lst, element):
    lt.addLast(lst, element)


def insertarElemento(lst, elemento, pos):
    lt.insertElement(lst, elemento, pos)

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
def compareRecordIds(recordA, recordB):
    if int(recordA['id']) == int(recordB['id']):
        return 0
    elif int(recordA['id']) > int(recordB['id']):
        return 1
    return - 1
