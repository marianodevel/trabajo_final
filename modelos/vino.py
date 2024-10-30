import json


class Vino:
    """Clase que representa un vino."""

    def __repr__(self):
        """Retorna una representación en string del objeto."""
        return json.dumps({"nombre": self.obtener_nombre()})

    def convertir_a_json(self):
        """Convierte el objeto a un diccionario JSON básico."""
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "bodega": self.obtener_bodega().obtener_nombre(),
            "cepas": self.__mapear_cepas(),
            "partidas": self.__partidas,
        }

    def convertir_a_json_full(self):
        """Convierte el objeto a un diccionario JSON completo."""
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "bodega": self.obtener_bodega().obtener_nombre(),
            "cepas": self.__mapear_cepas(),
            "partidas": self.__partidas,
        }

    def __mapear_cepas(self):
        """Mapea las cepas a una lista de nombres."""
        cepas = self.obtener_cepas()
        cepas_mapa = map(lambda a: a.obtener_nombre(), cepas)
        return list(cepas_mapa)
