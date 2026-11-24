from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse

app = FastAPI(
    title="EDP Case Default API",
    description="API inicial para experimentação do repositório-base do EDP.",
    version="0.1.0",
    contact={"name": "EDP Case Default"},
    openapi_tags=[
        {
            "name": "health",
            "description": "Endpoints para verificar a saúde da aplicação.",
        }
    ],
)


@app.get(
    "/ping",
    tags=["health"],
    summary="Verifica se a API está respondendo",
    description="Retorna `pong` no fluxo normal. O parâmetro `fail` existe apenas para demonstrar respostas de erro.",
    responses={
        200: {"description": "API respondendo normalmente."},
        400: {"description": "Requisição inválida simulada."},
        500: {"description": "Erro interno simulado."},
    },
)
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
