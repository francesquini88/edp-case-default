from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI(title="EDP Case Default")


@app.get("/ping")
def ping(fail: int | None = Query(default=None, description="Use 400 ou 500 para simular uma falha")) -> JSONResponse:
    try:
        if fail == 400:
            raise ValueError("requisição inválida simulada")
        if fail == 500:
            raise RuntimeError("erro interno simulado")

        return JSONResponse(status_code=200, content={"message": "pong"})
    except ValueError as error:
        return JSONResponse(status_code=400, content={"error": str(error)})
    except Exception:
        return JSONResponse(status_code=500, content={"error": "erro interno do servidor"})
