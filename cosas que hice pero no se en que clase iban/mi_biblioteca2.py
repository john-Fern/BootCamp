biblioteca = []
libro1 = {"Titulo": "Sueñan los Androides con Ovejas Electricas?", "Autor": "Philip K. Dick", "Año": "1968"}
libro2 = {"Titulo": "El extranjero", "Autor": "Albert Camus", "Año": "1942"}
libro3 = {"Titulo": "1984", "Autor": "George Orwell", "Año": "1949"}

biblioteca.append(libro1)
biblioteca.append(libro2)
biblioteca.append(libro3)

print("\n\t\t=== Mi Biblioteca ===\n")
for i, libro in enumerate(biblioteca, start=1):
    print(f"{i}. {libro["Titulo"]} - {libro["Autor"]} - {libro["Año"]}")

categorias = ("Ficción", "Historia", "Ciencia")
print(f"\nCategorias disponibles: {categorias}\n")

def agregar_libro():

    while True:
            opcion = input("¿Deseas agregar un nuevo libro? (s/n): ").lower()
            if opcion == "s":
                nuevo_libro = {
                    "Titulo": input("Título: "),
                    "Autor": input("Autor: "),
                    "Año": input("Año: ")
                }

                biblioteca.append(nuevo_libro)

                print("Libro agregado con éxito!\n")
            elif opcion == "n":
                break
            else:
                print("Opción invalida. Usa 's' o 'n'")

        
agregar_libro()

print("\n\t\t=== Mi Biblioteca ===\n")
for i, libro in enumerate(biblioteca, start=1):
    print(f"{i}. {libro['Titulo']} - {libro['Autor']} - {libro['Año']}")
        