from modelos.libro import Libro
from utils.mensajes import imprimir

def crear_libro(titulo, autor, anio, genero):
    return Libro(titulo, autor, anio, genero)

def mostrar_libro(libro):
    imprimir(libro.mostrar_informacion())

def prestar_libro(libro):
    imprimir(libro.prestar())

def devolver_libro(libro):
    imprimir(libro.devolver())
