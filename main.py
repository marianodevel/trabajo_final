from flask import Flask
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


if __name__ == "__main__":
    # Inicializar la vinoteca
    Vinoteca.inicializar()
    
    # Configurar Flask y la API
    app = Flask(__name__)
    api = Api(app)
    
    # Registrar recursos
    api.add_resource(RecursoBodega, '/api/bodegas/<id>')
    api.add_resource(RecursoBodegas, '/api/bodegas')
    api.add_resource(RecursoCepa, '/api/cepas/<id>')
    api.add_resource(RecursoCepas, '/api/cepas')
    api.add_resource(RecursoVino, '/api/vinos/<id>')
    api.add_resource(RecursoVinos, '/api/vinos')
    
    print("🍷 Servidor de Vinoteca iniciado - Accede a http://localhost:5000")
    app.run(debug=True)
