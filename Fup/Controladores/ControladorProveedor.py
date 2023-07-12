from Repositorio.RepositorioProveedor import RepositorioProveedor
from Modelos.Proveedor import Proveedor


class ControladorProveedor():
    def __init__(self):
        self.repositorioProveedor = RepositorioProveedor()
        print("Creando controlador proveedor")

    def index(self):
        print("Listar todos los proveedor")
        return self.repositorioProveedor.findAll()

    def create(self, elProveedor):
        print("Crear un proveedor")
        nuevoProveedor = Proveedor(elProveedor)
        return self.repositorioProveedor.save(nuevoProveedor)

    def show(self, id):
        elProveedor = Proveedor(self.repositorioProveedor.findById(id))
        return elProveedor.__dict__

    def update(self, id, elProveedor):
        print("Actualizando proveedor con id ", id)
        ProveedorActual = Proveedor(self.repositorioProveedor.findById(id))
        ProveedorActual.nombre_proveedor = elProveedor["nombre"]
        ProveedorActual.nit = elProveedor["nit"]
        ProveedorActual.direccion = elProveedor["direccion"]
        ProveedorActual.telefono = elProveedor["telefono"]
        return self.repositorioProveedor.save(ProveedorActual)

    def delete(self, id):
        return self.repositorioProveedor.delete(id)


