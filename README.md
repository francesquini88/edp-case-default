# EDP Case Default

Starter mínimo e público para o repositório-base do EDP.

## Subir a aplicação

```bash
docker compose up --build
```

Depois, acesse:

```text
http://localhost:8000/ping
```

Resposta esperada:

```json
{"message":"hello world"}
```

Documentação automática da API:

- http://localhost:8000/docs
- http://localhost:8000/redoc

## Executar o teste

```bash
pip install -r requirements.txt
pytest
```

## Estrutura

```text
app/main.py       # aplicação FastAPI e endpoint /ping
tests/test_ping.py # teste do endpoint
Dockerfile        # imagem da aplicação
docker-compose.yml # execução local com Docker Compose
```
