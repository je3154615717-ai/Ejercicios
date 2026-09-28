from modelos.persona import Persona
from utils.mensajes import imprimir

def crear_persona(nombre, edad, ocupacion):
    return Persona(nombre, edad, ocupacion)

def mostrar_persona(persona):
    imprimir(persona.mostrar_informacion())

def actualizar_ocupacion(persona, nueva_ocupacion):
    imprimir(persona.cambiar_ocupacion(nueva_ocupacion))

def celebrar_cumple(persona):
    imprimir(persona.cumplir_anios())
