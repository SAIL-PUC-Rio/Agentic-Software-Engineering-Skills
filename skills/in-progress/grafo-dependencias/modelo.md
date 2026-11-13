# Modelo de Documento de Grafo de Dependências (`grafo_<fluxo>.md`)

Este arquivo define a estrutura recomendada para documentar fluxos através de mapas de dependências.

---

````markdown
# Mapa de Dependências — <Nome do Fluxo>

<Breve descrição contextual do fluxo: o que ele faz, quais os objetivos de negócio e quais componentes orquestra.>

## Diagrama do Fluxo

![Grafo de Dependências — <Nome do Fluxo>](./images/grafo_<fluxo>.svg)

> **Fonte do grafo:** [`mermaid/grafo_<fluxo>.mmd`](./mermaid/grafo_<fluxo>.mmd)
> *(Caso o ambiente não disponha de Node.js para compilar o SVG via `mmdc`, o bloco ` ```mermaid ` deve substituir a imagem acima como fallback).*

---

## Legenda Arquitetural

| Cor / Forma | Camada / Papel | Descrição |
| :--- | :--- | :--- |
| 🟪 Roxo | **Apresentação / Entrypoint (`pres`)** | Pontos de entrada: rotas de API, controllers, triggers, consumers. |
| 🟦 Azul | **Domínio / Negócio (`core`)** | Regras de negócio, serviços de aplicação, usecases. |
| 🟩 Verde | **Infraestrutura (`infra`)** | Repositórios, clientes HTTP, drivers de banco, adaptadores externos. |
| 🟨 Amarelo (Cápsula) | **Entidades / Dados (`entity`)** | Modelos ORM, entidades de domínio, schemas e tabelas. |
| 🟧 Laranja (Hexágono) | **Fronteira Externa (`boundary`)** | Sistemas de terceiros, microsserviços externos, bancos de dados físicos. |
| ⬜ Cinza | **Bootstrap (`boot`)** | Configurações do app, inicialização e injeção de dependência. |
| Seta contínua | **Chamada Direta** | Execução de método ou função (rótulo = funções chamadas). |
| Linha tracejada | **Uso de Entidade** | Instanciação, consulta ou retorno de dados de entidade. |
| Seta tracejada | **Instanciação dinâmica / Evento** | Criação em tempo de execução ou disparo de callback/evento. |

> **Nota:** Interfaces e contratos implementados são destacados entre parênteses sob o nome do componente. Mecanismos de injeção e factories são abstraídos, conectando a dependência diretamente à implementação correspondente.

---

## Tabela de Componentes

| Componente | Arquivo / Módulo | Interfaces / Tipos | Funções / Métodos Chamados | Responsabilidade no Fluxo |
| :--- | :--- | :--- | :--- | :--- |
| `<NomeComponente1>` | `<caminho/do/arquivo>` | `<(IInterface)> ou —` | `metodoA()`, `metodoB()` | <Explicação objetiva da função deste componente no fluxo.> |
| `<NomeComponente2>` | `<caminho/do/arquivo>` | — | — | <Descrição do modelo ou entidade de dados.> |
| `<ServicoExterno>` | — | — | `POST /endpoint` | <Serviço externo ou sistema terceiro consumido.> |
````
