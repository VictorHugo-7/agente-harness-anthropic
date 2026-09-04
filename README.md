<!--TÍTULO-->
# Agente Harness Anthropic


<!--DESCRIÇÃO-->
> Projeto baseado no artigo [Harness Design for Long-Running Applications](https://www.anthropic.com/engineering/harness-design-long-running-apps).<br/>
> O projeto consiste em agentes de IA trabalhando em conjunto para construir uma landing page de forma autônoma: um agente planeja, outro desenvolve e um terceiro testa e revisa o resultado em um navegador real.


<!--FUNCIONALIDADES-->
## Funcionalidades
````
Harness:
    . Planner: pega o pedido e transforma numa lista de seções
    . Generator: escreve o index.html, style.css e script.js
    . Evaluator: abre a página no navegador (Playwright), acha erros de verdade e aprova ou manda corrigir
    . Loop automático: Generator <-> Evaluator até aprovar ou acabar as rodadas
    . Modo demo:
        True  -> Força erro na 1ª rodada para demonstrar: erro → correção → aprovação.
        False -> Execução normal, sem erro forçado.
````


<!--TECNOLOGIAS-->
## Tecnologias
| <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg" width="40"/> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/html5/html5-original.svg" width="40"/> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/css3/css3-original.svg" width="40"/> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/javascript/javascript-original.svg" width="40"/> | <img src="https://cdn.simpleicons.org/claude" width="40"/> | <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/playwright/playwright-original.svg" width="40"/> |
| --------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Python | HTML5 | CSS3 | JavaScript | Claude API | Playwright |


<!--DEPENDÊNCIAS-->
## Dependência
````
anthropic     | ^0.40.0 | Cliente pra chamar a API da Anthropic
python-dotenv | ^1.0.0  | Lê a ANTHROPIC_API_KEY do .env
playwright    | ^1.49.0 | Abre a página num Chromium headless pra testar de verdade
````


<!--COMO UTILIZAR-->
## Como Utilizar
```
Requisitos:
    . Python 3.10+
    . pip
    . Uma chave de API da Anthropic (ANTHROPIC_API_KEY)

Execução:
    1. Clone o repositório                | git clone https://github.com/VictorHugo-7/agente-harness-anthropic

    2. Navegue até o diretório do projeto | cd agente-harness-anthropic

    3. Instale as dependências            | pip install -r requirements.txt
                                          | playwright install chromium

    4. Configure sua chave                | ANTHROPIC_API_KEY="sua_chave_secreta"

    5. (Opcional) muda o pedido           | edite a chave tarefa no prompts.json

    6. (Opcional) muda os agentes         | edite planner, generator, evaluator no prompts.json

    8. Roda o harness                     | python main.py

    9. Vê o resultado                     | abre output/index.html no navegador
```


<!--ESTRUTURA DE PASTAS-->
## Estrutura de Pastas
````
agente-harness-anthropic/
├── agents/
│   ├── evaluator.py
│   ├── generator.py
│   └── planner.py
├── .gitignore
├── config.py
├── main.py
├── prompts.json
├── requirements.txt
└─ README.md
````


<!--ESTATÍSTICAS-->
## Estatísticas
![](https://visitor-badge.laobi.icu/badge?page_id=VictorHugo-7.agente-harness-anthropic)
![Tamanho do Repositório](https://img.shields.io/github/repo-size/VictorHugo-7/agente-harness-anthropic)
![Linguagens](https://img.shields.io/github/languages/top/VictorHugo-7/agente-harness-anthropic)


<!--LICENÇA-->
## Licença
