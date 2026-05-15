# Movie Chatbot

Chatbot de filmes com backend em Python/FastAPI e frontend em Next.js.

## Visao Geral

O projeto recebe uma mensagem do usuario no endpoint `/chat`, usa um supervisor para decidir quais agentes devem atuar e executa ferramentas relacionadas a filmes, como busca, detalhes, elenco, reviews, trailers e recomendacoes.

Fluxo principal:

```text
POST /chat
  -> AgentState
  -> supervisor_node
  -> agent_executor_node
  -> response_node
  -> resposta final
```

## Tecnologias

- Python 3.12
- FastAPI
- Uvicorn
- LangGraph
- OpenAI SDK, usado tambem com Groq via endpoint compativel
- Google GenAI
- HTTPX
- Pydantic
- Next.js
- React
- Docker e Docker Compose

## Estrutura

```text
backend/
  Dockerfile
  .env
  app/
    api/routes/        Rotas HTTP
    agents/           Definicoes e registro de agentes
    graph/            Builder e nodes do LangGraph
    mcp/              MCPs e tools disponiveis
    services/         Providers de LLM e integracoes externas
    schemas/          Schemas Pydantic
    states/           Estado compartilhado do grafo

frontend/
  Dockerfile
  .env.local
  app/
  components/
  services/
```

## Variaveis de Ambiente

Crie um arquivo `backend/.env`:

```env
APP_NAME=Movie AI
API_VERSION=/api/v1
LOG_LEVEL=INFO

TMDB_API_TOKEN=seu_token_tmdb
GROQ_API_KEY=sua_chave_groq

LLM_PROVIDER=groq
LLM_MODEL=llama3-8b-8192
LLM_TEMPERATURE=0.7
```

Crie um arquivo `frontend/.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

Observacao: arquivos `.env` nao devem ser versionados.

## Rodando com Docker

Suba backend e frontend com:

```bash
docker compose up --build
```

O frontend ficara disponivel em:

```text
http://localhost:3000/chat
```

A API ficara disponivel em:

```text
http://localhost:8000
```

Documentacao interativa do FastAPI:

```text
http://localhost:8000/docs
```

## Rodando Localmente

### Backend

Crie e ative um ambiente virtual:

```bash
cd backend
python3 -m venv venv
source venv/bin/activate
```

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Inicie a API:

```bash
cd ..
uvicorn backend.app.main:app --host 0.0.0.0 --port 8000 --reload
```

### Frontend

Instale as dependencias:

```bash
cd frontend
npm install
```

Inicie o Next.js:

```bash
npm run dev
```

## Endpoint Principal

### POST `/chat`

Exemplo de request:

```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Me recomende filmes parecidos com Interestelar"}'
```

Exemplo de body:

```json
{
  "message": "Me recomende filmes parecidos com Interestelar"
}
```

## Validacoes

Checar sintaxe dos arquivos Python:

```bash
backend/venv/bin/python -m compileall backend/app
```

Checar dependencias instaladas:

```bash
pip check
```

Validar compose:

```bash
docker compose config --quiet
```

## Observacoes

- O provider padrao e `groq`.
- A integracao com o TMDB depende de `TMDB_API_TOKEN`.
- O Docker Compose monta `./backend/app:/app/backend/app`, entao alteracoes no backend sao refletidas durante o desenvolvimento.
- O frontend usa `NEXT_PUBLIC_API_URL=http://localhost:8000` para o navegador chamar a API local.
