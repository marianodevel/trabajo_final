class EntidadVineria(ABC):
    def __init__(self, id: str, nombre: str) -> None:
        self.__id = id
        self.__nombre = nombre

    def establecer_nombre(self, nombre: str) -> None:
        self.__nombre = nombre

    def obtener_id(self) -> str:
        return self.__id

    def obtener_nombre(self) -> str:
        return self.__nombre

    @abstractmethod
    def convertir_a_json(self) -> Dict[str, Any]:
        pass

    @abstractmethod
    def convertir_a_json_full(self) -> Dict[str, Any]:
        pass

    def __eq__(self, otro: object) -> bool:
        if not isinstance(otro, EntidadVineria):
            return False
        return self.__id == otro.obtener_id()
