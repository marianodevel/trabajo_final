import json
from typing import List
from .entidad_vineria import EntidadVineria

class Vino(EntidadVineria):
    def __init__(self, id_: str, nombre: str, bodega_id: str, 
                 cepa_ids: List[str], partidas: List[int]):
        super().__init__(id_, nombre)
        self._bodega_id = bodega_id
        self._cepa_ids = cepa_ids
        self._partidas = partidas
    
    def establecer_bodega(self, bodega_id: str) -> None:
        self._bodega_id = bodega_id
    
    def establecer_cepas(self, cepa_ids: List[str]) -> None:
        self._cepa_ids = cepa_ids
    
    def establecer_partidas(self, partidas: List[int]) -> None:
        self._partidas = partidas
    
    def obtener_bodega(self) -> 'Bodega':
        from .vinoteca import Vinoteca
        return Vinoteca.buscar_bodega(self._bodega_id)
    
    def obtener_cepas(self) -> List['Cepa']:
        from .vinoteca import Vinoteca
        return [Vinoteca.buscar_cepa(cepa_id) for cepa_id in self._cepa_ids]
    
    def obtener_partidas(self) -> List[int]:
        return self._partidas
    
    def __mapear_cepas(self) -> List[str]:
        return [cepa.obtener_nombre() for cepa in self.obtener_cepas()]
    
    def convertir_a_json(self) -> dict:
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "bodega": self.obtener_bodega().obtener_nombre(),
            "cepas": self.__mapear_cepas(),
            "partidas": self._partidas,
        }
    
    def convertir_a_json_full(self) -> dict:
        return self.convertir_a_json()
    
    def __repr__(self) -> str:
        return json.dumps({"nombre": self.obtener_nombre()})
