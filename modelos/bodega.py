import json
from typing import List
from .entidad_vineria import EntidadVineria

class Bodega(EntidadVineria):
    def obtener_vinos(self) -> List['Vino']:
        from .vino import Vino
        from .vinoteca import Vinoteca
        return [vino for vino in Vinoteca.obtener_vinos() 
                if vino.obtener_bodega().obtener_id() == self.obtener_id()]
    
    def obtener_cepas(self) -> List['Cepa']:
        vinos = self.obtener_vinos()
        cepas_unicas = set()
        for vino in vinos:
            for cepa in vino.obtener_cepas():
                cepas_unicas.add(cepa)
        return list(cepas_unicas)
    
    def __mapear_cepas(self) -> List[str]:
        cepas = self.obtener_cepas()
        return [cepa.obtener_nombre() for cepa in cepas]
    
    def __mapear_vinos(self) -> List[str]:
        vinos = self.obtener_vinos()
        return [vino.obtener_nombre() for vino in vinos]
    
    def convertir_a_json(self) -> dict:
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "cepas": self.__mapear_cepas(),
            "vinos": len(self.obtener_vinos()),
        }
    
    def convertir_a_json_full(self) -> dict:
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "cepas": self.__mapear_cepas(),
            "vinos": self.__mapear_vinos(),
        }
    
    def __repr__(self) -> str:
        return json.dumps(self.convertir_a_json())
