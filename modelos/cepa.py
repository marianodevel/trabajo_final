import json
from typing import List, Dict, TYPE_CHECKING
from .entidad_vineria import EntidadVineria

if TYPE_CHECKING:
    from .vino import Vino
    from .bodega import Bodega
    from vinoteca import Vinoteca


class Cepa(EntidadVineria):
    """
    Clase que representa una cepa de vino.
    Hereda de EntidadVineria y provee funcionalidades específicas para
    gestionar los vinos asociados a esta cepa.
    """

    def __init__(self, id_: str, nombre: str) -> None:
        """
        Inicializa una nueva instancia de Cepa.

        Args:
            id_: Identificador único de la cepa
            nombre: Nombre de la cepa
        """
        super().__init__(id_, nombre)

    def obtener_vinos(self) -> List['Vino']:
        """
        Obtiene todos los vinos que utilizan esta cepa.
        Utiliza el servicio obtener_vinos de la clase Vinoteca para
        recuperar la lista completa y filtra los que incluyen esta cepa.

        Returns:
            Lista de vinos que utilizan esta cepa
        """
        from vinoteca import Vinoteca
        todos_vinos = Vinoteca.obtener_vinos()
        return [
            vino for vino in todos_vinos
            if self.obtener_id() in [cepa.obtener_id() for cepa in vino.obtener_cepas()]
        ]

    def convertir_a_json(self) -> Dict:
        """
        Convierte el objeto a un diccionario JSON básico.
        Incluye información resumida de la cepa.

        Returns:
            Diccionario con la información básica de la cepa
        """
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "vinos": len(self.obtener_vinos()),
        }

    def convertir_a_json_full(self) -> Dict:
        """
        Convierte el objeto a un diccionario JSON completo.
        Incluye toda la información de la cepa, incluyendo
        la lista completa de vinos.

        Returns:
            Diccionario con la información completa de la cepa
        """
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "vinos": self.__mapear_vinos(),
        }

    def __mapear_vinos(self) -> List[str]:
        """
        Mapea los vinos a una lista de nombres con su bodega.
        Método auxiliar para la serialización JSON.

        Returns:
            Lista de strings con formato "nombre_vino (nombre_bodega)"
        """
        vinos = self.obtener_vinos()
        vinos_mapa = map(
            lambda a: f"{a.obtener_nombre()} ({a.obtener_bodega().obtener_nombre()})",
            vinos,
        )
        return list(vinos_mapa)

    def __repr__(self) -> str:
        """
        Retorna una representación en string del objeto.
        Utiliza la versión básica del JSON para la representación.

        Returns:
            String con la representación JSON de la cepa
        """
        return json.dumps({"nombre": self.obtener_nombre()})
