"""Módulo para definiciones de recursos de la API REST."""
import json

from flask import request
from flask_restful import Resource

import vinoteca
from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino


class RecursoBodega(Resource):
    """Recurso para manejar endpoints individuales de bodegas."""

    def get(self, id):
        """
        Obtiene una bodega específica por ID.

        Args:
            id (str): ID de la bodega

        Returns:
            tuple: Respuesta JSON y código de estado HTTP
        """
        bodega = vinoteca.Vinoteca.buscar_bodega(id)
        if isinstance(bodega, Bodega):
            return json.loads(json.dumps(bodega.convertir_a_json_full())), 200
        return {"error": "Bodega no encontrada"}, 404


class RecursoBodegas(Resource):
    """Recurso para manejar endpoints de colección de bodegas."""

    def get(self):
        """
        Obtiene lista de todas las bodegas con ordenamiento opcional.

        Returns:
            tuple: Respuesta JSON y código de estado HTTP
        """
        orden = request.args.get("orden")
        if orden:
            reverso = request.args.get("reverso")
            bodegas = vinoteca.Vinoteca.obtener_bodegas(
                orden=orden,
                reverso=reverso == "si"
            )
        else:
            bodegas = vinoteca.Vinoteca.obtener_bodegas()
        return (
            json.loads(
                json.dumps(bodegas, default=lambda o: o.convertir_a_json())
            ),
            200,
        )


class RecursoCepa(Resource):
    """Recurso para manejar endpoints individuales de cepas."""

    def get(self, id):
        """
        Obtiene una cepa específica por ID.

        Args:
            id (str): ID de la cepa

        Returns:
            tuple: Respuesta JSON y código de estado HTTP
        """
        cepa = vinoteca.Vinoteca.buscar_cepa(id)
        if isinstance(cepa, Cepa):
            return json.loads(json.dumps(cepa.convertir_a_json_full())), 200
        return {"error": "Cepa no encontrada"}, 404


class RecursoCepas(Resource):
    """Recurso para manejar endpoints de colección de cepas."""

    def get(self):
        """
        Obtiene lista de todas las cepas con ordenamiento opcional.

        Returns:
            tuple: Respuesta JSON y código de estado HTTP
        """
        orden = request.args.get("orden")
        if orden:
            reverso = request.args.get("reverso")
            cepas = vinoteca.Vinoteca.obtener_cepas(
                orden=orden,
                reverso=reverso == "si"
            )
        else:
            cepas = vinoteca.Vinoteca.obtener_cepas()
        return (
            json.loads(
                json.dumps(cepas, default=lambda o: o.convertir_a_json_full())
            ),
            200,
        )


class RecursoVino(Resource):
    """Recurso para manejar endpoints individuales de vinos."""

    def get(self, id):
        """
        Obtiene un vino específico por ID.

        Args:
            id (str): ID del vino

        Returns:
            tuple: Respuesta JSON y código de estado HTTP
        """
        vino = vinoteca.Vinoteca.buscar_vino(id)
        if isinstance(vino, Vino):
            return json.loads(json.dumps(vino.convertir_a_json_full())), 200
        return {"error": "Vino no encontrado"}, 404


class RecursoVinos(Resource):
    """Recurso para manejar endpoints de colección de vinos."""

    def get(self):
        """
        Obtiene lista de todos los vinos con filtrado y ordenamiento opcional.

        Returns:
            tuple: Respuesta JSON y código de estado HTTP
        """
        anio = request.args.get("anio")
        if anio:
            anio = int(anio)
        orden = request.args.get("orden")
        if orden:
            reverso = request.args.get("reverso")
            vinos = vinoteca.Vinoteca.obtener_vinos(
                anio,
                orden=orden,
                reverso=reverso == "si"
            )
        else:
            vinos = vinoteca.Vinoteca.obtener_vinos(anio)
        return (
            json.loads(
                json.dumps(vinos, default=lambda o: o.convertir_a_json())
            ),
            200,
        )
