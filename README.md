# Reqres API Automation

## Descripción
Este proyecto está diseñado para automatizar las pruebas de la API de Reqres utilizando **Python**, **pytest**, **requests** y **Allure**. Las pruebas incluyen la validación de los endpoints de la API de Reqres, y se pueden ejecutar localmente o en un entorno de integración continua (CI) como GitHub Actions.

## Requisitos Previos

Antes de comenzar, asegúrate de tener las siguientes herramientas instaladas:

- Python 3.13.0 o superior
- pip (gestor de paquetes de Python)
- virtualenv (para gestionar entornos virtuales)
- Git (para clonar y gestionar el repositorio)

## Configuración del Proyecto

### 1. Clonar el Repositorio
Clona el repositorio utilizando el siguiente comando:

```bash
git clone <url-del-repositorio>
cd reqres-api-automation
2. Crear el Entorno Virtual
Crea y activa un entorno virtual para el proyecto:

bash
Copy
Edit
python -m venv venv
source venv/Scripts/activate  # En Windows
3. Instalar las Dependencias
Instala las dependencias del proyecto, que están listadas en requirements.txt:

bash
Copy
Edit
pip install -r requirements.txt
playwright install  # Si usas Playwright, asegúrate de instalar los navegadores
Ejecutar Pruebas
Pruebas con Pytest
Para ejecutar las pruebas con pytest, usa el siguiente comando:

bash
Copy
Edit
pytest -v src/tests/test_usuarios.py
Pruebas con Allure
Para generar un reporte con Allure, ejecuta:

bash
Copy
Edit
pytest --alluredir=allure-results
allure serve allure-results
Esto generará un reporte interactivo que podrás ver en tu navegador.

Estructura del Proyecto
plaintext
Copy
Edit
reqres-api-automation/
├── .github/
│   └── workflows/
│       └── python-tests.yml          # Configuración de CI con GitHub Actions
├── src/
│   ├── api/
│   │   └── base_api.py              # Lógica base para interactuar con la API
│   ├── config/
│   │   └── config.py                # Configuraciones globales (e.g. URL base, API keys)
│   └── tests/
│       └── test_usuarios.py         # Casos de prueba para la API de usuarios
├── .gitignore                       # Archivos y carpetas que no se deben versionar
├── requirements.txt                 # Dependencias de Python del proyecto
├── pytest.ini                       # Configuración de pytest
└── README.md                        # Este archivo
Integración Continua
Este proyecto está configurado con GitHub Actions para:

Ejecutar las pruebas automáticamente en cada push o pull request.
Generar reportes Allure con los resultados de las pruebas.
Publicar los resultados en GitHub Pages para visualización.
Tecnologías
Python: Lenguaje de programación principal.
Pytest: Framework de pruebas utilizado.
Requests: Librería para hacer solicitudes HTTP a la API.
Allure: Herramienta para la generación de reportes visuales de las pruebas.
Playwright: Usado para pruebas de interfaz si es necesario (para pruebas de API se puede omitir).
GitHub Actions: Plataforma de integración continua utilizada para ejecutar las pruebas.
Guía Rápida de Comandos Git
bash
Copy
Edit
# Inicializar un repositorio Git
git init

# Añadir cambios al staging area
git add .

# Hacer commit de los cambios
git commit -m "Mensaje descriptivo"

# Subir los cambios al repositorio remoto
git push origin main
Contribución
Si deseas contribuir a este proyecto, sigue estos pasos:

Haz un fork del repositorio.
Crea una rama para tu feature o corrección.
Realiza tus cambios y haz commit de ellos.
Abre un Pull Request hacia la rama principal (main).
Autor
Elyer Gregorio Maldonado