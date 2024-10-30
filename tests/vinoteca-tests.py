import unittest
import json
from entidad_vineria import EntidadVineria
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino
from vinoteca import Vinoteca


class TestEntidadVineria(unittest.TestCase):
    """Pruebas para la clase base EntidadVineria."""

    def test_no_puede_instanciar_entidad_vineria_directamente(self):
        """Verifica que EntidadVineria no puede ser instanciada directamente."""
        with self.assertRaises(TypeError):
            EntidadVineria("1", "Test")

    def test_equals_compara_por_id(self):
        """Verifica que la comparación de entidades se hace por ID."""
        class EntidadConcreta(EntidadVineria):
            pass

        entidad1 = EntidadConcreta("1", "Test 1")
        entidad2 = EntidadConcreta("1", "Test 2")
        entidad3 = EntidadConcreta("2", "Test 1")

        self.assertEqual(entidad1, entidad2)
        self.assertNotEqual(entidad1, entidad3)


class TestBodega(unittest.TestCase):
    """Pruebas para la clase Bodega."""

    def setUp(self):
        """Inicializa el ambiente de pruebas."""
        Vinoteca.inicializar()
        # Usando una bodega real del JSON
        self.bodega = Vinoteca.buscar_bodega(
            "a0900e61-0f72-67ae-7e9d-4218da29b7d8"  # Casa La Primavera
        )

    def test_obtener_vinos_retorna_vinos_correctos(self):
        """Verifica que se obtienen los vinos correctos de la bodega."""
        vinos = self.bodega.obtener_vinos()
        # Debería tener 3 vinos: Profugo, Oveja Black y Sin Palabra
        self.assertEqual(len(vinos), 3)
        nombres_vinos = {vino.obtener_nombre() for vino in vinos}
        self.assertEqual(
            nombres_vinos,
            {"Profugo", "Oveja Black", "Sin Palabra"}
        )

    def test_obtener_cepas_sin_duplicados(self):
        """Verifica que se obtienen las cepas sin duplicados."""
        cepas = self.bodega.obtener_cepas()
        nombres_cepas = {cepa.obtener_nombre() for cepa in cepas}
        self.assertEqual(
            nombres_cepas,
            {"Chardonnay", "Malbec", "Cabernet Sauvignon", "Merlot"}
        )

    def test_convertir_a_json_formato_correcto(self):
        """Verifica que la conversión a JSON tiene el formato correcto."""
        json_data = self.bodega.convertir_a_json()
        self.assertEqual(
            json_data["id"],
            "a0900e61-0f72-67ae-7e9d-4218da29b7d8"
        )
        self.assertEqual(
            json_data["nombre"],
            "Casa La Primavera Bodegas y Viñedos"
        )


class TestCepa(unittest.TestCase):
    """Pruebas para la clase Cepa."""

    def setUp(self):
        """Inicializa el ambiente de pruebas."""
        Vinoteca.inicializar()
        # Usando una cepa real del JSON
        self.cepa = Vinoteca.buscar_cepa(
            "33ccaa9d-4710-9942-002d-1b5cb9912e5d"  # Chardonnay
        )

    def test_obtener_vinos_retorna_vinos_correctos(self):
        """Verifica que se obtienen los vinos correctos para la cepa."""
        vinos = self.cepa.obtener_vinos()
        # Verificar que todos los vinos retornados tienen esta cepa
        for vino in vinos:
            self.assertIn(
                self.cepa.obtener_id(),
                [cepa.obtener_id() for cepa in vino.obtener_cepas()]
            )

    def test_convertir_a_json_full_formato_correcto(self):
        """Verifica que la conversión a JSON completo tiene formato correcto."""
        json_data = self.cepa.convertir_a_json_full()
        self.assertEqual(
            json_data["id"],
            "33ccaa9d-4710-9942-002d-1b5cb9912e5d"
        )
        self.assertEqual(json_data["nombre"], "Chardonnay")
        self.assertTrue("vinos" in json_data)


class TestVino(unittest.TestCase):
    """Pruebas para la clase Vino."""

    def setUp(self):
        """Inicializa el ambiente de pruebas."""
        Vinoteca.inicializar()
        # Usando un vino real del JSON
        self.vino = Vinoteca.buscar_vino(
            "4823ad54-0a3a-38b8-adf6-795512994a4f"  # Abducido
        )

    def test_obtener_bodega_retorna_bodega_correcta(self):
        """Verifica que se obtiene la bodega correcta del vino."""
        bodega = self.vino.obtener_bodega()
        self.assertEqual(bodega.obtener_nombre(), "La Iride")

    def test_obtener_cepas_retorna_cepas_correctas(self):
        """Verifica que se obtienen las cepas correctas del vino."""
        cepas = self.vino.obtener_cepas()
        nombres_cepas = {cepa.obtener_nombre() for cepa in cepas}
        self.assertEqual(
            nombres_cepas,
            {"Cabernet Sauvignon", "Malbec"}
        )

    def test_obtener_partidas_correctas(self):
        """Verifica que se obtienen las partidas correctas del vino."""
        partidas = self.vino.obtener_partidas()
        self.assertEqual(set(partidas), {2024, 2023, 2022})


class TestVinoteca(unittest.TestCase):
    """Pruebas para la clase Vinoteca."""

    def setUp(self):
        """Inicializa el ambiente de pruebas."""
        Vinoteca.inicializar()

    def test_obtener_bodegas_sin_parametros_retorna_todas(self):
        """Verifica que se obtienen todas las bodegas sin filtros."""
        bodegas = Vinoteca.obtener_bodegas(None, None)
        self.assertEqual(len(bodegas), 7)  # El JSON tiene 7 bodegas

    def test_obtener_bodegas_ordenadas_por_nombre(self):
        """Verifica que las bodegas se ordenan correctamente por nombre."""
        bodegas = Vinoteca.obtener_bodegas("nombre", "no")
        nombres = [bodega.obtener_nombre() for bodega in bodegas]
        self.assertEqual(nombres, sorted(nombres))

    def test_obtener_vinos_por_anio_2020(self):
        """Verifica que se obtienen los vinos correctos por año."""
        vinos = Vinoteca.obtener_vinos(2020, None, None)
        self.assertEqual(len(vinos), 2)
        nombres_vinos = {vino.obtener_nombre() for vino in vinos}
        self.assertEqual(
            nombres_vinos,
            {"Sin Palabra", "Familia Gascon"}
        )

    def test_obtener_vinos_ordenados_por_nombre(self):
        """Verifica que los vinos se ordenan correctamente por nombre."""
        vinos = Vinoteca.obtener_vinos(None, "nombre", "no")
        nombres = [vino.obtener_nombre() for vino in vinos]
        self.assertEqual(nombres, sorted(nombres))

    def test_buscar_vino_existente(self):
        """Verifica que se encuentra un vino existente."""
        vino = Vinoteca.buscar_vino(
            "4823ad54-0a3a-38b8-adf6-795512994a4f"
        )
        self.assertIsNotNone(vino)
        self.assertEqual(vino.obtener_nombre(), "Abducido")

    def test_buscar_vino_inexistente(self):
        """Verifica que se maneja correctamente la búsqueda de vino inexistente."""
        vino = Vinoteca.buscar_vino("id_inexistente")
        self.assertIsNone(vino)


if __name__ == '__main__':
    unittest.main()
