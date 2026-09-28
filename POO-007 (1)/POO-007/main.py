from servicios.gestion_libros import (
    crear_libro,
    mostrar_libro,
    prestar_libro,
    devolver_libro,
    cambiar_titulo,
    cambiar_autor
)

def menu():
    print("\n--- Menú Biblioteca ---")
    print("1. Mostrar información del libro")
    print("2. Prestar libro")
    print("3. Devolver libro")
    print("4. Cambiar título")
    print("5. Cambiar autor")
    print("6. Salir")

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
            nuevo_titulo = input("Ingrese el nuevo título: ")
            cambiar_titulo(libro1, nuevo_titulo)
        elif opcion == "5":
            nuevo_autor = input("Ingrese el nuevo autor: ")
            cambiar_autor(libro1, nuevo_autor)
        elif opcion == "6":
            print("Saliendo del sistema...")
            break
        else:
            print("Opción inválida, intente de nuevo.")

if __name__ == "__main__":
    main()
