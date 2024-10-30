import json


class Bodega:
    """Clase que representa una bodega de vinos."""

    def __repr__(self):
        """Retorna una representación en string del objeto."""
        return json.dumps(self.convertir_a_json())

    def convertir_a_json(self):
        """Convierte el objeto a un diccionario JSON básico."""
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "cepas": self.__mapear_cepas(),
            "vinos": len(self.obtener_vinos()),
        }

    def convertir_a_json_full(self):
        """Convierte el objeto a un diccionario JSON completo."""
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "cepas": self.__mapear_cepas(),
            "vinos": self.__mapear_vinos(),
        }

    def __mapear_cepas(self):
        """Mapea las cepas a una lista de nombres."""
        cepas = self.obtener_cepas()
        cepas_mapa = map(lambda a: a.obtener_nombre(), cepas)
        return list(cepas_mapa)

    def __mapear_vinos(self):
        """Mapea los vinos a una lista de nombres."""
        vinos = self.obtener_vinos()
        vinos_mapa = map(lambda a: a.obtener_nombre(), vinos)
        return list(vinos_mapa)
