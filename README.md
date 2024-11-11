# TRABAJO INTEGRADOR FINAL
## PROGRAMACIÓN 2 - 2024 – 2do cuatrimestre
## TECNICATURA UNIVERSITARIA EN DESARROLLO WEB

## Autores
- Ileana Nieto
- Laura Moyano
- Maximiliano Antonio Ortiz
- Mariano Bustos
- Juan Paulo Trentino

## Instrucciones de Instalación

### 1. Clonar el Repositorio

Para clonar el repositorio, necesitarás tener Git instalado en tu sistema. Luego ejecuta:

```bash
git clone https://github.com/marianodevel/trabajo_final.git
cd trabajo_final
```

### 2. Instalar Dependencias

El proyecto requiere Python 3.x y utiliza un archivo requirements.txt para gestionar las dependencias.

Primero, es recomendable crear un entorno virtual:

#### Windows:
```bash
# Crear entorno virtual
python -m venv venv

# Activar el entorno virtual
venv\Scripts\activate
```

#### macOS/Linux:
```bash
# Crear entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate
```

Una vez activado el entorno virtual, instalar las dependencias:

#### Windows:
```bash
pip install -r requirements.txt
```

#### macOS/Linux:
```bash
pip3 install -r requirements.txt
```

## Uso

Para ejecutar la aplicación:

#### Windows:
```bash
python main.py
```

#### macOS/Linux:
```bash
python3 main.py
```

La API estará disponible en `http://localhost:5000`

## Documentación

La API proporciona los siguientes endpoints:

### Vinos
- `GET /vinos`: Obtiene lista de todos los vinos
  - Parámetros opcionales:
    - `anio`: Filtra por año de la partida
    - `orden`: Ordena por el campo especificado
    - `reverso`: "si" para orden descendente
- `GET /vinos/<id>`: Obtiene un vino específico por ID

### Bodegas
- `GET /bodegas`: Obtiene lista de todas las bodegas
  - Parámetros opcionales:
    - `orden`: Ordena por el campo especificado
    - `reverso`: "si" para orden descendente
- `GET /bodegas/<id>`: Obtiene una bodega específica por ID

### Cepas
- `GET /cepas`: Obtiene lista de todas las cepas
  - Parámetros opcionales:
    - `orden`: Ordena por el campo especificado
    - `reverso`: "si" para orden descendente
- `GET /cepas/<id>`: Obtiene una cepa específica por ID

### Ejemplos de Uso

Para probar los endpoints, puedes usar curl (disponible en Windows 10+, macOS y Linux) o cualquier cliente HTTP como Postman:

```bash
# Obtener todos los vinos
curl http://localhost:5000/vinos

# Obtener vinos del año 2020
curl http://localhost:5000/vinos?anio=2020

# Obtener vinos ordenados por nombre
curl http://localhost:5000/vinos?orden=nombre

# Obtener bodegas ordenadas por nombre en orden descendente
curl http://localhost:5000/bodegas?orden=nombre&reverso=si
```

También puedes acceder a estos endpoints directamente desde tu navegador web visitando las URLs correspondientes.
