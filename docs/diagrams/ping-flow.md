# Fluxo do endpoint `/ping`

```mermaid
sequenceDiagram
    participant C as Cliente
    participant A as FastAPI

    C->>A: GET /ping
    alt sem parâmetro fail
        A-->>C: 200 OK {"message": "pong"}
    else fail=400
        A-->>C: 400 {"error": "requisição inválida simulada"}
    else fail=500
        A-->>C: 500 {"error": "erro interno do servidor"}
    end
```

Fluxo equivalente:

```mermaid
flowchart LR
    Cliente -->|GET /ping| FastAPI
    FastAPI --> Decisao{fail informado?}
    Decisao -->|não| OK[200 + pong]
    Decisao -->|400| BadRequest[400 + erro de requisição]
    Decisao -->|500| InternalError[500 + erro interno]
    OK --> Cliente
    BadRequest --> Cliente
    InternalError --> Cliente
```
