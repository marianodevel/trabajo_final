import json
from typing import List, TYPE_CHECKING
from .entidad_vineria import EntidadVineria

if TYPE_CHECKING:
    from .cepa import Cepa
    from .vino import Vino
    from vinoteca import Vinoteca


class Bodega(EntidadVineria):
    """
    Clase que representa una bodega de vinos.
    Hereda de EntidadVineria y provee funcionalidades específicas para
    gestionar vinos y cepas asociadas.
    """

    def __init__(self, id: str, nombre: str) -> None:
        """
        Inicializa una nueva instancia de Bodega.

        Args:
            id: Identificador único de la bodega
            nombre: Nombre de la bodega
        """
        super().__init__(id, nombre)

    def obtener_vinos(self) -> List['Vino']:
        """
        Obtiene todos los vinos que pertenecen a esta bodega.
        Utiliza el servicio obtener_vinos de la clase Vinoteca para
        recuperar la lista completa y filtra los que corresponden
        a esta bodega.

        Returns:
            Lista de vinos pertenecientes a esta bodega
        """
        from vinoteca import Vinoteca
        todos_vinos = Vinoteca.obtener_vinos()
        return [
            vino for vino in todos_vinos
            if vino.obtener_bodega().obtener_id() == self.obtener_id()
        ]

    def obtener_cepas(self) -> List['Cepa']:
        """
        Obtiene todas las cepas de los vinos que pertenecen a esta bodega.
        Primero obtiene los vinos de la bodega y luego extrae sus cepas únicas.

        Returns:
            Lista de cepas únicas utilizadas en los vinos de esta bodega
        """
        vinos = self.obtener_vinos()
        # Usamos set para eliminar duplicados
        cepas_unicas = {vino.obtener_cepa() for vino in vinos}
        return list(cepas_unicas)

    def convertir_a_json(self) -> dict:
        """
        Convierte el objeto a un diccionario JSON básico.
        Incluye información resumida de la bodega.

        Returns:
            Diccionario con la información básica de la bodega
        """
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "cepas": self.__mapear_cepas(),
            "vinos": len(self.obtener_vinos()),
        }

    def convertir_a_json_full(self) -> dict:
        """
        Convierte el objeto a un diccionario JSON completo.
        Incluye toda la información de la bodega, incluyendo
        la lista completa de vinos.

        Returns:
            Diccionario con la información completa de la bodega
        """
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "cepas": self.__mapear_cepas(),
            "vinos": self.__mapear_vinos(),
        }

    def __mapear_cepas(self) -> List[str]:
        """
        Mapea las cepas a una lista de nombres.
        Método auxiliar para la serialización JSON.

        Returns:
            Lista de nombres de cepas
        """
        cepas = self.obtener_cepas()
        cepas_mapa = map(lambda a: a.obtener_nombre(), cepas)
        return list(cepas_mapa)

    def __mapear_vinos(self) -> List[str]:
        """
        Mapea los vinos a una lista de nombres.
        Método auxiliar para la serialización JSON.

        Returns:
            Lista de nombres de vinos
        """
        vinos = self.obtener_vinos()
        vinos_mapa = map(lambda a: a.obtener_nombre(), vinos)
        return list(vinos_mapa)

    def __repr__(self) -> str:
        """
        Retorna una representación en string del objeto.
        Utiliza la versión básica del JSON para la representación.

        Returns:
            String con la representación JSON de la bodega
        """
        return json.dumps(self.convertir_a_json())
