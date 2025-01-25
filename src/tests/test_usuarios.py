import pytest
import requests
import allure
import json

@allure.epic("Reqres API Rest")
@allure.feature("US-001: Gestión de Usuarios")
class TestUsuarios:
    BASE_URL = "https://reqres.in/api"

    @allure.story("TC1: Flujo de obtención de lista de usuarios")
    def test_obtener_lista_usuarios(self):
        with allure.step("Realizar solicitud GET para obtener lista de usuarios"):
            url = f"{self.BASE_URL}/users"
            params = {"page": 2}
            response = requests.get(url, params=params)
            
            # Añadir detalles de la solicitud
            allure.attach(
                f"URL: {url}\nParámetros: {params}", 
                name="Detalles de la Solicitud", 
                attachment_type=allure.attachment_type.TEXT
            )
            
            # Añadir body de la respuesta
            allure.attach(
                json.dumps(response.json(), indent=2), 
                name="Respuesta Completa", 
                attachment_type=allure.attachment_type.JSON
            )

        with allure.step("Validar respuesta exitosa"):
            assert response.status_code == 200, "La solicitud de usuarios no fue exitosa"

        with allure.step("Validar estructura de datos"):
            data = response.json()
            assert "data" in data, "No se encontró la clave 'data' en la respuesta"
            assert len(data["data"]) > 0, "La lista de usuarios está vacía"

    @allure.story("TC2: Flujo de creación de usuario")
    def test_crear_usuario(self):
        with allure.step("Preparar datos de usuario"):
            payload = {
                "nombre": "morfeo",
                "trabajo": "líder"
            }
            
            # Añadir detalles del payload
            allure.attach(
                json.dumps(payload, indent=2), 
                name="Payload de Solicitud", 
                attachment_type=allure.attachment_type.JSON
            )

        with allure.step("Realizar solicitud POST para crear usuario"):
            url = f"{self.BASE_URL}/users"
            response = requests.post(url, json=payload)
            
            # Añadir body de la respuesta
            allure.attach(
                json.dumps(response.json(), indent=2), 
                name="Respuesta Completa", 
                attachment_type=allure.attachment_type.JSON
            )

        with allure.step("Validar respuesta de creación"):
            assert response.status_code == 201, "La creación de usuario no fue exitosa"

        with allure.step("Validar estructura de datos del usuario creado"):
            data = response.json()
            assert data["nombre"] == payload["nombre"], "El nombre no coincide"
            assert data["trabajo"] == payload["trabajo"], "El trabajo no coincide"
            assert "id" in data, "No se generó ID para el usuario"
            assert "createdAt" in data, "No se registró fecha de creación"