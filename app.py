from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import random

app = FastAPI(title="Servicio de cédula")


@app.get("/obtener_cedula")
def obtener_cedula() -> int:
    # Genera un número entero aleatorio de exactamente 10 dígitos
    return random.randint(1_000_000_000, 9_999_999_999)


@app.get("/swagger.html", response_class=HTMLResponse)
def swagger_html():
    """Sirve el archivo swagger.html incluido en el proyecto."""
    with open("swagger.html", "r", encoding="utf-8") as f:
        return HTMLResponse(content=f.read(), media_type="text/html")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
