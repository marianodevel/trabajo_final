import json


class Cepa:
    """Clase que representa una cepa de vino."""

    def __repr__(self):
        """Retorna una representación en string del objeto."""
        return json.dumps({"nombre": self.obtener_nombre()})

    def convertir_a_json(self):
        """Convierte el objeto a un diccionario JSON básico."""
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "vinos": len(self.obtener_vinos()),
        }

    def convertir_a_json_full(self):
        """Convierte el objeto a un diccionario JSON completo."""
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "vinos": self.__mapear_vinos(),
        }

    def __mapear_vinos(self):
        """Mapea los vinos a una lista de nombres con su bodega."""
        vinos = self.obtener_vinos()
        vinos_mapa = map(
            lambda a: f"{a.obtener_nombre()} ({a.obtener_bodega().obtener_nombre()})",
            vinos,
        )
        return list(vinos_mapa)
