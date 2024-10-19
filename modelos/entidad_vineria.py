from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    def __init__(self, id_: str, nombre: str):
        self._id = id_
        self._nombre = nombre
    
    def establecer_nombre(self, nombre: str) -> None:
        self._nombre = nombre
    
    def obtener_id(self) -> str:
        return self._id
    
    def obtener_nombre(self) -> str:
        return self._nombre
    
    def __eq__(self, other) -> bool:
        if not isinstance(other, EntidadVineria):
            return False
        return self._id == other.obtener_id()
