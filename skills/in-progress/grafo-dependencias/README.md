# Skill `grafo-dependencias`

Cria, documenta e mantém mapas visuais de dependências arquiteturais (grafos Mermaid e/ou SVG) para qualquer fluxo de software, independente da linguagem ou framework (Python, TypeScript, Kotlin, Dart/Flutter, Java, Go, C#, etc.).

---

## 🎯 O que a skill faz

- **Mapeia fluxos de código reais:** rastreia com precisão métodos, funções e chamadas feitas a partir de um ponto de entrada (rota HTTP, controller, worker, etc.).
- **Divide em etapas lógicas:** organiza a sequência temporal de execução em subgraphs numerados.
- **Categoriza por camadas arquiteturais:** aplica uma paleta padronizada de cores e formas semânticas (classes, interfaces entre parênteses, entidades em cápsula, sistemas externos em hexágono).
- **Garante integridade e transparência:** por padrão, **não omite nenhuma conexão real** do código sem a autorização do usuário (apenas factories de injeção e loggers genéricos são abstraídos). Havendo dúvidas sobre a densidade do grafo, o agente pergunta ao usuário se prefere simplificar ou manter a fidelidade total.

---

## 🚀 Como usar

Basta solicitar ao agente em linguagem natural, especificando o fluxo e, se desejar, o ponto de entrada:

- *"Crie o grafo de dependências do fluxo de busca no backend (`POST /v1/search`)."*
- *"Mapeie o fluxo de ingestão de documentos a partir de `ingestions.py`."*
- *"Atualize o grafo do fluxo de notificações após a refatoração."*

---

## 📦 Arquivos Gerados

Para cada fluxo documentado em `docs/grafos/` (ou caminho equivalente do repositório):

| Arquivo | Descrição |
| :--- | :--- |
| `images/grafo_<fluxo>.svg` | **Imagem gerada via `mmdc` (formato padrão exibido no `.md`).** |
| `mermaid/grafo_<fluxo>.mmd` | Fonte em Mermaid puro (onde o grafo é mantido e editado). |
| `grafo_<fluxo>.md` | Documento estruturado com a imagem SVG, legenda e tabela de classes/componentes. |

---

## 🛠️ Renderização do Diagrama

- **Padrão e Preferência:** O documento Markdown sempre incorpora a imagem vetorial SVG gerada (`![Grafo](./images/grafo_<fluxo>.svg)`).
- **Geração do SVG:** Feita automaticamente via Node.js usando `mmdc` (ou `npx -y -p @mermaid-js/mermaid-cli@12.0.0 mmdc ...`).
- **Fallback Excepcional:** O bloco de código Mermaid nativo (```` ```mermaid ````) só é inserido no `.md` caso o ambiente não possua Node.js para compilar o SVG.
