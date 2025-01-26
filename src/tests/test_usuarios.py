import pytest
import requests
import allure
import json
import time
from typing import Dict

@allure.epic("Reqres API Rest")
@allure.feature("Gestión de Usuarios")
class TestUsuarios:
    BASE_URL = "https://reqres.in/api"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Obtener Lista de Usuarios")
    @allure.title("TC1: (GET) VALIDAR LA OBTENCIÓN DE LA LISTA DE USUARIOS DE LA PÁGINA 2")
    def test_obtener_lista_usuarios(self):
        
        with allure.step("Preparar Solicitud GET"):
            endpoint = "/users"
            url = f"{self.BASE_URL}{endpoint}"
            params = {"page": 2}
            
            
            request_details = {
                "URL": url,
                "Método": "GET",
                "Parámetros": params
            }
            allure.attach(
                json.dumps(request_details, indent=2), 
                name="Detalles de Solicitud", 
                attachment_type=allure.attachment_type.JSON
            )

        
        with allure.step("Enviar Solicitud"):
            start_time = time.time()
            response = requests.get(url, params=params)
            response_time = time.time() - start_time

        
        with allure.step("Documentar Respuesta"):
            response_details = {
                "Código de Estado": response.status_code,
                "Tiempo de Respuesta (s)": round(response_time, 2),
                "Cabeceras": dict(response.headers)
            }
            
            
            allure.attach(
                json.dumps(response_details, indent=2), 
                name="Metadatos de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )
            
            
            allure.attach(
                json.dumps(response.json(), indent=2), 
                name="Contenido de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )

        # Validaciones
        with allure.step("Validar Respuesta"):
            # Validación de código de estado
            assert response.status_code == 200, "Solicitud de usuarios no exitosa"

            # Validación de estructura de datos
            data = response.json()
            assert "data" in data, "Estructura de respuesta incorrecta"
            
            usuarios = data["data"]
            assert len(usuarios) > 0, "Lista de usuarios vacía"
            
            # Validación de campos de usuarios
            campos_requeridos = ["id", "email", "first_name", "last_name"]
            for usuario in usuarios:
                for campo in campos_requeridos:
                    assert campo in usuario, f"Campo {campo} faltante en usuario"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Obtener Detalles de Usuario Unico")
    @allure.title("TC2: (GET) VALIDAR LA OBTENCIÓN DE USUARIO CON ID 2")
    def test_obtener_usuario_con_id_2(self):
        
        with allure.step("Preparar Solicitud GET"):
            endpoint = "/users/2"
            url = f"{self.BASE_URL}{endpoint}"
            params = {}
            
            
            request_details = {
                "URL": url,
                "Método": "GET",
                "Parámetros": params
            }
            allure.attach(
                json.dumps(request_details, indent=2), 
                name="Detalles de Solicitud", 
                attachment_type=allure.attachment_type.JSON
            )

    
        with allure.step("Enviar Solicitud"):
            start_time = time.time()
            response = requests.get(url, params=params)
            response_time = time.time() - start_time

        
        with allure.step("Documentar Respuesta"):
            response_details = {
                "Código de Estado": response.status_code,
                "Tiempo de Respuesta (s)": round(response_time, 2),
                "Cabeceras": dict(response.headers)
            }
            
            
            allure.attach(
                json.dumps(response_details, indent=2), 
                name="Metadatos de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )
            
            
            allure.attach(
                json.dumps(response.json(), indent=2), 
                name="Contenido de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )

        # Validaciones
        with allure.step("Validar Respuesta"):
            # Validación de código de estado
            assert response.status_code == 200, "Solicitud de usuarios no exitosa"

            # Validación de estructura de datos
            data = response.json()
            assert "data" in data, "Estructura de respuesta incorrecta"
            
            usuarios = data["data"]
            assert isinstance(usuarios, dict), "Usuario no encontrado"

             # Validar que los campos no estén vacíos o tengan valores válidos
            assert usuarios["id"] == 2, "El ID del usuario no es el esperado"
            assert usuarios["email"] == "janet.weaver@reqres.in", "El email del usuario no es el esperado"
            assert usuarios["first_name"] == "Janet", "El nombre del usuario no es el esperado"
            assert usuarios["last_name"] == "Weaver", "El apellido del usuario no es el esperado"
            assert usuarios["avatar"].startswith("https://"), "El avatar del usuario no tiene una URL válida"

            # Validación de la sección 'support'
            support = data.get("support")
            assert support, "El campo 'support' está ausente"
            assert "url" in support and "text" in support, "Los campos 'url' y 'text' faltan en 'support'"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Obtener Detalles de Usuario Unico")
    @allure.title("TC3: (GET) VALIDAR NO ENCONTRAR USUARIO CON ID 23")
    def test_no_encontrar_usuario_id_23(self):
        
        with allure.step("Preparar Solicitud GET"):
            endpoint = "/users/23"
            url = f"{self.BASE_URL}{endpoint}"
            params = {}
            
            
            request_details = {
                "URL": url,
                "Método": "GET",
                "Parámetros": params
            }
            allure.attach(
                json.dumps(request_details, indent=2), 
                name="Detalles de Solicitud", 
                attachment_type=allure.attachment_type.JSON
            )

        
        with allure.step("Enviar Solicitud"):
            start_time = time.time()
            response = requests.get(url, params=params)
            response_time = time.time() - start_time

        
        with allure.step("Documentar Respuesta"):
            response_details = {
                "Código de Estado": response.status_code,
                "Tiempo de Respuesta (s)": round(response_time, 2),
                "Cabeceras": dict(response.headers)
            }
            
            
            allure.attach(
                json.dumps(response_details, indent=2), 
                name="Metadatos de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )
            
            
            allure.attach(
                json.dumps(response.json(), indent=2), 
                name="Contenido de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )

        # Validaciones
        with allure.step("Validar Respuesta Usuario No Encontrado"):
            # Validación de código de estado
            assert response.status_code == 404, "Solicitud de usuarios no exitosa"

            # Validación de estructura de datos
            response_body = response.json()
            assert "data" not in response_body, "La respuesta no debería contener el campo 'data'"

            
         


    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Creación de Usuario")
    @allure.title("TC4: (POST) CREAR UN NUEVO USUARIO")
    def test_crear_usuario(self):
        
        with allure.step("Preparar Payload"):
            payload = {
                "name": "morpheus",
                "job": "leader"
            }
            
        
            allure.attach(
                json.dumps(payload, indent=2), 
                name="Datos de Usuario", 
                attachment_type=allure.attachment_type.JSON
            )

        
        with allure.step("Enviar Solicitud POST"):
            endpoint = "/users"
            url = f"{self.BASE_URL}{endpoint}"
            
            start_time = time.time()
            response = requests.post(url, json=payload)
            response_time = time.time() - start_time

        
        with allure.step("Documentar Respuesta"):
            response_details = {
                "Código de Estado": response.status_code,
                "Tiempo de Respuesta (s)": round(response_time, 2)
            }
            
            allure.attach(
                json.dumps(response_details, indent=2), 
                name="Metadatos de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )
            
            allure.attach(
                json.dumps(response.json(), indent=2), 
                name="Contenido de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )

        # Validaciones
        with allure.step("Validar Creación"):
            # Validación de código de estado
            assert response.status_code == 201, "Creación de usuario fallida"

            # Validación de datos
            data = response.json()
            assert data["name"] == payload["name"], "Nombre no coincide"
            assert data["job"] == payload["job"], "Trabajo no coincide"
            assert "id" in data, "ID de usuario no generado"
            assert "createdAt" in data, "Fecha de creación no registrada"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Creación de Usuario")
    @allure.title("TC5: (PUT) VALIDAR ACTUALIZAR USUARIO CON ID 2")
    def test_actualizar_usurio_con_id_2(self):
        
        with allure.step("Preparar Payload"):
            payload = {
                "name": "morpheus",
                "job": "zion resident"
            }
            
            
            allure.attach(
                json.dumps(payload, indent=2), 
                name="Datos de Usuario", 
                attachment_type=allure.attachment_type.JSON
            )

    
        with allure.step("Enviar Solicitud PUT"):
            endpoint = "/users/2"
            url = f"{self.BASE_URL}{endpoint}"
            
            start_time = time.time()
            response = requests.post(url, json=payload)
            response_time = time.time() - start_time

        
        with allure.step("Documentar Respuesta"):
            response_details = {
                "Código de Estado": response.status_code,
                "Tiempo de Respuesta (s)": round(response_time, 2)
            }
            
            allure.attach(
                json.dumps(response_details, indent=2), 
                name="Metadatos de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )
            
            allure.attach(
                json.dumps(response.json(), indent=2), 
                name="Contenido de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )

        # Validaciones
        with allure.step("Validar Actualizacion usuario 2"):
            # Validación de código de estado
            assert response.status_code == 201, "Actualizacion  de usuario fallida"

            # Validación de datos
            data = response.json()
            assert data["name"] == payload["name"], "Nombre no coincide"
            assert data["job"] == payload["job"], "Trabajo no coincide"

    @allure.severity(allure.severity_level.NORMAL)
    @allure.story("Creación de Usuario")
    @allure.title("TC6: (PATCH) VALIDAR ACTUALIZAR USUARIO CON ID 2")
    def test_actualizar_con_metodo_patch_con_id_2(self):
        
        with allure.step("Preparar Payload"):
            payload = {
                "name": "morpheus",
                "job": "zion resident"
            }
            
            
            allure.attach(
                json.dumps(payload, indent=2), 
                name="Datos de Usuario", 
                attachment_type=allure.attachment_type.JSON
            )

        
        with allure.step("Enviar Solicitud PATCH"):
            endpoint = "/users/2"
            url = f"{self.BASE_URL}{endpoint}"
            
            start_time = time.time()
            response = requests.patch(url, json=payload)
            response_time = time.time() - start_time

        
        with allure.step("Documentar Respuesta"):
            response_details = {
                "Código de Estado": response.status_code,
                "Tiempo de Respuesta (s)": round(response_time, 2)
            }
            
            allure.attach(
                json.dumps(response_details, indent=2), 
                name="Metadatos de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )
            
            allure.attach(
                json.dumps(response.json(), indent=2), 
                name="Contenido de Respuesta", 
                attachment_type=allure.attachment_type.JSON
            )

        # Validaciones
        with allure.step("Validar Actualizacion usuario 2"):
            # Validación de código de estado
            assert response.status_code == 200, "Actualizacion  de usuario fallida"

            # Validación de datos
            data = response.json()
            assert data["name"] == payload["name"], "Nombre no coincide"
            assert data["job"] == payload["job"], "Trabajo no coincide"
            
            # Validar campo updatedAt
            assert "updatedAt" in data, "Fecha de actualización no registrada"

    @allure.severity(allure.severity_level.CRITICAL)
    @allure.story("Obtener Detalles de Usuario Unico")
    @allure.title("TC7: (DELETE) VALIDAR LA ELIMINACIO DEL USUARIO CON ID 2")
    def test_eliminar_usuario_con_id_2(self):
        
        with allure.step("Preparar Solicitud DELETE"):
            endpoint = "/users/2"
            url = f"{self.BASE_URL}{endpoint}"
            params = {}

        
            request_details = {
                "URL": url,
                "Método": "DELETE",
                "Parámetros": params
            }
            allure.attach(
                json.dumps(request_details, indent=2),
                name="Detalles de Solicitud",
                attachment_type=allure.attachment_type.JSON
            )

        
        with allure.step("Enviar Solicitud"):
            start_time = time.time()
            response = requests.delete(url, params=params)
            response_time = time.time() - start_time

        
        with allure.step("Documentar Respuesta"):
            response_details = {
                "Código de Estado": response.status_code,
                "Tiempo de Respuesta (s)": round(response_time, 2),
                "Cabeceras": dict(response.headers)
            }

            
            allure.attach(
                json.dumps(response_details, indent=2),
                name="Metadatos de Respuesta",
                attachment_type=allure.attachment_type.JSON
            )

            
            if response.status_code != 204:
                try:
                    response_body = response.json()
                    allure.attach(
                        json.dumps(response_body, indent=2),
                        name="Contenido de Respuesta",
                        attachment_type=allure.attachment_type.JSON
                    )
                except ValueError:
                    pass  # En caso de que no haya un cuerpo válido en la respuesta

        # Validaciones
        with allure.step("Validar Respuesta"):
            # Validación de código de estado
            assert response.status_code == 204, "Eliminacion de usuarios no exitosa"
