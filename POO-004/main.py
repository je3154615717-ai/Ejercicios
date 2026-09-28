from servicios.gestion_personas import (
    crear_persona,
    mostrar_persona,
    actualizar_ocupacion,
    celebrar_cumple
)

def main():
    persona1 = crear_persona("Andrés", 30, "Ingeniero")

    mostrar_persona(persona1)
    actualizar_ocupacion(persona1, "Desarrollador de Software")
    celebrar_cumple(persona1)

if __name__ == "__main__":
    main()
