# Servicio FastAPI - Obtener Cédula

Descripción
- Servicio web en FastAPI que expone un endpoint `GET /obtener_cedula` que devuelve un número entero aleatorio de 10 dígitos.

Respuesta
- Tipo: `application/json` (entero) 
- Ejemplo de respuesta:

```
1234567890
```

Nota: Actualmente la API retorna directamente el número entero (no envuelve en un objeto). Si prefieres `{"cedula": 1234567890}` puedo cambiarlo.

Endpoints importantes
- Swagger UI (interfaz interactiva): `http://localhost:8000/docs`
- OpenAPI JSON: `http://localhost:8000/openapi.json`

Probar localmente (sin Docker)

1. Crear y activar un entorno virtual (opcional):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Instalar dependencias e iniciar:

```bash
pip install -r requirements.txt
uvicorn app:app --reload --host 0.0.0.0 --port 8000
```

3. Probar con curl:

```bash
curl http://127.0.0.1:8000/obtener_cedula
```

Usar Docker

Build y run con Docker:

```bash
docker build -t taller-cedula:latest .
docker run --rm -p 8000:8000 taller-cedula:latest
```

Con docker-compose:

```bash
docker-compose up --build
```

Después de levantado, la API estará disponible en `http://localhost:8000/obtener_cedula` y la documentación en `/docs`.

Postman

- Importa la colección localizada en `postman_collection.json` en la raíz del proyecto.
- La colección usa una variable `base_url` con valor por defecto `http://localhost:8000`.

Swagger / OpenAPI

- FastAPI expone la documentación Swagger automáticamente en `/docs`.
- También puedes obtener el JSON de la especificación en `/openapi.json`.

Archivos añadidos
- `Dockerfile` — imagen para ejecutar la app.
- `docker-compose.yml` — levantar la app con `docker-compose up`.
- `.dockerignore` — reducir contexto de build.
- `postman_collection.json` — colección para importar en Postman.

¿Quieres que modifique la respuesta para devolver un objeto JSON con la clave `cedula` y ejemplos de tests automatizados?
