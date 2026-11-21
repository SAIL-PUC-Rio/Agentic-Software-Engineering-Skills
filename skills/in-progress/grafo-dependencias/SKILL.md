---
name: grafo-dependencias
description: >-
  Cria ou atualiza mapas de dependências arquiteturais (grafos Mermaid e/ou SVG) para qualquer fluxo, serviço ou módulo de software, independentemente de linguagem ou framework (Python, FastAPI, Kotlin, Dart/Flutter, TypeScript, Go, Java, C#, etc.). Gera diagramas estruturados em subgraphs sequenciais de etapas do fluxo, com categorização visual por camadas arquiteturais, formas semânticas (classes/módulos, interfaces entre parênteses, entidades em cápsula, fronteiras externas em hexágono), rótulos estritos de métodos/funções chamados e tabela descritiva de componentes. Por padrão, NUNCA oculta conexões reais de código sem confirmação explícita do usuário.
---

# Mapa de dependências (Grafo de Fluxos & Arquitetura)

Esta skill cria, documenta e mantém mapas visuais de dependências de código em projetos de software.
O grafo mostra quais componentes (classes, funções, módulos, rotas) participam de um fluxo, a ordem em que interagem, quem chama quem e quais métodos ou funções específicos são invocados.

---

## 1. Princípios Fundamentais (Invioláveis)

1. **Aderência Estrita ao Código Real:**
   Toda aresta precisa existir de verdade no código. Nunca deduza chamadas por convenção de nome. Inspecione o código diretamente (leituras de arquivos, buscas de chamadas, construtores, injeções de dependência).

2. **Política de Conexões — Não Oculte Conexões por Decisão Arbitrária:**
   - **Regra padrão:** O agente **NUNCA** deve omitir, podar ou simplificar conexões sob a justificativa de que o grafo está "muito poluído" ou "complexo". O objetivo do grafo é a fidelidade técnica.
   - **Exceções canônicas aceitas sem confirmação:**
     - **Factories / Mecanismos de Injeção de Dependência:** Abstraia a factory e ligue a dependência diretamente à implementação concreta injetada (ou à classe instanciada).
     - **Loggers:** Utilitários de log (`logging.getLogger()`, `AppLogger`, etc.) são omitidos a menos que definam branches de negócio do fluxo.
   - **Dúvidas sobre densidade de conexões:** Se houver um número muito alto de conexões cruzadas ou utilitários recorrentes (ex.: conversões de tipo, tratamentos de erro genéricos, constantes), **pergunte ativamente ao usuário**:
     > *"O fluxo possui conexões secundárias para [Componente X / Utilitário Y]. Deseja incluir todas as conexões para máxima fidelidade ou prefere focar apenas no caminho crítico de negócio?"*
     Se o usuário não especificar, **mantenha todas as conexões reais**.

3. **Independência de Linguagem e Framework:**
   A skill não assume uma linguagem fixa. Ela adapta os termos (classes, módulos, usecases, rotas, schemas, structs) e as camadas arquiteturais à realidade do projeto sob análise.

4. **Interfaces entre Parênteses:**
   Quando um componente implementa uma interface, contrato, protocolo ou classe abstrata, isso é sinalizado dentro do rótulo do nó entre parênteses logo abaixo do nome:
   `NomeComponente["NomeComponente<br/>(IContrato)"]`

---

## 2. Padrão Visual Obrigatório

Copie a estrutura `init` e a paleta de estilos padrão para manter harmonia e contraste em temas claros e escuros:

### 2.1 Cores por Papel Arquitetural

As cores representam o papel arquitetural de cada componente no fluxo:

| `classDef` | Cor | Papel Arquitetural | Exemplos Backend / Web / Mobile |
| :--- | :--- | :--- | :--- |
| `pres` | Roxo (`#f3e8ff` / borda `#9333ea` / texto `#7e22ce`) | **Apresentação & Entrada (Entrypoints)** | Rotas FastAPI/Express/Spring, Controllers, Handlers gRPC, Workers de fila, Activities/Screens |
| `core` | Azul (`#e0f2fe` / borda `#0284c7` / texto `#0369a1`) | **Domínio & Regras de Negócio** | Casos de uso (`UseCases`), Serviços de domínio (`Services`), Algoritmos de negócio |
| `infra` | Verde (`#dcfce7` / borda `#16a34a` / texto `#15803d`) | **Infraestrutura & Adaptadores** | Repositórios, Gateways, Clientes HTTP/SDKs, Adaptadores de BD/Cache, Mailers |
| `entity` | Amarelo (`#fef3c7` / borda `#d97706` / texto `#b45309`) | **Entidades & Dados** | Modelos ORM (SQLAlchemy, Prisma, TypeORM), Schemas Pydantic/DTOs, Entidades de Domínio |
| `boundary` | Laranja tracejado (`#fff7ed` / borda `#ea580c` / texto `#c2410c`) | **Fronteiras & Sistemas Externos** | Microsserviços externos, APIs de terceiros, Bancos de Dados, Plataformas nativas (Bridge) |
| `boot` | Cinza (`#f1f5f9` / borda `#64748b` / texto `#334155`) | **Bootstrap & Configuração** | Arquivos de inicialização de app (`main.py`, `app.ts`, `settings.py`), Módulos DI |

### 2.2 Formas Semânticas dos Nós

| Forma | Sintaxe Mermaid | Finalidade |
| :--- | :--- | :--- |
| **Retângulo** | `Nome["Nome"]` ou `Nome["Nome<br/>(IInterface)"]` | Classes, funções, módulos, controllers, services, repositórios. |
| **Cápsula** | `Nome(["Nome"])` | Entidades de domínio, modelos de dados ou tabelas. |
| **Hexágono** | `SistemaExterno{{"Sistema / Serviço Externo<br/>Descrição"}}` | Fronteiras externas (ex: outro microsserviço, API externa, BD relacional, bridge de plataforma). |

### 2.3 Tipos de Arestas

| Sintaxe | Significado | Regra do Rótulo |
| :--- | :--- | :--- |
| `A -->\|"metodoA() / metodoB()"\| B` | Chamada síncrona/direta de função ou método | **Obrigatório**: lista de métodos ou funções chamadas com `()` e sem argumentos, separados por ` / `. |
| `A -.- E` | Leitura, instanciação ou retorno de entidade/modelo | Sem rótulo. |
| `A -.-> B` | Instanciação dinâmica em tempo de execução | Sem rótulo (a menos que passe parâmetros-chave relevantes). |
| `A -.->\|"onEvento"\| B` | Callback, evento assíncrono ou webhook | **Obrigatório**: nome do evento/callback. |
| `A ~~~ B` | Ligação invisível | Apenas para controlar layout Mermaid (precedida de comentário `%%`). |

> **Atenção:** Rótulos de arestas não devem conter frases descritivas longas (ex.: ~~"salva os dados no banco após validação"~~). Rótulos contêm apenas os identificadores de código (funções/métodos). Explicações contextuais pertencem à tabela descritiva no `.md`.

### 2.4 Subgraphs e Etapas

- Cada `subgraph` agrupa nós por **etapas cronológicas ou lógicas do fluxo** (e não por camadas de pastas):
  Exemplo: `1. Entrada / Requisição HTTP`, `2. Processamento e Regras de Negócio`, `3. Comunicação Externa e Persistência`.
- IDs dos subgraphs: `SB<N><NomeEmPascalCase>` (ex: `SB1Triggers`, `SB2BusinessLogic`, `SB3ExternalSync`).
- Bloco 1 (Entrypoints): use preferencialmente `direction LR`. Demais blocos: `direction TB`.

---

## 3. Estrutura dos Arquivos Gerados e Prioridade Visual

Defina o diretório de documentação apropriado para o repositório (ex.: `hackathon/docs/grafos/` ou `docs/grafos/`). Para cada fluxo mapeado:

1. **Fonte Mermaid (`.mmd`):** `.../mermaid/grafo_<fluxo>.mmd`
   Contém o código Mermaid puro, iniciando direto no bloco `%%{ init ... }%%`, sem blocos de código markdown ou tags HTML container. É o único arquivo onde a modelagem do grafo é editada e mantida.
2. **Imagem Vetorial SVG (`.svg`):** `.../images/grafo_<fluxo>.svg`
   - O SVG é o **formato preferencial e padrão** para exibição do diagrama.
   - Sempre que o ambiente possuir Node.js / `mmdc` (ou `npx -y -p @mermaid-js/mermaid-cli@12.0.0 mmdc`), **a geração do SVG é obrigatória**.
3. **Documento Explicativo (`.md`):** `.../grafo_<fluxo>.md`
   - **Regra de Exibição do Diagrama no Markdown:**
     - **Preferência Absoluta:** O documento Markdown **deve exibir a imagem SVG** via `![Grafo de Dependências — <Fluxo>](./images/grafo_<fluxo>.svg)` apontando para a fonte em `mermaid/grafo_<fluxo>.mmd`.
     - **Fallback Excepcional:** O bloco de código Mermaid nativo (```` ```mermaid ````) **SÓ DEVE** ser colocado diretamente no `.md` caso o ambiente não disponha de Node.js / `mmdc` para gerar o SVG. Havendo Node.js no ambiente, o `.md` exibe exclusivamente a imagem SVG.
   - Contém o título, breve resumo do fluxo, a imagem SVG (ou fallback mermaid), legenda arquitetural e a **Tabela de Componentes**.

---

## 4. Tabela de Componentes (Obrigatória no Documento `.md`)

Abaixo do diagrama, inclua a tabela detalhando todos os nós que aparecem no grafo:

| Componente / Classe | Arquivo / Módulo | Interfaces / Tipos | Métodos / Funções Chamadas | Descrição / Responsabilidade no Fluxo |
| :--- | :--- | :--- | :--- | :--- |
| `search_route` | `app/routes/search.py` | — | `POST /v1/search` | Recebe a requisição, orquestra cliente de IA e agrupa famílias. |
| `AiClient` | `app/clients/ai_client.py` | `(IAiClient)` | `search()` | Cliente HTTP que envia a busca ao módulo de IA. |
| `DocumentFamily` | `app/models.py` | — | — | Modelo de dados que representa a família de documentos. |

---

## 5. Roteiro de Execução

1. **Alinhamento do Fluxo:**
   - Identifique o ponto de entrada (rota HTTP, comando CLI, consumer de mensageria, etc.) e o objetivo do fluxo.
   - Caso o escopo do fluxo seja ambíguo ou amplo demais, pergunte ao usuário antes de iniciar.
2. **Rastreamento de Código:**
   - Abra os arquivos a partir do ponto de entrada.
   - Inspecione chamadas de funções, dependências injetadas, chamadas a banco ou serviços externos.
   - Aplique a política de abstração de factories e conecte diretamente à implementação concreta.
   - Coloque as interfaces entre parênteses no rótulo da classe.
   - Se houver dúvida quanto a poluição de conexões com muitos utilitários secundários, pergunte ao usuário. Caso contrário, mantenha todas as chamadas reais.
3. **Redação do Mermaid (`.mmd`):**
   - Use as `classDef` de cores padronizadas.
   - Estruture em subgraphs numerados pela ordem do fluxo.
4. **Geração do SVG e Criação do Documento (`.md`):**
   - Verifique a presença de Node.js no ambiente (`node -v`).
   - Se Node.js estiver disponível, gere o SVG com o `mmdc`:
     ```powershell
     mmdc -i <caminho>/mermaid/grafo_<fluxo>.mmd -o <caminho>/images/grafo_<fluxo>.svg -b white
     ```
     (Ou via `npx -y -p @mermaid-js/mermaid-cli@12.0.0 mmdc ...`).
   - No documento `.md`, referencie a imagem SVG (`![Grafo de Dependências](./images/grafo_<fluxo>.svg)`).
   - Se e somente se o Node.js não estiver disponível, faça o fallback inserindo o bloco ```` ```mermaid ```` dentro do `.md`.
5. **Checklist de Validação:**
   - [ ] Todo nó possui uma classe de estilo arquitetural associada (`pres`, `core`, `infra`, `entity`, `boundary`, `boot`).
   - [ ] Todos os métodos listados nas arestas existem no código e são chamados pela origem.
   - [ ] Nenhuma conexão real foi suprimida arbitrariamente sem confirmação ou sem ser factory/logger.
   - [ ] Interfaces implementadas estão indicadas entre parênteses.
   - [ ] Não há caracteres que quebram o Mermaid (como `<` ou `>` fora de tags HTML permitidas; genéricos devem ser simplificados ou substituídos).
   - [ ] Toda classe ou componente do grafo está listado na tabela descritiva.
