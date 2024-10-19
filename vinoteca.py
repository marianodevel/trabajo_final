import json
from typing import List, Dict, Optional

from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class Vinoteca:
    # Atributos de clase
    __archivo_de_datos = "vinoteca.json"
    __bodegas: List[Bodega] = []
    __cepas: List[Cepa] = []
    __vinos: List[Vino] = []

    @classmethod
    def inicializar(cls) -> None:
        """Inicializa las colecciones de la Vinoteca desde el archivo JSON."""
        datos = cls.__parsear_archivo_de_datos()
        cls.__convertir_json_a_listas(datos)

    @classmethod
    def obtener_bodegas(
        cls,
        orden: Optional[str] = None,
        reverso: bool = False
    ) -> List[Bodega]:
        """
        Obtiene la lista de bodegas, opcionalmente ordenada.
        
        Args:
            orden: Criterio de ordenamiento ('nombre' o 'vinos')
            reverso: True para orden descendente, False para ascendente
            
        Returns:
            Lista de bodegas ordenada según los criterios especificados
        """
        if orden is None:
            return cls.__bodegas
        
        if orden == "nombre":
            return sorted(
                cls.__bodegas,
                key=lambda x: x.obtener_nombre(),
                reverse=reverso
            )
        elif orden == "vinos":
            return sorted(
                cls.__bodegas,
                key=lambda x: len(x.obtener_vinos()),
                reverse=reverso
            )
        return cls.__bodegas

    @classmethod
    def obtener_cepas(
        cls,
        orden: Optional[str] = None,
        reverso: bool = False
    ) -> List[Cepa]:
        """
        Obtiene la lista de cepas, opcionalmente ordenada.
        
        Args:
            orden: Criterio de ordenamiento ('nombre')
            reverso: True para orden descendente, False para ascendente
            
        Returns:
            Lista de cepas ordenada según los criterios especificados
        """
        if orden is None:
            return cls.__cepas
        
        if orden == "nombre":
            return sorted(
                cls.__cepas,
                key=lambda x: x.obtener_nombre(),
                reverse=reverso
            )
        return cls.__cepas

    @classmethod
    def obtener_vinos(
        cls,
        anio: Optional[int] = None,
        orden: Optional[str] = None,
        reverso: bool = False
    ) -> List[Vino]:
        """
        Obtiene la lista de vinos, opcionalmente filtrada por año y ordenada.
        
        Args:
            anio: Año para filtrar las partidas
            orden: Criterio de ordenamiento ('nombre', 'bodega' o 'cepas')
            reverso: True para orden descendente, False para ascendente
            
        Returns:
            Lista de vinos filtrada y ordenada según los criterios especificados
        """
        vinos = cls.__vinos
        
        if anio is not None:
            vinos = [vino for vino in vinos if anio in vino.obtener_partidas()]
        
        if orden is None:
            return vinos
        
        if orden == "nombre":
            return sorted(
                vinos,
                key=lambda x: x.obtener_nombre(),
                reverse=reverso
            )
        elif orden == "bodega":
            return sorted(
                vinos,
                key=lambda x: x.obtener_bodega().obtener_nombre(),
                reverse=reverso
            )
        elif orden == "cepas":
            return sorted(
                vinos,
                key=lambda x: len(x.obtener_cepas()),
                reverse=reverso
            )
        return vinos

    @classmethod
    def buscar_bodega(cls, id: str) -> Optional[Bodega]:
        """
        Busca una bodega por su ID.
        
        Args:
            id: ID de la bodega a buscar
            
        Returns:
            Bodega encontrada o None si no existe
        """
        for bodega in cls.__bodegas:
            if bodega.obtener_id() == id:
                return bodega
        return None

    @classmethod
    def buscar_cepa(cls, id: str) -> Optional[Cepa]:
        """
        Busca una cepa por su ID.
        
        Args:
            id: ID de la cepa a buscar
            
        Returns:
            Cepa encontrada o None si no existe
        """
        for cepa in cls.__cepas:
            if cepa.obtener_id() == id:
                return cepa
        return None

    @classmethod
    def buscar_vino(cls, id: str) -> Optional[Vino]:
        """
        Busca un vino por su ID.
        
        Args:
            id: ID del vino a buscar
            
        Returns:
            Vino encontrado o None si no existe
        """
        for vino in cls.__vinos:
            if vino.obtener_id() == id:
                return vino
        return None

    @classmethod
    def __parsear_archivo_de_datos(cls) -> Dict:
        """
        Lee y parsea el archivo JSON de datos.
        
        Returns:
            Diccionario con los datos del archivo
        """
        try:
            with open(cls.__archivo_de_datos, 'r', encoding='utf-8') as archivo:
                return json.load(archivo)
        except Exception as e:
            print(f"Error al leer el archivo de datos: {e}")
            return {"bodegas": [], "cepas": [], "vinos": []}

    @classmethod
    def __convertir_json_a_listas(cls, datos: Dict) -> None:
        """
        Convierte los datos JSON a objetos y los almacena en las listas.
        
        Args:
            datos: Diccionario con los datos a convertir
        """
        cls.__bodegas = [
            Bodega(bodega["id"], bodega["nombre"])
            for bodega in datos.get("bodegas", [])
        ]
        
        cls.__cepas = [
            Cepa(cepa["id"], cepa["nombre"])
            for cepa in datos.get("cepas", [])
        ]
        
        cls.__vinos = [
            Vino(
                vino["id"],
                vino["nombre"],
                vino["bodega"],
                vino["cepas"],
                vino["partidas"]
            )
            for vino in datos.get("vinos", [])
        ]
