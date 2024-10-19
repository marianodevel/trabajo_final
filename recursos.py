from flask_restful import Resource
from flask import request
import json

from modelos.bodega import Bodega
from modelos.cepa import Cepa
from modelos.vino import Vino
from vinoteca import Vinoteca


class RecursoBodega(Resource):
    def get(self, id):
        bodega = Vinoteca.buscar_bodega(id)
        if isinstance(bodega, Bodega):
            return json.loads(json.dumps(bodega.convertir_a_json_full())), 200
        return {"error": "Bodega no encontrada"}, 404


class RecursoBodegas(Resource):
    def get(self):
        orden = request.args.get("orden")
        if orden:
            reverso = request.args.get("reverso")
            bodegas = Vinoteca.obtener_bodegas(
                orden=orden, 
                reverso=reverso == "si"
            )
        else:
            bodegas = Vinoteca.obtener_bodegas()
        
        return (
            json.loads(json.dumps(bodegas, default=lambda o: o.convertir_a_json())),
            200,
        )


class RecursoCepa(Resource):
    def get(self, id):
        cepa = Vinoteca.buscar_cepa(id)
        if isinstance(cepa, Cepa):
            return json.loads(json.dumps(cepa.convertir_a_json_full())), 200
        return {"error": "Cepa no encontrada"}, 404


class RecursoCepas(Resource):
    def get(self):
        orden = request.args.get("orden")
        if orden:
            reverso = request.args.get("reverso")
            cepas = Vinoteca.obtener_cepas(
                orden=orden,
                reverso=reverso == "si"
            )
        else:
            cepas = Vinoteca.obtener_cepas()
        
        return (
            json.loads(json.dumps(cepas, default=lambda o: o.convertir_a_json_full())),
            200,
        )


class RecursoVino(Resource):
    def get(self, id):
        vino = Vinoteca.buscar_vino(id)
        if isinstance(vino, Vino):
            return json.loads(json.dumps(vino.convertir_a_json_full())), 200
        return {"error": "Vino no encontrado"}, 404


class RecursoVinos(Resource):
    def get(self):
        anio = request.args.get("anio")
        if anio:
            anio = int(anio)
            
        orden = request.args.get("orden")
        if orden:
            reverso = request.args.get("reverso")
            vinos = Vinoteca.obtener_vinos(
                anio,
                orden=orden,
                reverso=reverso == "si"
            )
        else:
            vinos = Vinoteca.obtener_vinos(anio)
            
        return json.loads(json.dumps(vinos, default=lambda o: o.convertir_a_json())), 200
