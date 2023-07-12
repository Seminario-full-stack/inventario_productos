from Repositorio.RepositorioAlmacenista import RepositorioAlmacenista
from Repositorio.RepositorioProducto import RepositorioProducto
from Modelos.Producto import Producto
from Modelos.Almacenista import Almacenista


class ControladorAlmacenista():
    def __init__(self):
        self.repositorioAlamcenista = RepositorioAlmacenista()
        self.repositorioProducto = RepositorioProducto()
        print("Creando controlador Almacenista")

    def index(self):
        print("Listar todos los Almacenista")
        return self.repositorioAlamcenista.findAll()

    def create(self, elAlmacenista):
        print("Crear un Almacenista")
        nuevoAlmacenista = Almacenista(elAlmacenista)
        return self.repositorioAlamcenista.save(nuevoAlmacenista)

    def show(self, id):
        elAlmacenista = Almacenista(self.repositorioAlamcenista.findById(id))
        return elAlmacenista.__dict__

    def update(self, id, elAlmacenista):
        print("Actualizando Almacenista con id ", id)
        alamacenistaActual = Almacenista(self.repositorioAlamcenista.findById(id))
        alamacenistaActual.nombre = elAlmacenista["nombre"]
        alamacenistaActual.cedula = elAlmacenista["cedula"]
        alamacenistaActual.direccion = elAlmacenista["direccion"]
        alamacenistaActual.celular = elAlmacenista["celular"]
        return self.repositorioAlamcenista.save(alamacenistaActual)

    def delete(self, id):
        return self.repositorioAlamcenista.delete(id)

    """def asignarProducto(self, id, id_producto):
        almacenistaActual = Almacenista(self.repositorioAlamcenista.findById(id))
        productoActual = Producto(self.repositorioProducto.findById(id_producto))
        almacenistaActual.producto = productoActual
        return self.repositorioAlamcenista.save(almacenistaActual)"""
