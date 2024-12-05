class Libro:
    def __init__(self, id_libro, nombre, autor, categoria, anio):
        self.id_libro = id_libro
        self.nombre = nombre
        self.autor = autor
        self.categoria = categoria
        self.anio = anio
        self.disponible = True  # Estado del libro

    def __str__(self):
        return f"ID: {self.id_libro}, Nombre: {self.nombre}, Autor: {self.autor}, Categoría: {self.categoria}, Año: {self.anio}, Disponible: {self.disponible}"

class libreria:
    def __init__(self):
        self.libros = []
        self.prestamos = {}
        self.usuarios = {}

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_por_categoria(self, categoria):
        resultados = [libro for libro in self.libros if libro.categoria.lower() == categoria.lower() and libro.disponible]
        return resultados

    def prestar_libro(self, id_libro, usuario):
        for libro in self.libros:
            if libro.id_libro == id_libro and libro.disponible:
                libro.disponible = False
                self.prestamos[usuario] = libro
                print(f"Libro '{libro.nombre}' prestado a {usuario}.")
                return
        print("El libro no está disponible")

    def devolver_libro(self, usuario):
        if usuario in self.prestamos:
            libro = self.prestamos.pop(usuario)
            libro.disponible = True
            print(f"Libro '{libro.nombre}' devuelto por {usuario}.")
        else:
            print("El usuario no tiene libros prestados.")

    def verificar_penalizacion(self, usuario):
        if usuario in self.prestamos:
            print(f"{usuario} tiene un libro pendiente de devolución.")
        else:
            print(f"{usuario} no tiene penalizaciones.")

if __name__ == "__main__":
    biblioteca = libreria()

    # Agregar libros
    biblioteca.agregar_libro(Libro(1, "Atraves de mi ventana", "Esteban", "Ficción", 2001))
    biblioteca.agregar_libro(Libro(2, "A Dos Metros de Ti ", "Julion", "Novela", 2015))
    biblioteca.agregar_libro(Libro(3, "After", "Hardin", "Romance", 2012))

    # Buscar libros por categoría
    categoria = "Ficción"
    print(f"Buscando libros en la categoría '{categoria}':")
    resultados = biblioteca.buscar_por_categoria(categoria)
    for libro in resultados:
        print(libro)

    # Prestar un libro
    print("\nPrestando un libro:")
    biblioteca.prestar_libro(1, "Emmanuel")

    # Intentar prestar el mismo libro de nuevo
    print("\nIntentando prestar el mismo libro de nuevo:")
    biblioteca.prestar_libro(1, "Jasmin")

    # Verificar penalización
    print("\nVerificando penalizaciones:")
    biblioteca.verificar_penalizacion("Emmanuel")
    biblioteca.verificar_penalizacion("Yasmin")

    # Devolver un libro
    print("\nDevolviendo un libro:")
    biblioteca.devolver_libro("Emmanuel")

    # Verificar penalización nuevamente
    print("\nVerificando penalizaciones después de la devolución:")
    biblioteca.verificar_penalizacion("Jasmin")
