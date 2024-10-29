class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def obtener_precio(self):
        return self._precio

    def mostrar_info(self):
        return f"{self._nombre}, Precio: {self._precio} Gs."


class Ropa(Producto):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio)
        self._talla = talla
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        return (f"{self._nombre}: Talla: {self._talla}, Tipo de Tela: {self._tipo_tela}")


class Camisa(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_cuello):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_cuello = tipo_cuello

    def mostrar_info(self):
        return (f"Camisa: {self._nombre}, Precio: {self._precio} Gs., "
                f"Talla: {self._talla}, Tipo de Tela: {self._tipo_tela}, "
                f"Tipo de Cuello: {self._tipo_cuello}")


class Pantalon(Ropa):
    def __init__(self, nombre, precio, talla, tipo_tela, tipo_cintura):
        super().__init__(nombre, precio, talla, tipo_tela)
        self._tipo_cintura = tipo_cintura

    def mostrar_info(self):
        return (f"Pantalón: {self._nombre}, Precio: {self._precio} Gs., "
                f"Talla: {self._talla}, Tipo de Tela: {self._tipo_tela}, "
                f"Tipo de Cintura: {self._tipo_cintura}")


class Zapato(Ropa):
    def __init__(self, nombre, precio, talla, tipo_material):
        super().__init__(nombre, precio, talla, tipo_material)
        self._tipo_material = tipo_material

    def mostrar_info(self):
        return (f"Zapato: {self._nombre}, Precio: {self._precio} Gs., "
                f"Talla: {self._talla}, Tipo de Material: {self._tipo_material}")


class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def calcular_total(self):
        return sum(producto.obtener_precio() for producto in self._productos)

    def mostrar_resumen(self):
        if not self._productos:
            return "El carrito está vacío."
        resumen = "Productos en el carrito:\n"
        for producto in self._productos:
            resumen += producto.mostrar_info() + "\n"
        resumen += f"Total a pagar: {self.calcular_total()} Gs."
        return resumen


class Tienda:
    def __init__(self):
        self._productos = [
            Camisa("Camisa Casual", 50000, "M", "Algodón", "Mao"),
            Pantalon("Pantalón Jeans", 70000, "L", "Denim", "Normal"),
            Zapato("Zapato Deportivo", 80000, "42", "Cuero"),
        ]
        self._carrito = Carrito()

    def menu(self):
        print("\nBienvenido a nuestra tienda")
        print("""\nMenú:
        1- Agregar Carrito
        2- Ver carrito
        3- Pagar y salir""")
        print("Selecciona una opción: ")

    def mostrar_productos(self):
        print("\nProductos disponibles:")
        for idx, producto in enumerate(self._productos, start=1):
            print(f"{idx}. {producto.mostrar_info()}")

    def menu_principal(self):
        while True:
            self.menu()
            try:
                opcion = int(input())
                
                if opcion == 1:
                    self.mostrar_productos()
                    producto_seleccionado = int(input("Selecciona el número del producto a agregar al carrito: ")) - 1
                    if 0 <= producto_seleccionado < len(self._productos):
                        self._carrito.agregar_producto(self._productos[producto_seleccionado])
                        print(f"Agregado al carrito: {self._productos[producto_seleccionado].mostrar_info()}")
                    else:
                        print("Producto no válido.")
                elif opcion == 2:
                    print(self._carrito.mostrar_resumen())
                elif opcion == 3:
                    print("Resumen de tu compra:")
                    print(self._carrito.mostrar_resumen())
                    print("Gracias por tu visita. ¡Hasta luego!")
                    break
                else:
                    print("Opción no válida. Por favor, selecciona nuevamente.")
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")

if __name__ == "__main__":
    tienda = Tienda()
    tienda.menu_principal()
