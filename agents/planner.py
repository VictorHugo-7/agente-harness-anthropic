from config import client, MODEL, extrair_texto, carregar_prompt

SYSTEM = carregar_prompt("planner")

def planejar(tarefa: str) -> str:
    resposta = client.messages.create(
        model=MODEL,
        max_tokens=400,
        system=SYSTEM,
        messages=[{"role": "user", "content": tarefa}],
    )
    return extrair_texto(resposta)