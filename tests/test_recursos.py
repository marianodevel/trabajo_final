import unittest
from unittest.mock import patch
import json
from flask import Flask
from flask.testing import FlaskClient

# Importaciones locales
from recursos import (
    RecursoBodega, RecursoBodegas,
    RecursoCepa, RecursoCepas,
    RecursoVino, RecursoVinos
)
from vinoteca import Vinoteca
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino

class TestRecursosBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Configuración inicial que se ejecuta una vez para toda la clase"""
        # Crear la aplicación Flask de prueba
        cls.app = Flask(__name__)
        cls.app.config['TESTING'] = True
        cls.client = cls.app.test_client()
        
        # Datos de prueba
        cls.datos_prueba = {
            "bodegas": [
                {"id": "b1", "nombre": "Bodega Test 1"},
                {"id": "b2", "nombre": "Bodega Test 2"}
            ],
            "cepas": [
                {"id": "c1", "nombre": "Cepa Test 1"},
                {"id": "c2", "nombre": "Cepa Test 2"}
            ],
            "vinos": [
                {
                    "id": "v1",
                    "nombre": "Vino Test 1",
                    "bodega": "b1",
                    "cepas": ["c1"],
                    "partidas": [2020, 2021]
                },
                {
                    "id": "v2",
                    "nombre": "Vino Test 2",
                    "bodega": "b2",
                    "cepas": ["c1", "c2"],
                    "partidas": [2021, 2022]
                }
            ]
        }

    def setUp(self):
        """Configuración que se ejecuta antes de cada test"""
        # Mock del archivo JSON y inicialización de Vinoteca
        with patch('builtins.open', create=True) as mock_file:
            mock_file.return_value.__enter__.return_value.read.return_value = \
                json.dumps(self.datos_prueba)
            Vinoteca.inicializar()


class TestRecursoBodega(TestRecursosBase):
    def setUp(self):
        """Configuración específica para tests de RecursoBodega"""
        super().setUp()
        self.recurso = RecursoBodega()

    def test_get_bodega_existente(self):
        """Prueba obtener una bodega que existe"""
        response, status = self.recurso.get("b1")
        self.assertEqual(status, 200)
        self.assertEqual(response["nombre"], "Bodega Test 1")
        self.assertIn("vinos", response)
        self.assertIn("cepas", response)

    def test_get_bodega_inexistente(self):
        """Prueba obtener una bodega que no existe"""
        response, status = self.recurso.get("inexistente")
        self.assertEqual(status, 404)
        self.assertIn("error", response)


class TestRecursoBodegas(TestRecursosBase):
    def setUp(self):
        """Configuración específica para tests de RecursoBodegas"""
        super().setUp()
        self.recurso = RecursoBodegas()

    def test_get_todas_bodegas(self):
        """Prueba obtener todas las bodegas sin filtros"""
        with self.app.test_request_context():
            response, status = self.recurso.get()
            self.assertEqual(status, 200)
            self.assertEqual(len(response), 2)

    def test_get_bodegas_ordenadas(self):
        """Prueba obtener bodegas con ordenamiento"""
        with self.app.test_request_context('/?orden=nombre&reverso=si'):
            response, status = self.recurso.get()
            self.assertEqual(status, 200)
            self.assertEqual(response[0]["nombre"], "Bodega Test 2")


class TestRecursoCepa(TestRecursosBase):
    def setUp(self):
        """Configuración específica para tests de RecursoCepa"""
        super().setUp()
        self.recurso = RecursoCepa()

    def test_get_cepa_existente(self):
        """Prueba obtener una cepa que existe"""
        response, status = self.recurso.get("c1")
        self.assertEqual(status, 200)
        self.assertEqual(response["nombre"], "Cepa Test 1")
        self.assertIn("vinos", response)

    def test_get_cepa_inexistente(self):
        """Prueba obtener una cepa que no existe"""
        response, status = self.recurso.get("inexistente")
        self.assertEqual(status, 404)
        self.assertIn("error", response)


class TestRecursoCepas(TestRecursosBase):
    def setUp(self):
        """Configuración específica para tests de RecursoCepas"""
        super().setUp()
        self.recurso = RecursoCepas()

    def test_get_todas_cepas(self):
        """Prueba obtener todas las cepas sin filtros"""
        with self.app.test_request_context():
            response, status = self.recurso.get()
            self.assertEqual(status, 200)
            self.assertEqual(len(response), 2)

    def test_get_cepas_ordenadas(self):
        """Prueba obtener cepas con ordenamiento"""
        with self.app.test_request_context('/?orden=nombre&reverso=si'):
            response, status = self.recurso.get()
            self.assertEqual(status, 200)
            self.assertEqual(response[0]["nombre"], "Cepa Test 2")


class TestRecursoVino(TestRecursosBase):
    def setUp(self):
        """Configuración específica para tests de RecursoVino"""
        super().setUp()
        self.recurso = RecursoVino()

    def test_get_vino_existente(self):
        """Prueba obtener un vino que existe"""
        response, status = self.recurso.get("v1")
        self.assertEqual(status, 200)
        self.assertEqual(response["nombre"], "Vino Test 1")
        self.assertIn("bodega", response)
        self.assertIn("cepas", response)
        self.assertIn("partidas", response)

    def test_get_vino_inexistente(self):
        """Prueba obtener un vino que no existe"""
        response, status = self.recurso.get("inexistente")
        self.assertEqual(status, 404)
        self.assertIn("error", response)


class TestRecursoVinos(TestRecursosBase):
    def setUp(self):
        """Configuración específica para tests de RecursoVinos"""
        super().setUp()
        self.recurso = RecursoVinos()

    def test_get_todos_vinos(self):
        """Prueba obtener todos los vinos sin filtros"""
        with self.app.test_request_context():
            response, status = self.recurso.get()
            self.assertEqual(status, 200)
            self.assertEqual(len(response), 2)

    def test_get_vinos_por_anio(self):
        """Prueba obtener vinos filtrados por año"""
        with self.app.test_request_context('/?anio=2020'):
            response, status = self.recurso.get()
            self.assertEqual(status, 200)
            self.assertEqual(len(response), 1)
            self.assertEqual(response[0]["nombre"], "Vino Test 1")

    def test_get_vinos_ordenados(self):
        """Prueba obtener vinos con diferentes ordenamientos"""
        # Por nombre
        with self.app.test_request_context('/?orden=nombre'):
            response, status = self.recurso.get()
            self.assertEqual(status, 200)
            self.assertEqual(response[0]["nombre"], "Vino Test 1")
        
        # Por bodega
        with self.app.test_request_context('/?orden=bodega'):
            response, status = self.recurso.get()
            self.assertEqual(status, 200)
            self.assertEqual(response[0]["bodega"], "Bodega Test 1")


if __name__ == '__main__':
    unittest.main()
