import json
from typing import List
from .entidad_vineria import EntidadVineria

class Cepa(EntidadVineria):
    def obtener_vinos(self) -> List['Vino']:
        from .vinoteca import Vinoteca
        return [vino for vino in Vinoteca.obtener_vinos() 
                if any(cepa.obtener_id() == self.obtener_id() 
                      for cepa in vino.obtener_cepas())]
    
    def __mapear_vinos(self) -> List[str]:
        vinos = self.obtener_vinos()
        return [f"{vino.obtener_nombre()} ({vino.obtener_bodega().obtener_nombre()})"
                for vino in vinos]
    
    def convertir_a_json(self) -> dict:
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "vinos": len(self.obtener_vinos()),
        }
    
    def convertir_a_json_full(self) -> dict:
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "vinos": self.__mapear_vinos(),
        }
    
    def __repr__(self) -> str:
        return json.dumps({"nombre": self.obtener_nombre()})
