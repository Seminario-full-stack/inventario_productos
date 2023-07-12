
from Modelos.Almacenista import Almacenista
from Modelos.Producto import Producto
from Modelos.Inventario import Inventario
from Repositorio.RepositorioProducto import RepositorioProducto
from Repositorio.RepositorioAlmacenista import RepositorioAlmacenista
from Repositorio.RepositorioInventario import RepositorioInventario

"""
Dentro de la clase se crean unos metodos, estos serán los encargados de manipular
a los modelos, en estos se programarán las tareas básicas tales como crear, listar,
visualizar, modificar y eliminar. (CRUD)
"""


class ControladorInventario():
    """
   constructor que permite llevar a cabo la creacion de instancias del controlador.
   """

    def __init__(self):
        print("Creando ControladorInventario")
        self.repositorioInventario = RepositorioInventario();
        self.repositorioAlmacenista = RepositorioAlmacenista();
        self.repositorioProducto = RepositorioProducto();

    def index(self):
        print("Listar todos los Inventario")
        return self.repositorioInventario.findAll()

    """Asignacion de almacenista y producto a inventario"""

    def create(self, infoInventario, id_almacenista, id_producto):
        print("Crear un Inventario")
        nuevoInventario = Inventario(infoInventario)
        elProducto = Producto(self.repositorioProducto.findById(id_producto))
        elAlmacenista = Almacenista(self.repositorioAlmacenista.findById(id_almacenista))
        nuevoInventario.almacenista = elAlmacenista
        nuevoInventario.producto = elProducto
        return self.repositorioInventario.save(nuevoInventario)

    def show(self, id):
        print("Mostrando un Inventario con id ", id)
        elInventario = Inventario(self.repositorioInventario.findById(id))
        return elInventario.__dict__

    def update(self, id, infoInventario, id_almacenista, id_producto):
        elInventario = Inventario(self.repositorioInventario.findById(id))
        elInventario.fecha = infoInventario["fecha"]
        elInventario.cantidad_inv = infoInventario["cantidad"]
        elAlmacenista = Almacenista(self.repositorioAlmacenista.findById(id_almacenista))
        elProducto = Producto(self.repositorioProducto.findById(id_producto))
        elInventario.almacenista = elAlmacenista
        elInventario.producto = elProducto
        return self.repositorioInventario.save(elInventario)

    """def update(self, id, infoInventario ,id_almacenista,id_producto ):
        print("Actualizando Inventario con id ", id)
        InventarioActual = Inventario(self.repositorioInventario.findById(id))
        elAlmacenista = Almacenista(self.repositorioAlmacenista.findById(id_almacenista))
        elProducto = Producto(self.repositorioProducto.findById(id_producto))
        InventarioActual.producto = elProducto
        InventarioActual.almacenista = elAlmacenista
        return self.repositorioInventario.save(InventarioActual)"""

    def delete(self, id):
        print("Elimiando Inventario con id ", id)
        return self.repositorioInventario.delete(id)


