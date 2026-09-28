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

def cambiar_titulo(libro, nuevo_titulo):
    imprimir(libro.set_titulo(nuevo_titulo))

def cambiar_autor(libro, nuevo_autor):
    imprimir(libro.set_autor(nuevo_autor))

