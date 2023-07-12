from abc import ABCMeta

"""
Constructor especial el cual permitirá instanciar un objeto del tipo
requerido a partir de la información almacenada en un diccionario.
"""


class AbstractModelo(metaclass=ABCMeta):
    def __init__(self, data):
        for llave, valor in data.items():
            setattr(self, llave, valor)