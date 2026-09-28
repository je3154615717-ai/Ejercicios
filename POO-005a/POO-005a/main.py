from servicios.gestion_libros import (
    crear_libro,
    mostrar_libro,
    prestar_libro,
    devolver_libro
)

def menu():
    print("\n--- Menú Biblioteca ---")
    print("1. Mostrar información del libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Salir")

def main():
    libro1 = crear_libro("Cien años de soledad", "Gabriel García Márquez", 1967, "Novela")

    while True:
        menu()
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            mostrar_libro(libro1)
        elif opcion == "2":
            prestar_libro(libro1)
        elif opcion == "3":
            devolver_libro(libro1)
        elif opcion == "4":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
