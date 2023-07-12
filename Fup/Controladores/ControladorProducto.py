from Repositorio.RepositorioProducto import RepositorioProducto
from Modelos.Producto import Producto


class ControladorProducto():
    def __init__(self):
        self.repositorioProducto = RepositorioProducto()
        print("Creando controlador producto")

    def index(self):
        print("Listar todos los producto")
        return self.repositorioProducto.findAll()

    def create(self, elProducto):
        print("Crear un producto")
        nuevoProducto = Producto(elProducto)
        return self.repositorioProducto.save(nuevoProducto)

    def show(self, id):
        elProducto = Producto(self.repositorioProducto.findById(id))
        return elProducto.__dict__

    def update(self, id, elProducto):
        print("Actualizando producto con id ", id)
        ProductoActual = Producto(self.repositorioProducto.findById(id))
        ProductoActual.nombreProducto = elProducto["nombre"]
        ProductoActual.precio = elProducto["precio"]
        ProductoActual.cantidad = elProducto["cantidad"]
        ProductoActual.descripcion = elProducto["descripcion"]
        return self.repositorioProducto.save(ProductoActual)

    def delete(self, id):
        return self.repositorioProducto.delete(id)


