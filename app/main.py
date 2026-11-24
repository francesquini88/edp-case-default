from fastapi import FastAPI

app = FastAPI(title="EDP Case Default")


@app.get("/ping")
def ping() -> dict[str, str]:
    return {"message": "pong"}
