from pathlib import Path
from config import MAX_RODADAS, carregar_tarefa
from agents.planner import planejar
from agents.generator import gerar, salvar_arquivos
from agents.evaluator import testar_com_playwright, avaliar

PASTA_OUTPUT = Path("output")

# Modo demo: injeta de propósito um bug na 1ª rodada só para mostrar o Evaluator pegando um erro real e o Generator corrigindo na 2ª rodada.
# Deixe False para rodar o harness sem bug forçado.
MODO_DEMO = True

def injetar_bug_demo(arquivos: dict) -> dict:
    arquivos = dict(arquivos)
    arquivos["js"] += "\n\n// bug proposital injetado só para demonstração\nconst demoBug = 'string sem fechar;"
    return arquivos

def imprimir_indentado(texto: str):
    for linha in texto.split("\n"):
        linha = linha.strip()
        if linha:
            print(f"\t{linha}")

def main():
    print("Harness Simples: Planner -> Generator -> Evaluator")
    print()

    print("[1/3] Planner criando a especificação...")
    tarefa = carregar_tarefa()
    spec = planejar(tarefa)
    imprimir_indentado(spec)

    feedback = "Primeira versão, siga a especificação."
    arquivos = {"html": "", "css": "", "js": ""}

    for rodada in range(1, MAX_RODADAS + 1):
        print()
        print(f"[2/3] Generator - rodada {rodada}")
        arquivos = gerar(spec, feedback)

        if MODO_DEMO and rodada == 1:
            print("\t(modo demo: injetando um bug proposital no JS para a demonstração)")
            arquivos_para_teste = injetar_bug_demo(arquivos)
        else:
            arquivos_para_teste = arquivos

        salvar_arquivos(arquivos_para_teste, PASTA_OUTPUT)
        print("\tarquivos salvos em output/")
        print()

        print("[3/3] Evaluator: testando com Playwright...")
        dados_playwright = testar_com_playwright(PASTA_OUTPUT)
        print(f"\terros de console: {dados_playwright['console_errors']}")
        print(f"\terros de página: {dados_playwright['page_errors']}")

        print("\tEvaluator: revisando o código...")
        resultado = avaliar(arquivos_para_teste["html"], arquivos_para_teste["css"], arquivos_para_teste["js"], dados_playwright)
        imprimir_indentado(resultado)

        sem_erros = not dados_playwright["console_errors"] and not dados_playwright["page_errors"]
        if resultado.upper().startswith("APROVADO") and sem_erros:
            print()
            print(f"Aprovado na rodada {rodada}")
            break

        feedback = resultado
        if not sem_erros:
            feedback += f"\nErros reais encontrados no navegador: {dados_playwright}"

    print(f"Resultado final em: {PASTA_OUTPUT}/index.html")

if __name__ == "__main__":
    main()