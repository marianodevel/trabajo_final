from typing import List, Optional, Dict, TYPE_CHECKING

class Vinoteca:
    __archivoDeDatos: str = "vinoteca.json"
    __bodegas: List['Bodega'] = []
    __cepas: List['Cepa'] = []
    __vinos: List['Vino'] = []

    @classmethod
    def obtener_archivo_datos(cls) -> str:
        return cls.__archivoDeDatos

    @classmethod
    def obtener_bodegas(cls, orden: Optional[str] = None, reverso: bool = False) -> List['Bodega']:
        if orden is not None:
            return sorted(
                cls.__bodegas[:],
                key=lambda x: getattr(x, orden),
                reverse=reverso
            )
        return cls.__bodegas

    @classmethod
    def obtener_cepas(cls, orden: Optional[str] = None, reverso: bool = False) -> List['Cepa']:
        if orden is not None:
            return sorted(
                cls.__cepas[:],
                key=lambda x: getattr(x, orden),
                reverse=reverso
            )
        return cls.__cepas

    @classmethod
    def obtener_vinos(cls, anio: Optional[int] = None, orden: Optional[str] = None, reverso: bool = False) -> List['Vino']:
        vinos_filtrados = cls.__vinos
        if anio is not None:
            vinos_filtrados = [
                vino for vino in cls.__vinos
                if anio in vino.obtener_partidas()
            ]
        
        if orden is not None:
            return sorted(
                vinos_filtrados[:],
                key=lambda x: getattr(x, orden),
                reverse=reverso
            )
        return vinos_filtrados

    @classmethod
    def __parsearArchivoDeDatos(cls) -> Dict:
        with open(cls.__archivoDeDatos, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        return datos

    @classmethod
    def __convertirJsonAListas(cls, listas: Dict) -> None:
        from modelos.bodega import Bodega
        from modelos.cepa import Cepa
        from modelos.vino import Vino
        
        cls.__bodegas.clear()
        cls.__cepas.clear()
        cls.__vinos.clear()

        for bodega_data in listas.get('bodegas', []):
            cls.__bodegas.append(Bodega(
                bodega_data['id'],
                bodega_data['nombre']
            ))

        for cepa_data in listas.get('cepas', []):
            cls.__cepas.append(Cepa(
                cepa_data['id'],
                cepa_data['nombre']
            ))

        for vino_data in listas.get('vinos', []):
            cls.__vinos.append(Vino(
                vino_data['id'],
                vino_data['nombre'],
                vino_data['bodega'],
                vino_data['cepas'],
                vino_data['partidas']
            ))
