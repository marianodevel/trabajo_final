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
    <link rel="stylesheet" href="{{ url_for('static', filename='styles.css') }}">
</head>
<body>
    <h1>Documentación API de Vinoteca</h1>
    
    <div class="menu">
        <div class="route-section">
            <h2>Bodegas</h2>
            <div class="route-item">
                <span class="route-method">GET</span>
                <span class="route-path">/api/bodegas</span>
                <div class="description">
                    Obtiene lista de todas las bodegas.
                    <br>
                    Parámetros opcionales:
                    <ul>
                        <li>orden: Campo por el cual ordenar (nombre, id)</li>
                        <li>reverso: "si" para orden descendente</li>
                    </ul>
                </div>
            </div>
            <div class="route-item">
                <span class="route-method">GET</span>
                <span class="route-path">/api/bodegas/&lt;id_&gt;</span>
                <div class="description">Obtiene detalles de una bodega específica por ID</div>
            </div>
        </div>

        <div class="route-section">
            <h2>Cepas</h2>
            <div class="route-item">
                <span class="route-method">GET</span>
                <span class="route-path">/api/cepas</span>
                <div class="description">
                    Obtiene lista de todas las cepas.
                    <br>
                    Parámetros opcionales:
                    <ul>
                        <li>orden: Campo por el cual ordenar (nombre, id)</li>
                        <li>reverso: "si" para orden descendente</li>
                    </ul>
                </div>
            </div>
            <div class="route-item">
                <span class="route-method">GET</span>
                <span class="route-path">/api/cepas/&lt;id_&gt;</span>
                <div class="description">Obtiene detalles de una cepa específica por ID</div>
            </div>
        </div>

        <div class="route-section">
            <h2>Vinos</h2>
            <div class="route-item">
                <span class="route-method">GET</span>
                <span class="route-path">/api/vinos</span>
                <div class="description">
                    Obtiene lista de todos los vinos.
                    <br>
                    Parámetros opcionales:
                    <ul>
                        <li>anio: Filtrar por año</li>
                        <li>orden: Campo por el cual ordenar (nombre, id, bodega, anio)</li>
                        <li>reverso: "si" para orden descendente</li>
                    </ul>
                </div>
            </div>
            <div class="route-item">
                <span class="route-method">GET</span>
                <span class="route-path">/api/vinos/&lt;id_&gt;</span>
                <div class="description">Obtiene detalles de un vino específico por ID</div>
            </div>
        </div>
    </div>
</body>
</html>
"""

def create_app() -> Flask:
    """
    Crea y configura la aplicación Flask.
    
    Returns:
        Flask: Instancia configurada de la aplicación Flask
    """
    app = Flask(__name__)
    api = Api(app)

    @app.route('/')
    def home():
        """Renderiza la página principal con la documentación de la API."""
        return render_template_string(TEMPLATE_HTML)

    # Registrar recursos de la API
    api.add_resource(RecursoBodega, '/api/bodegas/<id>')
    api.add_resource(RecursoBodegas, '/api/bodegas')
    api.add_resource(RecursoCepa, '/api/cepas/<id>')
    api.add_resource(RecursoCepas, '/api/cepas')
    api.add_resource(RecursoVino, '/api/vinos/<id>')
    api.add_resource(RecursoVinos, '/api/vinos')

    return app

if __name__ == "__main__":
    Vinoteca.inicializar()
    app = create_app()
    app.run(debug=True)
