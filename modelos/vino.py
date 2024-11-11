import json
from typing import List, Dict, TYPE_CHECKING
from .entidad_vineria import EntidadVineria

if TYPE_CHECKING:
    from .bodega import Bodega
    from .cepa import Cepa
    from vinoteca import Vinoteca


class Vino(EntidadVineria):
    """
    Clase que representa un vino en el sistema de la vinoteca.
    Hereda de EntidadVineria y mantiene información sobre la bodega,
    cepas y partidas asociadas.
    """
    
    def __init__(self, id: str, nombre: str, bodega_id: str, 
                 cepa_ids: List[str], partidas: List[int]) -> None:
        """
        Inicializa una instancia de Vino.

        Args:
            id: Identificador único del vino
            nombre: Nombre del vino
            bodega_id: Identificador de la bodega productora
            cepa_ids: Lista de identificadores de cepas utilizadas
            partidas: Lista de años de las partidas disponibles
        """
        super().__init__(id, nombre)
        self._bodega_id = bodega_id
        self._cepa_ids = cepa_ids
        self._partidas = partidas

    def establecer_bodega(self, bodega_id: str) -> None:
        """
        Establece la bodega del vino.

        Args:
            bodega_id: Identificador de la bodega
        """
        self._bodega_id = bodega_id

    def establecer_cepa(self, cepa_ids: List[str]) -> None:
        """
        Establece las cepas del vino.

        Args:
            cepa_ids: Lista de identificadores de cepas
        """
        self._cepa_ids = cepa_ids

    def establecer_partidas(self, partidas: List[int]) -> None:
        """
        Establece las partidas del vino.

        Args:
            partidas: Lista de años de las partidas
        """
        self._partidas = partidas

    def obtener_bodega(self) -> 'Bodega':
        """
        Obtiene el objeto Bodega asociado al vino.
        Utiliza el servicio buscarBodega de la clase Vinoteca.

        Returns:
            Objeto Bodega correspondiente a la bodega del vino
        """
        from vinoteca import Vinoteca
        return Vinoteca.buscar_bodega(self._bodega_id)

    def obtener_cepa(self) -> List['Cepa']:
        """
        Obtiene la lista de objetos Cepa asociados al vino.
        Utiliza el servicio buscarCepa de la clase Vinoteca.

        Returns:
            Lista de objetos Cepa correspondientes a las cepas del vino
        """
        from vinoteca import Vinoteca
        return [Vinoteca.buscar_cepa(cepa_id) for cepa_id in self._cepa_ids]

    def obtener_partidas(self) -> List[int]:
        """
        Obtiene la lista de partidas del vino.

        Returns:
            Lista de años de las partidas disponibles
        """
        return self._partidas

    def convertir_a_json(self) -> Dict:
        """
        Convierte el vino a una representación JSON básica.

        Returns:
            Diccionario con la información básica del vino
        """
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "bodega": self.obtener_bodega().obtener_nombre(),
            "cepas": [cepa.obtener_nombre() for cepa in self.obtener_cepa()],
            "partidas": self._partidas
        }

    def convertir_a_json_full(self) -> Dict:
        """
        Convierte el vino a una representación JSON completa.
        En esta implementación, retorna la misma información que convertir_a_json.

        Returns:
            Diccionario con la información completa del vino
        """
        return self.convertir_a_json()

    def __repr__(self) -> str:
        """
        Retorna una representación en string del objeto.
        Utiliza solo el nombre para la representación.

        Returns:
            String con la representación JSON del vino
        """
        return json.dumps({"nombre": self.obtener_nombre()})
