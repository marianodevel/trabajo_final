import json
from typing import List, Dict, TYPE_CHECKING
from .entidad_vineria import EntidadVineria

class Vino(EntidadVineria):
    def __init__(self, id: str, nombre: str, bodega_id: str, 
                 cepa_ids: List[str], partidas: List[int]) -> None:
        super().__init__(id, nombre)
        self.__bodega_id = bodega_id
        self.__cepa_ids = cepa_ids
        self.__partidas = partidas

    def obtener_bodega_id(self) -> str:
        return self.__bodega_id

    def obtener_cepa_ids(self) -> List[str]:
        return self.__cepa_ids

    def establecer_bodega(self, bodega_id: str) -> None:
        self.__bodega_id = bodega_id

    def establecer_cepa(self, cepa_ids: List[str]) -> None:
        self.__cepa_ids = cepa_ids

    def establecer_partidas(self, partidas: List[int]) -> None:
        self.__partidas = partidas

    def obtener_bodega(self) -> 'Bodega':
        from vinoteca import Vinoteca
        return Vinoteca.buscar_bodega(self.__bodega_id)

    def obtener_cepa(self) -> List['Cepa']:
        from vinoteca import Vinoteca
        return [Vinoteca.buscar_cepa(cepa_id) for cepa_id in self.__cepa_ids]

    def obtener_partidas(self) -> List[int]:
        return self.__partidas

    def convertir_a_json(self) -> Dict:
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "bodega": self.obtener_bodega().obtener_nombre(),
            "cepas": [cepa.obtener_nombre() for cepa in self.obtener_cepa()],
            "partidas": self.__partidas
        }
