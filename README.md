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
{"message":"pong"}
```

Documentação automática da API:

- http://localhost:8000/docs
- http://localhost:8000/redoc

O endpoint `/ping` está documentado no Swagger com a tag `health`, descrição dos parâmetros e respostas `200`, `400` e `500`.

## Executar localmente sem Docker

### 1. Criar o ambiente virtual

Windows PowerShell:

```powershell
python -m venv .venv
```

Linux ou macOS:

```bash
python3 -m venv .venv
```

### 2. Ativar o ambiente virtual

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Linux ou macOS:

```bash
source .venv/bin/activate
```

Se o PowerShell bloquear a ativação, execute uma vez:

```powershell
Set-ExecutionPolicy -Scope CurrentUser RemoteSigned
```

### 3. Instalar as dependências

Com o ambiente virtual ativo:

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### 4. Iniciar a API

```bash
uvicorn app.main:app --reload
```

Teste em http://localhost:8000/ping.

Para demonstrar os tratamentos de erro:

```text
http://localhost:8000/ping?fail=400  # requisição inválida
http://localhost:8000/ping?fail=500  # erro interno
```

Sem o parâmetro `fail`, a resposta normal é `200` com `pong`.

Para encerrar, pressione `Ctrl+C`. Para sair do ambiente virtual:

```bash
deactivate
```

## Executar os testes

Com o ambiente virtual ativo:

```bash
python -m pytest
```

## Estrutura

```text
app/main.py       # aplicação FastAPI e endpoint /ping
tests/test_ping.py # teste do endpoint
docs/diagrams/     # diagramas Mermaid e documentação visual
Dockerfile        # imagem da aplicação
docker-compose.yml # execução local com Docker Compose
```

## Diagrama do endpoint `/ping`

O fluxo mínimo da requisição está em [`docs/diagrams/ping-flow.md`](docs/diagrams/ping-flow.md).
