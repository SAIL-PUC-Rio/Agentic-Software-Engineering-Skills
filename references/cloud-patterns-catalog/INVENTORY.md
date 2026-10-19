# Source inventory

[Catalog](README.md) · [Reader index](INDEX.md) · [Source policy](SOURCES.md) · [Machine-readable inventory](inventory.json) · [Unmapped website material](WEBSITE-ONLY.md)

The supplied book has **76 list entries, 75 unique identities**: 70 main-list entries plus six supporting-list entries. Repositories occurs in both lists and shares one folder. There are 69 main identities and six supporting identities. Printed i–iv are physical PDF pages 3–6. The chapter/page references below are from the printed book, not inferred from the website.

## Reconciliation decisions

- Circuit Breaker is not in either list. Pilot 1 is Event Sourcing; pilot 2 is Extract Component.
- Repositories appears twice on iv. The main-list question repeats Refactor then Extract; the supporting-list question agrees with the repository discussion on p. 215. Its introduction follows that supporting entry.
- Microservices / Microservice and Self-Managed Data Store / Self-Managed Data Stores differ between the list and chapter headings; list spellings define identity.
- Draft titles can denote narrower or broader predecessors, not exact aliases. Each record explains its mapping; none creates an extra folder.
- The two Strangler Application drafts map to Strangle the Monolith. The two Results Cache drafts remain outside the list scope.

## Pattern records

### cloud-application

**Cloud Application** — chapter 1, Cloud Applications; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 6–15 (PDF 50–59).

Design an application around cloud capabilities so it can evolve and use resources effectively.

Canonical folder: [cloud-application](patterns/cloud-application/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Adoption/Cloud-Centric-Design/).

Aliases / draft labels: Cloud Centric Design.

The draft emphasizes greenfield PaaS design; the book broadens the architecture discussion.

### big-ball-of-mud

**Big Ball of Mud** — chapter 2, Application Architecture; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 22–29 (PDF 66–73).

Get early functionality working quickly when the requirements and value of an application are still uncertain.

Canonical folder: [big-ball-of-mud](patterns/big-ball-of-mud/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### modular-monolith

**Modular Monolith** — chapter 2, Application Architecture; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 29–38 (PDF 73–82).

Keep one deployable application while organizing its code into maintainable, cohesive modules.

Canonical folder: [modular-monolith](patterns/modular-monolith/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### distributed-architecture

**Distributed Architecture** — chapter 2, Application Architecture; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 38–48 (PDF 82–92).

Allow parts of an application to be developed, deployed, and executed independently.

Canonical folder: [distributed-architecture](patterns/distributed-architecture/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### cloud-native-architecture

**Cloud-Native Architecture** — chapter 3, Cloud-Native Application; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 58–62 (PDF 102–106).

Structure an application to benefit from the platform on which it runs.

Canonical folder: [cloud-native-architecture](patterns/cloud-native-architecture/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Native-Application-Considerations/Cloud-Native-Application/).

Aliases / draft labels: Cloud-Native Application.

A short source-repository draft, absent from the homepage navigation.

### application-package

**Application Package** — chapter 3, Cloud-Native Application; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 62–70 (PDF 106–114).

Choose a language and toolchain that bundle the application with its required dependencies for deployment.

Canonical folder: [application-package](patterns/application-package/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Native-Application-Considerations/Application-Runtime/).

Aliases / draft labels: Application Runtime.

Related predecessor, not an exact rename: the book covers packaging, dependencies and deployment; use the book for those aspects.

### service-api

**Service API** — chapter 3, Cloud-Native Application; main pattern.

List entries: main, printed iv (PDF 6). Book: pp. 70–80 (PDF 114–124).

Expose application tasks through a contract that clients can invoke without knowing the implementation.

Canonical folder: [service-api](patterns/service-api/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Native-Application-Considerations/Application-API/).

Aliases / draft labels: Application API.

The draft emphasizes HTTP and REST; the book includes a broader service contract discussion.

### stateless-application

**Stateless Application** — chapter 3, Cloud-Native Application; main pattern.

List entries: main, printed iv (PDF 6). Book: pp. 80–88 (PDF 124–132).

Handle concurrent requests and recover from process failures without keeping essential data inside the application instance.

Canonical folder: [stateless-application](patterns/stateless-application/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Native-Application-Considerations/Stateless-Application/).

Aliases / draft labels: none recorded.

The draft stores session state in a backend service; the book emphasizes client-held session context passed in requests. Both keep durable domain state outside application processes.

### replicable-application

**Replicable Application** — chapter 3, Cloud-Native Application; main pattern.

List entries: main, printed iv (PDF 6). Book: pp. 88–97 (PDF 132–141).

Run equivalent application instances to maintain service through failures and increasing demand.

Canonical folder: [replicable-application](patterns/replicable-application/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: Horizontally Scalable Application.

No matching standalone draft identified in the inspected website repository; book fallback.

### external-configuration

**External Configuration** — chapter 3, Cloud-Native Application; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 97–106 (PDF 141–150).

Deploy one application build into different environments by supplying settings separately from code.

Canonical folder: [external-configuration](patterns/external-configuration/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### backend-service

**Backend Service** — chapter 3, Cloud-Native Application; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 106–112 (PDF 150–156).

Share reusable functionality across applications through a separately running service.

Canonical folder: [backend-service](patterns/backend-service/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Native-Application-Considerations/Backend-Service/).

Aliases / draft labels: none recorded.

Short draft; book supplies the fuller discussion.

### microservices

**Microservices** — chapter 4, Microservices Architecture; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 119–130 (PDF 163–174).

Organize an application into cooperating modules that teams can develop independently.

Canonical folder: [microservices](patterns/microservices/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Microservices/Microservices-Architecture/).

Aliases / draft labels: Microservices Architecture; Microservice.

The book list says Microservices; the chapter heading and contents say Microservice.

### domain-microservice

**Domain Microservice** — chapter 4, Microservices Architecture; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 130–135 (PDF 174–179).

Assign each business capability to a service that encapsulates its logic and exposes a cohesive API.

Canonical folder: [domain-microservice](patterns/domain-microservice/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Microservices/Business-Microservice/).

Aliases / draft labels: Business Microservice; Decompose by Business Capability.

Website filename differs from its Domain Microservice title.

### adapter-microservice

**Adapter Microservice** — chapter 4, Microservices Architecture; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 135–140 (PDF 179–184).

Reuse existing functionality through a service boundary that fits a microservices application.

Canonical folder: [adapter-microservice](patterns/adapter-microservice/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Microservices/Adapter-Microservice/).

Aliases / draft labels: none recorded.

Same core identity.

### dispatcher

**Dispatcher** — chapter 4, Microservices Architecture; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 140–146 (PDF 184–190).

Give each client channel a suitable interface over business functionality spread across several services.

Canonical folder: [dispatcher](patterns/dispatcher/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Microservices/Backend-For-Frontend/).

Aliases / draft labels: Backend for Frontend; BFF; API Gateway; Aggregator.

The draft explicitly calls a BFF a Dispatcher.

### polyglot-development

**Polyglot Development** — chapter 4, Microservices Architecture; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 146–154 (PDF 190–198).

Let service teams choose implementation languages suited to their responsibilities.

Canonical folder: [polyglot-development](patterns/polyglot-development/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Microservices/Polyglot-Development/).

Aliases / draft labels: none recorded.

Same core identity.

### self-managed-data-store

**Self-Managed Data Store** — chapter 4, Microservices Architecture; main pattern.

List entries: main, printed iv (PDF 6). Book: pp. 154–160 (PDF 198–204).

Give each stateful microservice exclusive control over its persistent data.

Canonical folder: [self-managed-data-store](patterns/self-managed-data-store/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: Self-Managed Data Stores; Database per Service.

No matching standalone draft identified in the inspected website repository; book fallback. The chapter heading is plural; retain the singular list identity.

### service-orchestrator

**Service Orchestrator** — chapter 4, Microservices Architecture; main pattern.

List entries: main, printed iv (PDF 6). Book: pp. 160–171 (PDF 204–215).

Coordinate several service operations behind one API task that performs a larger business activity.

Canonical folder: [service-orchestrator](patterns/service-orchestrator/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### model-around-the-domain

**Model Around the Domain** — chapter 5, Microservice Design; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 183–189 (PDF 227–233).

Bring stakeholders together to describe the domain and reveal the capabilities the application must provide.

Canonical folder: [model-around-the-domain](patterns/model-around-the-domain/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Native-Architecture/Microservice-Design/).

Aliases / draft labels: Microservice Design.

Related draft: maps the design process broadly; book provides the named pattern.

### ubiquitous-language

**Ubiquitous Language** — chapter 5, Microservice Design; supporting pattern.

List entries: supporting, printed iv (PDF 6). Book: pp. 186–188 (PDF 230–232).

Use shared domain vocabulary to reduce misunderstandings between stakeholders and developers.

Canonical folder: [ubiquitous-language](patterns/ubiquitous-language/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### event-storming

**Event Storming** — chapter 5, Microservice Design; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 189–193 (PDF 233–237).

Explore domain events with stakeholders to uncover behavior, concepts, and candidate boundaries.

Canonical folder: [event-storming](patterns/event-storming/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Native-Architecture/Identify-Domain-Events/).

Aliases / draft labels: Identify Domain Events.

Despite the filename, the draft describes the Event Storming workshop, not the book pattern Domain Event.

### domain-event

**Domain Event** — chapter 5, Microservice Design; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 193–201 (PDF 237–245).

Represent a meaningful occurrence in the domain so other parts of the system can respond.

Canonical folder: [domain-event](patterns/domain-event/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### bounded-context

**Bounded Context** — chapter 5, Microservice Design; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 201–211 (PDF 245–255).

Define a boundary within which domain terminology, rules, and concepts have a consistent meaning.

Canonical folder: [bounded-context](patterns/bounded-context/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Native-Architecture/Context/).

Aliases / draft labels: none recorded.

Draft defines team boundaries; the book also covers domain semantics and context mapping.

### application-services

**Application Services** — chapter 5, Microservice Design; supporting pattern.

List entries: supporting, printed iv (PDF 6). Book: pp. 205–206 (PDF 249–250).

Protect a bounded context’s internals behind operations that serve application use cases.

Canonical folder: [application-services](patterns/application-services/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### context-map

**Context Map** — chapter 5, Microservice Design; supporting pattern.

List entries: supporting, printed iv (PDF 6). Book: pp. 206–207 (PDF 250–251).

Make the relationships and boundaries between domain contexts visible to technical and business stakeholders.

Canonical folder: [context-map](patterns/context-map/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### aggregate

**Aggregate** — chapter 5, Microservice Design; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 211–222 (PDF 255–266).

Group tightly related domain entities and values so they can be treated as one cohesive concept.

Canonical folder: [aggregate](patterns/aggregate/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Native-Architecture/Identify-Entities-And-Aggregates/).

Aliases / draft labels: Identify Entities and Aggregates.

The draft combines entities and aggregates; this catalog follows the book aggregate identity.

### repositories

**Repositories** — chapter 5, Microservice Design; supporting pattern.

List entries: main, printed iv (PDF 6), supporting, printed iv (PDF 6). Book: pp. 215–215 (PDF 259–259).

Mediate between aggregates and persistent storage through a domain-oriented collection interface.

Canonical folder: [repositories](patterns/repositories/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Native-Architecture/Identify-Repositories-And-Services/).

Aliases / draft labels: Identify Repositories.

Listed twice on book p. iv; the main-list description incorrectly repeats Refactor then Extract. Use the supporting-list description and p. 215.

### domain-service

**Domain Service** — chapter 5, Microservice Design; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 222–229 (PDF 266–273).

Model business operations that belong to the domain but not to one entity or aggregate.

Canonical folder: [domain-service](patterns/domain-service/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Native-Architecture/Services/).

Aliases / draft labels: Services.

Draft uses Services as its title.

### anti-corruption-layer

**Anti-Corruption Layer** — chapter 5, Microservice Design; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 229–233 (PDF 273–277).

Let bounded contexts communicate while protecting their distinct domain models.

Canonical folder: [anti-corruption-layer](patterns/anti-corruption-layer/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### event-choreography

**Event Choreography** — chapter 6, Event-Driven Architecture; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 246–255 (PDF 290–299).

Let independently interested components react when another component changes.

Canonical folder: [event-choreography](patterns/event-choreography/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Event-Based-Architecture/Event-Driven-Architecture/).

Aliases / draft labels: Event-driven Architecture.

The draft presents the architecture broadly; the book names its coordination pattern Event Choreography.

### event

**Event** — chapter 6, Event-Driven Architecture; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 255–260 (PDF 299–304).

Represent a component’s change as information that other components can interpret.

Canonical folder: [event](patterns/event/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### reactive-component

**Reactive Component** — chapter 6, Event-Driven Architecture; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 260–269 (PDF 304–313).

Build a component that listens for relevant events and chooses an appropriate response.

Canonical folder: [reactive-component](patterns/reactive-component/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Event-Based-Architecture/Event-Consumer/).

Aliases / draft labels: Event Consumer.

Related narrower draft: consumption is one role; the book covers components that consume and emit.

### event-notifier

**Event Notifier** — chapter 6, Event-Driven Architecture; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 269–274 (PDF 313–318).

Announce significant component changes as events for interested participants.

Canonical folder: [event-notifier](patterns/event-notifier/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### event-api

**Event API** — chapter 6, Event-Driven Architecture; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 274–279 (PDF 318–323).

Define which events components can expect and how those events are represented.

Canonical folder: [event-api](patterns/event-api/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Event-Based-Architecture/Event-Topic-Registry/).

Aliases / draft labels: Event Topic Registry.

Related narrower draft: a registry publishes contracts, while the book defines the contract itself.

### event-backbone

**Event Backbone** — chapter 6, Event-Driven Architecture; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 279–289 (PDF 323–333).

Deliver events to interested components without directly coupling them to their producers.

Canonical folder: [event-backbone](patterns/event-backbone/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Event-Based-Architecture/Event-Backbone/).

Aliases / draft labels: none recorded.

Same core identity.

### event-sourcing

**Event Sourcing** — chapter 6, Event-Driven Architecture; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 289–298 (PDF 333–342).

Retain an ordered event history to explain and reconstruct how application state developed.

Canonical folder: [event-sourcing](patterns/event-sourcing/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Event-Based-Architecture/Event-Sourcing/).

Aliases / draft labels: none recorded.

The draft uses ride-hailing; the book expands replay, checkpoints, retention and external-system limitations.

### cloud-database

**Cloud Database** — chapter 7, Cloud-Native Storage; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 311–316 (PDF 355–360).

Persist application data in storage designed to operate reliably and scale in a cloud environment.

Canonical folder: [cloud-database](patterns/cloud-database/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Scalable-Store/Scalable-Store/).

Aliases / draft labels: Scalable Store.

Related draft shares externalized persistent state; book expands cloud database topology.

### replicated-database

**Replicated Database** — chapter 7, Cloud-Native Storage; main pattern.

List entries: main, printed iv (PDF 6). Book: pp. 316–323 (PDF 360–367).

Maintain redundant database nodes and copies so storage can match an application’s availability and capacity needs.

Canonical folder: [replicated-database](patterns/replicated-database/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: Distributed Data Store.

No single standalone draft covers the book pattern. Synchronous Replication and Asynchronous Replication are related draft strategies, not additional book-list identities; use the book for the integrated treatment.

### configuration-database

**Configuration Database** — chapter 7, Cloud-Native Storage; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 323–328 (PDF 367–372).

Keep shared service state consistent and accessible across the nodes of a distributed cloud service.

Canonical folder: [configuration-database](patterns/configuration-database/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Scalable-Store/Global-Configs/).

Aliases / draft labels: Distributed Coordination Service; Global Configs.

Global Configs is a three-line predecessor about cross-datacenter configuration; the book develops reliable service-state coordination, consistency and change notifications. The book supplies the missing aspects.

### application-database

**Application Database** — chapter 7, Cloud-Native Storage; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 328–333 (PDF 372–377).

Store domain data in a database whose availability, capacity, and access model support a stateless application.

Canonical folder: [application-database](patterns/application-database/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### relational-database

**Relational Database** — chapter 7, Cloud-Native Storage; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 333–338 (PDF 377–382).

Persist structured data that needs flexible queries and relationships between records.

Canonical folder: [relational-database](patterns/relational-database/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Scalable-Store/Table-Store/).

Aliases / draft labels: Table Store.

The draft explicitly recommends a relational DBMS.

### document-database

**Document Database** — chapter 7, Cloud-Native Storage; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 338–344 (PDF 382–388).

Store evolving domain entities as documents when their future structure is not fully known.

Canonical folder: [document-database](patterns/document-database/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Scalable-Store/Document-Store/).

Aliases / draft labels: Document Store.

Draft emphasizes JSON responses; book addresses evolving document structure more generally.

### key-value-database

**Key-Value Database** — chapter 7, Cloud-Native Storage; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 344–351 (PDF 388–395).

Store independent values for fast retrieval through a known key.

Canonical folder: [key-value-database](patterns/key-value-database/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Scalable-Store/Key-Value-Store/).

Aliases / draft labels: Key-value Store.

Same storage model with a revised name.

### graph-database

**Graph Database** — chapter 7, Cloud-Native Storage; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 351–356 (PDF 395–400).

Store connected entities so applications can follow their relationships efficiently.

Canonical folder: [graph-database](patterns/graph-database/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### columnar-database

**Columnar Database** — chapter 7, Cloud-Native Storage; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 356–366 (PDF 400–410).

Organize analytical data for queries that inspect selected attributes across many records.

Canonical folder: [columnar-database](patterns/columnar-database/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Scalable-Store/Columnar-Store/).

Aliases / draft labels: Columnar Store.

The draft emphasizes fixed or slowly changing schemas and slower writes; the book discusses semi-structured data and groups wide-column stores with column-oriented analytics. Retain this source ambiguity rather than assuming all examples have one layout or workload profile.

### data-module

**Data Module** — chapter 7, Cloud-Native Storage; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 366–374 (PDF 410–418).

Align cohesive groups of stored data with application modules so both can evolve more independently.

Canonical folder: [data-module](patterns/data-module/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### polyglot-persistence

**Polyglot Persistence** — chapter 7, Cloud-Native Storage; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 374–378 (PDF 418–422).

Store each data module using the database model that fits its structure and access patterns.

Canonical folder: [polyglot-persistence](patterns/polyglot-persistence/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Scalable-Store/Polyglot-Persistence/).

Aliases / draft labels: none recorded.

Same core identity.

### database-as-a-service

**Database-as-a-Service** — chapter 7, Cloud-Native Storage; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 378–382 (PDF 422–426).

Obtain an application database through a service that handles much of its provisioning and management.

Canonical folder: [database-as-a-service](patterns/database-as-a-service/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### command-query-responsibility-segregation-cqrs

**Command Query Responsibility Segregation (CQRS)** — chapter 7, Cloud-Native Storage; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 382–392 (PDF 426–436).

Separate query and update responsibilities so each can serve its own access and throughput needs.

Canonical folder: [command-query-responsibility-segregation-cqrs](patterns/command-query-responsibility-segregation-cqrs/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Coexistence-Patterns/Command-Query-Responsibility-Separation/).

Aliases / draft labels: CQRS; Command Query Responsibility Separation.

The website uses Separation rather than Segregation and emphasizes coexistence with a legacy write model. The book emphasizes concurrent queries and updates and presents a two-database design.

### client-application

**Client Application** — chapter 8, Cloud Application Clients; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 406–410 (PDF 450–454).

Provide a user-facing application that accesses services running in the cloud.

Canonical folder: [client-application](patterns/client-application/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### browser-application

**Browser Application** — chapter 8, Cloud Application Clients; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 410–414 (PDF 454–458).

Reach users through a web browser without requiring a particular installed client platform.

Canonical folder: [browser-application](patterns/browser-application/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### web-form-application

**Web Form Application** — chapter 8, Cloud Application Clients; main pattern.

List entries: main, printed iv (PDF 6). Book: pp. 414–421 (PDF 458–465).

Deliver basic functionality widely through server-generated pages and HTML forms.

Canonical folder: [web-form-application](patterns/web-form-application/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Client-Architecture/Web-Application/).

Aliases / draft labels: Web Application.

The draft means server-generated forms; the book separates Browser Application from Web Form Application.

### single-page-application

**Single-Page Application** — chapter 8, Cloud Application Clients; main pattern.

List entries: main, printed iv (PDF 6). Book: pp. 421–426 (PDF 465–470).

Handle browser interaction within one logical page to balance responsiveness and server communication.

Canonical folder: [single-page-application](patterns/single-page-application/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Client-Architecture/Single-Page-Application/).

Aliases / draft labels: Single Page Application.

Hyphenation differs.

### micro-frontend

**Micro Frontend** — chapter 8, Cloud Application Clients; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 426–430 (PDF 470–474).

Divide a large frontend into independently owned business features instead of one shared application.

Canonical folder: [micro-frontend](patterns/micro-frontend/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Client-Architecture/Micro-Frontend/).

Aliases / draft labels: Microapps.

Same core identity.

### mobile-application

**Mobile Application** — chapter 8, Cloud Application Clients; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 430–437 (PDF 474–481).

Tailor the user experience to mobile devices and their platform-specific capabilities.

Canonical folder: [mobile-application](patterns/mobile-application/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Client-Architecture/Native-Mobile-Application/).

Aliases / draft labels: Native Mobile Application.

The book uses a broader title.

### command-line-interface

**Command-Line Interface** — chapter 8, Cloud Application Clients; main pattern.

List entries: main, printed i (PDF 3). Book: pp. 437–443 (PDF 481–487).

Enable bulk, repeated, or scheduled operations through commands that invoke application services.

Canonical folder: [command-line-interface](patterns/command-line-interface/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Client-Architecture/Command-Line-Interface/).

Aliases / draft labels: Command Line Interface.

Hyphenation differs.

### public-api

**Public API** — chapter 8, Cloud Application Clients; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 443–448 (PDF 487–492).

Expose a deliberate interface for third-party applications to use cloud application functionality.

Canonical folder: [public-api](patterns/public-api/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Client-Architecture/Public-API/).

Aliases / draft labels: none recorded.

Same core identity.

### interaction-model

**Interaction Model** — chapter 8, Cloud Application Clients; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 448–454 (PDF 492–498).

Separate user-interaction state and flow from presentation code and business logic.

Canonical folder: [interaction-model](patterns/interaction-model/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Client-Architecture/Interaction-Model/).

Aliases / draft labels: Application Model; Application Controller.

Same core identity.

### lift-and-shift

**Lift and Shift** — chapter 9, Application Migration and Modernization; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 470–475 (PDF 514–519).

Move an existing application to cloud infrastructure with minimal changes to its implementation.

Canonical folder: [lift-and-shift](patterns/lift-and-shift/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Adoption/Lift-and-Shift/).

Aliases / draft labels: Rehost.

Same core identity.

### virtualize-the-application

**Virtualize the Application** — chapter 9, Application Migration and Modernization; main pattern.

List entries: main, printed iv (PDF 6). Book: pp. 475–478 (PDF 519–522).

Package an installed application in a virtual server that can run in compatible environments.

Canonical folder: [virtualize-the-application](patterns/virtualize-the-application/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback.

### containerize-the-application

**Containerize the Application** — chapter 9, Application Migration and Modernization; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 478–484 (PDF 522–528).

Package an application for denser deployment and portability across compatible container environments.

Canonical folder: [containerize-the-application](patterns/containerize-the-application/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Adoption/Containerize-The-Monolith/).

Aliases / draft labels: Containerize the Monolith.

Book title also accommodates applications that are not monoliths.

### refactor-the-monolith

**Refactor the Monolith** — chapter 9, Application Migration and Modernization; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 484–492 (PDF 528–536).

Improve an existing application’s structure so teams can maintain it and prepare parts for distributed execution.

Canonical folder: [refactor-the-monolith](patterns/refactor-the-monolith/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Adoption/Cloud-Refactoring/).

Aliases / draft labels: Cloud Refactoring.

Draft focuses on cloud dependencies; book addresses maintainability and distribution together.

### start-small

**Start Small** — chapter 9, Application Migration and Modernization; main pattern.

List entries: main, printed iv (PDF 6). Book: pp. 492–496 (PDF 536–540).

Begin cloud adoption with a limited working change that lets the organization learn before expanding.

Canonical folder: [start-small](patterns/start-small/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Strangler-Patterns/Start-Small/).

Aliases / draft labels: Gradually Evolve the System; Baby Steps.

Same core identity.

### pave-the-road

**Pave the Road** — chapter 9, Application Migration and Modernization; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 496–503 (PDF 540–547).

Make cloud adoption easier through shared infrastructure, examples, training, and development practices.

Canonical folder: [pave-the-road](patterns/pave-the-road/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Strangler-Patterns/Pave-the-Road/).

Aliases / draft labels: Make Cloud Adoption Easier; Make Cloud Development Easier; Make Microservice Development Easier; Make Microservices Development Easier.

Same core identity.

### strangle-the-monolith

**Strangle the Monolith** — chapter 10, Strangling Monoliths; main pattern.

List entries: main, printed iv (PDF 6). Book: pp. 514–521 (PDF 558–565).

Replace monolithic functionality incrementally with microservices while the existing system continues to provide value.

Canonical folder: [strangle-the-monolith](patterns/strangle-the-monolith/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Strangler-Patterns/Strangler-Application/).

Aliases / draft labels: Strangler Application; Evolve System with Microservices.

Also appears in Cloud-Adoption/Strangler-App; one book identity with two drafts.

### wrap-the-monolith

**Wrap the Monolith** — chapter 10, Strangling Monoliths; supporting pattern.

List entries: supporting, printed iv (PDF 6). Book: pp. 518–518 (PDF 562–562).

Insulate clients from changing implementations while a monolith and its replacement services coexist.

Canonical folder: [wrap-the-monolith](patterns/wrap-the-monolith/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: none recorded.

No matching standalone draft identified in the inspected website repository; book fallback. The book calls this optional scaffolding and notes that it is not developed as a full standalone pattern.

### new-features-as-microservices

**New Features as Microservices** — chapter 10, Strangling Monoliths; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 521–526 (PDF 565–570).

Keep new functionality from expanding the monolith while an incremental migration is under way.

Canonical folder: [new-features-as-microservices](patterns/new-features-as-microservices/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Strangler-Patterns/Microservices-First-Strategy/).

Aliases / draft labels: Microservices First; New Functionality as Microservices; Microservices First Strategy; All new functionality as Microservices.

Draft title names the strategy; book names the migration action.

### transform-monolith-into-microservices

**Transform Monolith into Microservices** — chapter 10, Strangling Monoliths; main pattern.

List entries: main, printed iv (PDF 6). Book: pp. 526–530 (PDF 570–574).

Keep the original system operating while progressively substituting domain-aligned services for its functionality.

Canonical folder: [transform-monolith-into-microservices](patterns/transform-monolith-into-microservices/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: Replace Monolith Functionality with Microservices; Divide and Conquer.

No matching standalone draft identified in the inspected website repository; book fallback.

### hairline-cracks

**Hairline Cracks** — chapter 10, Strangling Monoliths; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 530–535 (PDF 574–579).

Find existing seams in a monolith that can become boundaries for extracted services.

Canonical folder: [hairline-cracks](patterns/hairline-cracks/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Cloud-Adoption/Hairline-Crack/).

Aliases / draft labels: Hairline Crack; Fracture Plane; Design Seams.

Singular draft title, plural book title.

### extract-component

**Extract Component** — chapter 10, Strangling Monoliths; main pattern.

List entries: main, printed ii (PDF 4). Book: pp. 535–542 (PDF 579–586).

Move loosely connected functionality out of a monolith into an independently deployable component.

Canonical folder: [extract-component](patterns/extract-component/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Strangler-Patterns/Extract-Component-and-Add-Fa%C3%A7ade/).

Aliases / draft labels: Extract and Add Façade; Extract Service and Add Façade; Extract Service; Extract Functionality to Microservice; Extract Component and Add Facade; Extract Component and Add Façade.

The draft requires a facade; the book treats it as an option and includes recursive extraction.

### macro-service

**Macro Service** — chapter 10, Strangling Monoliths; supporting pattern.

List entries: supporting, printed iv (PDF 6). Book: pp. 538–542 (PDF 582–586).

Extract a larger internally coupled component before refining it into smaller services.

Canonical folder: [macro-service](patterns/macro-service/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Strangler-Patterns/Macro-then-Micro/).

Aliases / draft labels: Macro then Micro; Divide and Conquer.

The draft presents the strategy; the book names its intermediate service. The draft alias Divide and Conquer is also a book alias for Transform Monolith into Microservices; that shared phrase does not merge their identities.

### refactor-then-extract

**Refactor then Extract** — chapter 10, Strangling Monoliths; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 542–546 (PDF 586–590).

Reduce internal coupling before moving a portion of the monolith into a service.

Canonical folder: [refactor-then-extract](patterns/refactor-then-extract/README.md). Status: complete.

Website: no matching standalone draft identified; use the book.

Aliases / draft labels: Reorganize Monolith then Extract to Microservices.

No matching standalone draft identified in the inspected website repository; book fallback.

### replace-as-microservice

**Replace as Microservice** — chapter 10, Strangling Monoliths; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 546–552 (PDF 590–596).

Reimplement tightly coupled functionality as a service when extracting the existing code is impractical.

Canonical folder: [replace-as-microservice](patterns/replace-as-microservice/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Strangler-Patterns/Replace-as-Microservice/).

Aliases / draft labels: Replace as Service; Reimplement as Service; Reimplement as Microservice; Extract to Service; Replace as a Service.

Same core identity.

### monolith-to-microservice-proxy

**Monolith to Microservice Proxy** — chapter 10, Strangling Monoliths; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 552–556 (PDF 596–600).

Keep an existing internal interface while redirecting its implementation to a new service.

Canonical folder: [monolith-to-microservice-proxy](patterns/monolith-to-microservice-proxy/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Strangler-Patterns/Proxy-Monolith-Components-to-Microservices/).

Aliases / draft labels: Proxy Monolith Components; Proxy Monolith Components to Microservices; Proxy Monolith Service to Microservice.

Book shortens the draft name.

### playback-testing

**Playback Testing** — chapter 10, Strangling Monoliths; main pattern.

List entries: main, printed iii (PDF 5). Book: pp. 556–561 (PDF 600–605).

Compare old and new behavior by replaying captured inputs when the original system is not fully understood.

Canonical folder: [playback-testing](patterns/playback-testing/README.md). Status: complete.

Website: [draft](https://kgb1001001.github.io/cloudadoptionpatterns/Coexistence-Patterns/Playback-Testing/).

Aliases / draft labels: Parallel Run; Validate New Implementation.

Same core identity.
