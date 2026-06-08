# python-claude-client

Cliente de la API de Claude escrito en Python. Permite enviar mensajes al modelo y recibir respuestas, con soporte para prompt caching y streaming.

## Que contiene

```
src/client.py      # wrapper sobre el SDK de Anthropic
src/utils.py       # logging de metadatos e utilidades de texto
prompts/           # system prompts como archivos .txt
main.py            # CLI: acepta un mensaje y devuelve la respuesta
tests/             # tests unitarios con pytest y mocks
```

## Configuracion

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # anade tu ANTHROPIC_API_KEY
```

## Uso

```bash
# respuesta directa
python main.py "Explica que es el prompt caching"

# con system prompt personalizado
python main.py "Revisa este codigo" --prompt code_reviewer

# streaming token a token
python main.py "Cuéntame algo" --stream
```

## Tests

```bash
pytest tests/ -v
```
