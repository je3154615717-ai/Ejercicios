from servicios.gestion_libros import (
    crear_libro,
    mostrar_libro,
    prestar_libro,
    devolver_libro
)

def main():
    libro1 = crear_libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela")

    mostrar_libro(libro1)
    prestar_libro(libro1)
    mostrar_libro(libro1)
    devolver_libro(libro1)
    mostrar_libro(libro1)

if __name__ == "__main__":
    main()
