from pathlib import Path
from playwright.sync_api import sync_playwright
from config import client, MODEL, extrair_texto, carregar_prompt

SYSTEM = carregar_prompt("evaluator")

def testar_com_playwright(pasta: Path) -> dict:
    arquivo = (pasta / "index.html").resolve()
    resultado = {"console_errors": [], "page_errors": []}

    if not arquivo.exists():
        resultado["page_errors"].append("index.html não encontrado.")
        return resultado

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1280, "height": 800})
        page.on("console", lambda msg: resultado["console_errors"].append(msg.text) if msg.type == "error" else None)
        page.on("pageerror", lambda err: resultado["page_errors"].append(str(err)))

        try:
            page.goto(arquivo.as_uri(), wait_until="load")
            cta = page.locator("#cta-btn")
            if cta.count() > 0:
                cta.click(timeout=2000)
            page.wait_for_timeout(300)
        except Exception as e:
            resultado["page_errors"].append(str(e))

        browser.close()

    return resultado

def avaliar(html: str, css: str, js: str, dados_playwright: dict) -> str:
    prompt = f"""
        HTML: {html}
        CSS:{css}
        JS:{js}
        Inspeção no navegador (Playwright):
        Erros de console: {dados_playwright['console_errors']}
        Erros de página: {dados_playwright['page_errors']} """
    
    resposta = client.messages.create(
        model=MODEL,
        max_tokens=400,
        system=SYSTEM,
        messages=[{"role": "user", "content": prompt}],
    )
    return extrair_texto(resposta)