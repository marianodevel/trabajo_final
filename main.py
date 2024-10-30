"""Módulo principal de la aplicación para la API de vinoteca."""
from flask import Flask, render_template_string
from flask_restful import Api

from vinoteca import Vinoteca
from recursos import (
    RecursoBodega,
    RecursoBodegas,
    RecursoCepa,
    RecursoCepas,
    RecursoVino,
    RecursoVinos
)

# Template HTML para la página principal
TEMPLATE_HTML = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Vinoteca API</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            line-height: 1.6;
        }
        h1 {
            color: #722F37;
            text-align: center;
            border-bottom: 2px solid #722F37;
            padding-bottom: 10px;
        }
        .menu {
            background-color: #f9f9f9;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }
        .menu h2 {
            color: #722F37;
            margin-top: 0;
        }
        .menu-item {
            margin-bottom: 15px;
            padding: 10px;
            background-color: white;
            border-radius: 3px;
        }
        a {
            color: #722F37;
            text-decoration: none;
        }
        a:hover {
            text-decoration: underline;
        }
        .descripcion {
            font-size: 0.9em;
            color: #666;
            margin-top: 5px;
        }
    </style>
</head>
<body>
    <h1>Bienvenido a la API de Vinoteca</h1>
    
    <div class="menu">
        <h2>Menú de Ejemplos</h2>
        
        <div class="menu-item">
            <a href="/api/bodegas/a0900e61-0f72-67ae-7e9d-4218da29b7d8">Ver Bodega Casa La Primavera</a>
            <div class="descripcion">Detalles de la bodega específica</div>
        </div>
        
        <div class="menu-item">
            <a href="/api/cepas/33ccaa9d-4710-9942-002d-1b5cb9912e5d">Ver Cepa Chardonnay</a>
            <div class="descripcion">Información detallada de la cepa</div>
        </div>
        
        <div class="menu-item">
            <a href="/api/vinos/4823ad54-0a3a-38b8-adf6-795512994a4f">Ver Vino Abducido</a>
            <div class="descripcion">Detalles completos del vino</div>
        </div>
        
        <div class="menu-item">
            <a href="/api/vinos?anio=2020&orden=nombre&reverso=no">Vinos del 2020 (orden alfabético)</a>
            <div class="descripcion">Lista de vinos del año 2020 ordenados por nombre</div>
        </div>
        
        <div class="menu-item">
            <a href="/api/vinos?anio=2020&orden=nombre&reverso=si">Vinos del 2020 (orden alfabético inverso)</a>
            <div class="descripcion">Lista de vinos del año 2020 ordenados por nombre en reverso</div>
        </div>
    </div>
</body>
</html>
"""

app = Flask(__name__)
api = Api(app)

@app.route('/')
def home():
    """Renderiza la página principal con el menú de navegación."""
    return render_template_string(TEMPLATE_HTML)

# Registrar recursos de la API
api.add_resource(RecursoBodega, '/api/bodegas/<id>')
api.add_resource(RecursoBodegas, '/api/bodegas')
api.add_resource(RecursoCepa, '/api/cepas/<id>')
api.add_resource(RecursoCepas, '/api/cepas')
api.add_resource(RecursoVino, '/api/vinos/<id>')
api.add_resource(RecursoVinos, '/api/vinos')

if __name__ == "__main__":
    Vinoteca.inicializar()
    app.run(debug=True)
