import json
from typing import List, TYPE_CHECKING
from .entidad_vineria import EntidadVineria

class Bodega(EntidadVineria):
    def __init__(self, id: str, nombre: str) -> None:
        super().__init__(id, nombre)

    def obtener_vinos(self) -> List['Vino']:
        from vinoteca import Vinoteca
        todos_vinos = Vinoteca.obtener_vinos()
        return [
            vino for vino in todos_vinos
            if vino.obtener_bodega().obtener_id() == self.obtener_id()
        ]

    def obtener_cepas(self) -> List['Cepa']:
        vinos = self.obtener_vinos()
        todas_cepas = [cepa for vino in vinos for cepa in vino.obtener_cepa()]
        
        cepas_por_id = {}
        for cepa in todas_cepas:
            cepas_por_id[cepa.obtener_id()] = cepa
        
        return list(cepas_por_id.values())

    def __mapear_cepas(self) -> List[str]:
        cepas = self.obtener_cepas()
        cepas_mapa = map(lambda a: a.obtener_nombre(), cepas)
        return list(cepas_mapa)

    def __mapear_vinos(self) -> List[str]:
        vinos = self.obtener_vinos()
        vinos_mapa = map(lambda a: a.obtener_nombre(), vinos)
        return list(vinos_mapa)
