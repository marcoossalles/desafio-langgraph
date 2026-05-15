# Movie Chatbot

Backend em Python para um chatbot de filmes usando FastAPI, LangGraph, LLMs e a API do TMDB.

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
- Docker e Docker Compose

## Estrutura

```text
app/
  api/routes/          Rotas HTTP
  agents/             Definicoes e registro de agentes
  graph/              Builder e nodes do LangGraph
  mcp/                MCPs e tools disponiveis
  services/           Providers de LLM e integracoes externas
  schemas/            Schemas Pydantic
  states/             Estado compartilhado do grafo
```

## Variaveis de Ambiente

Crie um arquivo `.env` na raiz do projeto:

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

Observacao: o `.env` nao deve ser versionado.

## Rodando com Docker

Suba a aplicacao com:

```bash
docker compose up --build
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

Crie e ative um ambiente virtual:

```bash
python3 -m venv venv
source venv/bin/activate
```

Instale as dependencias:

```bash
pip install -r requirements.txt
```

Inicie a API:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
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
python3 -m compileall app
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
- O Docker Compose monta `./app:/app/app`, entao alteracoes no codigo sao refletidas durante o desenvolvimento.
