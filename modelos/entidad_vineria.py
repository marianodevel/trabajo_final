from abc import ABC, abstractmethod
from typing import Dict, Any


class EntidadVineria(ABC):
    """
    Clase abstracta base para las entidades de la vinería.
    
    Define la interfaz común para todas las entidades del sistema (Bodega, Cepa, Vino)
    implementando la funcionalidad básica de identificación y nombre.
    """
    
    def __init__(self, id_: str, nombre: str) -> None:
        """
        Inicializa una nueva instancia de EntidadVineria.

        Args:
            id_: Identificador único de la entidad
            nombre: Nombre de la entidad
        """
        self._id = id_
        self._nombre = nombre

    def establecer_nombre(self, nombre: str) -> None:
        """
        Establece un nuevo nombre para la entidad.

        Args:
            nombre: Nuevo nombre para la entidad
        """
        self._nombre = nombre

    def obtener_id(self) -> str:
        """
        Obtiene el identificador único de la entidad.

        Returns:
            Identificador único de la entidad
        """
        return self._id

    def obtener_nombre(self) -> str:
        """
        Obtiene el nombre descriptivo de la entidad.

        Returns:
            Nombre descriptivo de la entidad
        """
        return self._nombre

    @abstractmethod
    def convertir_a_json(self) -> Dict[str, Any]:
        """
        Convierte la entidad a una representación JSON básica.

        Returns:
            Diccionario con la información básica de la entidad
        """
        pass

    @abstractmethod
    def convertir_a_json_full(self) -> Dict[str, Any]:
        """
        Convierte la entidad a una representación JSON completa.

        Returns:
            Diccionario con la información completa de la entidad
        """
        pass

    def __eq__(self, otro: object) -> bool:
        """
        Compara si dos entidades son iguales basándose en su identificador.

        Args:
            otro: Objeto a comparar

        Returns:
            True si los identificadores son iguales, False en caso contrario
        """
        if not isinstance(otro, EntidadVineria):
            return False
        return self._id == otro.obtener_id()
