import unittest
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino
from modelos.entidad_vineria import EntidadVineria

class TestEntidadVineria(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada test"""
        self.entidad = EntidadVineria("test_id", "Test Nombre")

    def test_getters(self):
        """Prueba los métodos getter de EntidadVineria"""
        self.assertEqual(self.entidad.obtener_id(), "test_id")
        self.assertEqual(self.entidad.obtener_nombre(), "Test Nombre")

    def test_setter_nombre(self):
        """Prueba el método setter de nombre"""
        self.entidad.establecer_nombre("Nuevo Nombre")
        self.assertEqual(self.entidad.obtener_nombre(), "Nuevo Nombre")

    def test_equality(self):
        """Prueba la comparación de igualdad entre entidades"""
        entidad2 = EntidadVineria("test_id", "Otro Nombre")
        entidad3 = EntidadVineria("otro_id", "Test Nombre")
        
        self.assertEqual(self.entidad, entidad2)  # Mismo ID
        self.assertNotEqual(self.entidad, entidad3)  # Diferente ID
        self.assertNotEqual(self.entidad, "no_es_entidad")  # Diferente tipo


class TestBodega(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada test"""
        self.bodega = Bodega("bod1", "Bodega Test")
        
        # Creamos algunas cepas y vinos para las pruebas
        self.cepa1 = Cepa("cep1", "Malbec")
        self.cepa2 = Cepa("cep2", "Cabernet")
        
        self.vino1 = Vino("vin1", "Vino Test 1", "bod1", ["cep1"], [2020])
        self.vino2 = Vino("vin2", "Vino Test 2", "bod1", ["cep1", "cep2"], [2021])

    def test_conversion_json(self):
        """Prueba los métodos de conversión a JSON"""
        json_basico = self.bodega.convertir_a_json()
        self.assertEqual(json_basico["id"], "bod1")
        self.assertEqual(json_basico["nombre"], "Bodega Test")
        
        json_completo = self.bodega.convertir_a_json_full()
        self.assertIn("id", json_completo)
        self.assertIn("nombre", json_completo)
        self.assertIn("cepas", json_completo)
        self.assertIn("vinos", json_completo)


class TestCepa(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada test"""
        self.cepa = Cepa("cep1", "Cepa Test")
        
        # Creamos algunos vinos para las pruebas
        self.vino1 = Vino("vin1", "Vino Test 1", "bod1", ["cep1"], [2020])
        self.vino2 = Vino("vin2", "Vino Test 2", "bod1", ["cep1", "cep2"], [2021])

    def test_conversion_json(self):
        """Prueba los métodos de conversión a JSON"""
        json_basico = self.cepa.convertir_a_json()
        self.assertEqual(json_basico["id"], "cep1")
        self.assertEqual(json_basico["nombre"], "Cepa Test")
        
        json_completo = self.cepa.convertir_a_json_full()
        self.assertIn("id", json_completo)
        self.assertIn("nombre", json_completo)
        self.assertIn("vinos", json_completo)


class TestVino(unittest.TestCase):
    def setUp(self):
        """Configuración inicial para cada test"""
        self.vino = Vino(
            "vin1",
            "Vino Test",
            "bod1",
            ["cep1", "cep2"],
            [2020, 2021]
        )

    def test_getters(self):
        """Prueba los métodos getter específicos de Vino"""
        self.assertEqual(self.vino.obtener_partidas(), [2020, 2021])

    def test_setters(self):
        """Prueba los métodos setter específicos de Vino"""
        self.vino.establecer_bodega("bod2")
        self.vino.establecer_cepas(["cep3"])
        self.vino.establecer_partidas([2022])
        
        self.assertEqual(self.vino._bodega_id, "bod2")
        self.assertEqual(self.vino._cepa_ids, ["cep3"])
        self.assertEqual(self.vino._partidas, [2022])

    def test_conversion_json(self):
        """Prueba los métodos de conversión a JSON"""
        json_basico = self.vino.convertir_a_json()
        self.assertEqual(json_basico["id"], "vin1")
        self.assertEqual(json_basico["nombre"], "Vino Test")
        self.assertIn("partidas", json_basico)
        
        json_completo = self.vino.convertir_a_json_full()
        self.assertEqual(json_completo, json_basico)  # En este caso son iguales


if __name__ == '__main__':
    unittest.main()
