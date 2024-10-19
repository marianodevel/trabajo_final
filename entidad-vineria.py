from abc import ABC, abstractmethod

class EntidadVineria(ABC):
    def __init__(self, id: str, nombre: str):
        """
        Constructor de la clase EntidadVineria
        
        Args:
            id (str): Identificador único de la entidad
            nombre (str): Nombre de la entidad
        """
        self.__id = id
        self.__nombre = nombre
    
    def establecer_nombre(self, nombre: str) -> None:
        """
        Establece un nuevo nombre para la entidad
        
        Args:
            nombre (str): Nuevo nombre a establecer
        """
        self.__nombre = nombre
    
    def obtener_id(self) -> str:
        """
        Obtiene el ID de la entidad
        
        Returns:
            str: ID de la entidad
        """
        return self.__id
    
    def obtener_nombre(self) -> str:
        """
        Obtiene el nombre de la entidad
        
        Returns:
            str: Nombre de la entidad
        """
        return self.__nombre
    
    def __eq__(self, other) -> bool:
        """
        Sobrescribe el método de comparación para comparar por ID
        
        Args:
            other: Otra instancia de EntidadVineria para comparar
            
        Returns:
            bool: True si los IDs son iguales, False en caso contrario
        """
        if not isinstance(other, EntidadVineria):
            return False
        return self.__id == other.obtener_id()
