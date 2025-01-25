Reqres API Automation
Descripción
Proyecto de automatización de pruebas para la API de Reqres utilizando Python, pytest, requests y allure.
Requisitos Previos

Python 3.13.0
pip
virtualenv
Git

Configuración del Proyecto
1. Clonar Repositorio
bashCopygit clone <url-del-repositorio>
cd reqres-api-automation
2. Crear Entorno Virtual
bashCopypython -m venv venv
source venv/Scripts/activate  # En Windows
3. Instalar Dependencias
bashCopypip install -r requirements.txt
playwright install
Ejecutar Pruebas
Pruebas con Pytest
bashCopypytest -v src/tests/test_usuarios.py
Pruebas con Allure
bashCopypytest --alluredir=allure-results
allure serve allure-results
Estructura del Proyecto
Copyreqres-api-automation/
├── .github/
│   └── workflows/
│       └── python-tests.yml
├── src/
│   ├── api/
│   │   └── base_api.py
│   ├── config/
│   │   └── config.py
│   └── tests/
│       └── test_usuarios.py
├── .gitignore
├── requirements.txt
├── pytest.ini
└── README.md
Integración Continua
Configurado con GitHub Actions para:

Ejecutar pruebas en cada push/pull request
Generar reportes Allure
Publicar resultados en GitHub Pages

Tecnologías

Python
Pytest
Requests
Allure
Playwright
GitHub Actions

Guía Rápida de Comandos Git
bashCopy# Inicializar repositorio
git init

# Añadir cambios
git add .

# Hacer commit
git commit -m "Mensaje descriptivo"

# Subir a repositorio remoto
git push origin main
Contribución

Hacer fork del repositorio
Crear rama de feature
Hacer commit de cambios
Crear Pull Request

Autor
[Elyer Gregorio Maldonado]