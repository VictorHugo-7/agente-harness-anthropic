from pathlib import Path
from config import client, MODEL, extrair_texto, carregar_prompt

SYSTEM = carregar_prompt("generator")

def gerar(spec: str, feedback: str) -> dict:
    prompt = f"Especificação do Planner:\n{spec}\n\nFeedback da rodada anterior:\n{feedback}"
    resposta = client.messages.create(
        model=MODEL,
        max_tokens=4000,
        system=SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )
    texto = extrair_texto(resposta)

    html = texto.split("===HTML===")[1].split("===CSS===")[0].strip()
    css = texto.split("===CSS===")[1].split("===JS===")[0].strip()
    js = texto.split("===JS===")[1].strip()
    return {"html": html, "css": css, "js": js}

def salvar_arquivos(arquivos: dict, pasta: Path):
    pasta.mkdir(exist_ok=True)
    (pasta / "index.html").write_text(arquivos["html"], encoding="utf-8")
    (pasta / "style.css").write_text(arquivos["css"], encoding="utf-8")
    (pasta / "script.js").write_text(arquivos["js"], encoding="utf-8")