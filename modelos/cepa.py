class Cepa(EntidadVineria):
    def __init__(self, id_: str, nombre: str) -> None:
        super().__init__(id_, nombre)

    def obtener_vinos(self) -> List['Vino']:
        from vinoteca import Vinoteca
        todos_vinos = Vinoteca.obtener_vinos()
        return [
            vino for vino in todos_vinos
            if self.obtener_id() in [cepa.obtener_id() for cepa in vino.obtener_cepa()]
        ]

    def convertir_a_json(self) -> Dict:
        return {
            "id": self.obtener_id(),
            "nombre": self.obtener_nombre(),
            "vinos": len(self.obtener_vinos()),
        }

    def __mapear_vinos(self) -> List[str]:
        vinos = self.obtener_vinos()
        vinos_mapa = map(
            lambda a: f"{a.obtener_nombre()} ({a.obtener_bodega().obtener_nombre()})",
            vinos,
        )
        return list(vinos_mapa)
