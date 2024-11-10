import json
from typing import List, Optional, Dict, TYPE_CHECKING

if TYPE_CHECKING:
    from modelos.bodega import Bodega
    from modelos.cepa import Cepa
    from modelos.vino import Vino


class Vinoteca:
    """
    Clase que centraliza las consultas a la base de datos de la vinoteca.
    No posee atributos de instancia ya que su propósito es ser utilizada
    a nivel clase.
    """
    # Atributos de clase según el diagrama
    archivoDeDatos: str = "vinoteca.json"
    bodegas: List['Bodega'] = []
    cepas: List['Cepa'] = []
    vinos: List['Vino'] = []

    @classmethod
    def inicializar(cls) -> None:
        """
        Inicializa las colecciones de la vinoteca desde el archivo JSON.
        """
        datos = cls.__parsearArchivoDeDatos()
        cls.__convertirJsonAListas(datos)

    @classmethod
    def obtenerBodegas(
        cls,
        orden: Optional[str] = None,
        reverso: bool = False
    ) -> List['Bodega']:
        """
        Obtiene la lista de bodegas, opcionalmente ordenada.

        Args:
            orden: Atributo por el cual ordenar
            reverso: True para orden descendente, False para ascendente

        Returns:
            Lista de bodegas ordenada según los parámetros
        """
        if orden is not None:
            return sorted(
                cls.bodegas[:],  # Copia de la colección
                key=lambda x: getattr(x, orden),
                reverse=reverso
            )
        return cls.bodegas

    @classmethod
    def obtenerCepas(
        cls,
        orden: Optional[str] = None,
        reverso: bool = False
    ) -> List['Cepa']:
        """
        Obtiene la lista de cepas, opcionalmente ordenada.

        Args:
            orden: Atributo por el cual ordenar
            reverso: True para orden descendente, False para ascendente

        Returns:
            Lista de cepas ordenada según los parámetros
        """
        if orden is not None:
            return sorted(
                cls.cepas[:],  # Copia de la colección
                key=lambda x: getattr(x, orden),
                reverse=reverso
            )
        return cls.cepas

    @classmethod
    def obtenerVinos(
        cls,
        anio: Optional[int] = None,
        orden: Optional[str] = None,
        reverso: bool = False
    ) -> List['Vino']:
        """
        Obtiene la lista de vinos, opcionalmente filtrada por año y ordenada.

        Args:
            anio: Año de la partida para filtrar
            orden: Atributo por el cual ordenar
            reverso: True para orden descendente, False para ascendente

        Returns:
            Lista de vinos filtrada y ordenada según los parámetros
        """
        vinos_filtrados = cls.vinos
        if anio is not None:
            vinos_filtrados = [
                vino for vino in cls.vinos
                if anio in vino.obtener_partidas()
            ]
        
        if orden is not None:
            return sorted(
                vinos_filtrados[:],  # Copia de la colección
                key=lambda x: getattr(x, orden),
                reverse=reverso
            )
        return vinos_filtrados

    @classmethod
    def buscarBodega(cls, id: str) -> Optional['Bodega']:
        """
        Busca una bodega por su ID.

        Args:
            id: Identificador de la bodega

        Returns:
            Bodega encontrada o None si no existe
        """
        for bodega in cls.bodegas:
            if bodega.obtener_id() == id:
                return bodega
        return None

    @classmethod
    def buscarCepa(cls, id: str) -> Optional['Cepa']:
        """
        Busca una cepa por su ID.

        Args:
            id: Identificador de la cepa

        Returns:
            Cepa encontrada o None si no existe
        """
        for cepa in cls.cepas:
            if cepa.obtener_id() == id:
                return cepa
        return None

    @classmethod
    def buscarVino(cls, id: str) -> Optional['Vino']:
        """
        Busca un vino por su ID.

        Args:
            id: Identificador del vino

        Returns:
            Vino encontrado o None si no existe
        """
        for vino in cls.vinos:
            if vino.obtener_id() == id:
                return vino
        return None

    @classmethod
    def __parsearArchivoDeDatos(cls) -> Dict:
        """
        Lee y parsea el archivo JSON de datos.

        Returns:
            Diccionario con los datos del archivo JSON
        """
        with open(cls.archivoDeDatos, 'r', encoding='utf-8') as archivo:
            datos = json.load(archivo)
        return datos

    @classmethod
    def __convertirJsonAListas(cls, listas: Dict) -> None:
        """
        Convierte los datos JSON en objetos y los almacena en las listas
        correspondientes.

        Args:
            listas: Diccionario con los datos a convertir
        """
        # Importaciones dinámicas para evitar ciclos
        from modelos.bodega import Bodega
        from modelos.cepa import Cepa
        from modelos.vino import Vino
        
        # Limpiar las listas existentes
        cls.bodegas.clear()
        cls.cepas.clear()
        cls.vinos.clear()

        # Convertir datos JSON en objetos
        for bodega_data in listas.get('bodegas', []):
            cls.bodegas.append(Bodega(
                bodega_data['id'],
                bodega_data['nombre']
            ))

        for cepa_data in listas.get('cepas', []):
            cls.cepas.append(Cepa(
                cepa_data['id'],
                cepa_data['nombre']
            ))

        for vino_data in listas.get('vinos', []):
            cls.vinos.append(Vino(
                vino_data['id'],
                vino_data['nombre'],
                vino_data['bodega'],
                vino_data['cepas'],
                vino_data['partidas']
            ))
