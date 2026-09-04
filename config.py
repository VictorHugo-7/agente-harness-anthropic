import os
import json
from pathlib import Path
from dotenv import load_dotenv
import anthropic

load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    raise RuntimeError("Defina ANTHROPIC_API_KEY no arquivo .env")

client = anthropic.Anthropic(api_key=API_KEY)

MODEL = "claude-sonnet-5"
MAX_RODADAS = 2
CAMINHO_PROMPTS = Path(__file__).parent / "prompts.json"

def extrair_texto(resposta) -> str:
    return "".join(bloco.text for bloco in resposta.content if getattr(bloco, "type", None) == "text").strip()

def _carregar_config() -> dict:
    return json.loads(CAMINHO_PROMPTS.read_text(encoding="utf-8"))

def carregar_prompt(nome_agente: str) -> str:
    return _carregar_config()[nome_agente]

def carregar_tarefa() -> str:
    return _carregar_config()["tarefa"]