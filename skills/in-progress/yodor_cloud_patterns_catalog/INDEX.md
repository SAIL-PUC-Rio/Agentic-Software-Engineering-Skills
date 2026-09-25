# Pattern index

Choose a description, then open only the aspect you need. Grouping follows the book chapters; each identity has one folder. Supporting patterns are marked †.

[Catalog](README.md) · [Inventory and aliases](INVENTORY.md)

## Cloud Applications

- [Cloud Application](patterns/cloud-application/README.md): Design an application around cloud capabilities so it can evolve and use resources effectively.

## Application Architecture

- [Big Ball of Mud](patterns/big-ball-of-mud/README.md): Get early functionality working quickly when the requirements and value of an application are still uncertain.
- [Modular Monolith](patterns/modular-monolith/README.md): Keep one deployable application while organizing its code into maintainable, cohesive modules.
- [Distributed Architecture](patterns/distributed-architecture/README.md): Allow parts of an application to be developed, deployed, and executed independently.

## Cloud-Native Application

- [Cloud-Native Architecture](patterns/cloud-native-architecture/README.md): Structure an application to benefit from the platform on which it runs.
- [Application Package](patterns/application-package/README.md): Choose a language and toolchain that bundle the application with its required dependencies for deployment.
- [Service API](patterns/service-api/README.md): Expose application tasks through a contract that clients can invoke without knowing the implementation.
- [Stateless Application](patterns/stateless-application/README.md): Handle concurrent requests and recover from process failures without keeping essential data inside the application instance.
- [Replicable Application](patterns/replicable-application/README.md): Run equivalent application instances to maintain service through failures and increasing demand.
- [External Configuration](patterns/external-configuration/README.md): Deploy one application build into different environments by supplying settings separately from code.
- [Backend Service](patterns/backend-service/README.md): Share reusable functionality across applications through a separately running service.

## Microservices Architecture

- [Microservices](patterns/microservices/README.md): Organize an application into cooperating modules that teams can develop independently.
- [Domain Microservice](patterns/domain-microservice/README.md): Assign each business capability to a service that encapsulates its logic and exposes a cohesive API.
- [Adapter Microservice](patterns/adapter-microservice/README.md): Reuse existing functionality through a service boundary that fits a microservices application.
- [Dispatcher](patterns/dispatcher/README.md): Give each client channel a suitable interface over business functionality spread across several services.
- [Polyglot Development](patterns/polyglot-development/README.md): Let service teams choose implementation languages suited to their responsibilities.
- [Self-Managed Data Store](patterns/self-managed-data-store/README.md): Give each stateful microservice exclusive control over its persistent data.
- [Service Orchestrator](patterns/service-orchestrator/README.md): Coordinate several service operations behind one API task that performs a larger business activity.

## Microservice Design

- [Model Around the Domain](patterns/model-around-the-domain/README.md): Bring stakeholders together to describe the domain and reveal the capabilities the application must provide.
- [Ubiquitous Language](patterns/ubiquitous-language/README.md) †: Use shared domain vocabulary to reduce misunderstandings between stakeholders and developers.
- [Event Storming](patterns/event-storming/README.md): Explore domain events with stakeholders to uncover behavior, concepts, and candidate boundaries.
- [Domain Event](patterns/domain-event/README.md): Represent a meaningful occurrence in the domain so other parts of the system can respond.
- [Bounded Context](patterns/bounded-context/README.md): Define a boundary within which domain terminology, rules, and concepts have a consistent meaning.
- [Application Services](patterns/application-services/README.md) †: Protect a bounded context’s internals behind operations that serve application use cases.
- [Context Map](patterns/context-map/README.md) †: Make the relationships and boundaries between domain contexts visible to technical and business stakeholders.
- [Aggregate](patterns/aggregate/README.md): Group tightly related domain entities and values so they can be treated as one cohesive concept.
- [Repositories](patterns/repositories/README.md) †: Mediate between aggregates and persistent storage through a domain-oriented collection interface.
- [Domain Service](patterns/domain-service/README.md): Model business operations that belong to the domain but not to one entity or aggregate.
- [Anti-Corruption Layer](patterns/anti-corruption-layer/README.md): Let bounded contexts communicate while protecting their distinct domain models.

## Event-Driven Architecture

- [Event Choreography](patterns/event-choreography/README.md): Let independently interested components react when another component changes.
- [Event](patterns/event/README.md): Represent a component’s change as information that other components can interpret.
- [Reactive Component](patterns/reactive-component/README.md): Build a component that listens for relevant events and chooses an appropriate response.
- [Event Notifier](patterns/event-notifier/README.md): Announce significant component changes as events for interested participants.
- [Event API](patterns/event-api/README.md): Define which events components can expect and how those events are represented.
- [Event Backbone](patterns/event-backbone/README.md): Deliver events to interested components without directly coupling them to their producers.
- [Event Sourcing](patterns/event-sourcing/README.md): Retain an ordered event history to explain and reconstruct how application state developed.

## Cloud-Native Storage

- [Cloud Database](patterns/cloud-database/README.md): Persist application data in storage designed to operate reliably and scale in a cloud environment.
- [Replicated Database](patterns/replicated-database/README.md): Maintain redundant database nodes and copies so storage can match an application’s availability and capacity needs.
- [Configuration Database](patterns/configuration-database/README.md): Keep shared service state consistent and accessible across the nodes of a distributed cloud service.
- [Application Database](patterns/application-database/README.md): Store domain data in a database whose availability, capacity, and access model support a stateless application.
- [Relational Database](patterns/relational-database/README.md): Persist structured data that needs flexible queries and relationships between records.
- [Document Database](patterns/document-database/README.md): Store evolving domain entities as documents when their future structure is not fully known.
- [Key-Value Database](patterns/key-value-database/README.md): Store independent values for fast retrieval through a known key.
- [Graph Database](patterns/graph-database/README.md): Store connected entities so applications can follow their relationships efficiently.
- [Columnar Database](patterns/columnar-database/README.md): Organize analytical data for queries that inspect selected attributes across many records.
- [Data Module](patterns/data-module/README.md): Align cohesive groups of stored data with application modules so both can evolve more independently.
- [Polyglot Persistence](patterns/polyglot-persistence/README.md): Store each data module using the database model that fits its structure and access patterns.
- [Database-as-a-Service](patterns/database-as-a-service/README.md): Obtain an application database through a service that handles much of its provisioning and management.
- [Command Query Responsibility Segregation (CQRS)](patterns/command-query-responsibility-segregation-cqrs/README.md): Separate query and update responsibilities so each can serve its own access and throughput needs.

## Cloud Application Clients

- [Client Application](patterns/client-application/README.md): Provide a user-facing application that accesses services running in the cloud.
- [Browser Application](patterns/browser-application/README.md): Reach users through a web browser without requiring a particular installed client platform.
- [Web Form Application](patterns/web-form-application/README.md): Deliver basic functionality widely through server-generated pages and HTML forms.
- [Single-Page Application](patterns/single-page-application/README.md): Handle browser interaction within one logical page to balance responsiveness and server communication.
- [Micro Frontend](patterns/micro-frontend/README.md): Divide a large frontend into independently owned business features instead of one shared application.
- [Mobile Application](patterns/mobile-application/README.md): Tailor the user experience to mobile devices and their platform-specific capabilities.
- [Command-Line Interface](patterns/command-line-interface/README.md): Enable bulk, repeated, or scheduled operations through commands that invoke application services.
- [Public API](patterns/public-api/README.md): Expose a deliberate interface for third-party applications to use cloud application functionality.
- [Interaction Model](patterns/interaction-model/README.md): Separate user-interaction state and flow from presentation code and business logic.

## Application Migration and Modernization

- [Lift and Shift](patterns/lift-and-shift/README.md): Move an existing application to cloud infrastructure with minimal changes to its implementation.
- [Virtualize the Application](patterns/virtualize-the-application/README.md): Package an installed application in a virtual server that can run in compatible environments.
- [Containerize the Application](patterns/containerize-the-application/README.md): Package an application for denser deployment and portability across compatible container environments.
- [Refactor the Monolith](patterns/refactor-the-monolith/README.md): Improve an existing application’s structure so teams can maintain it and prepare parts for distributed execution.
- [Start Small](patterns/start-small/README.md): Begin cloud adoption with a limited working change that lets the organization learn before expanding.
- [Pave the Road](patterns/pave-the-road/README.md): Make cloud adoption easier through shared infrastructure, examples, training, and development practices.

## Strangling Monoliths

- [Strangle the Monolith](patterns/strangle-the-monolith/README.md): Replace monolithic functionality incrementally with microservices while the existing system continues to provide value.
- [Wrap the Monolith](patterns/wrap-the-monolith/README.md) †: Insulate clients from changing implementations while a monolith and its replacement services coexist.
- [New Features as Microservices](patterns/new-features-as-microservices/README.md): Keep new functionality from expanding the monolith while an incremental migration is under way.
- [Transform Monolith into Microservices](patterns/transform-monolith-into-microservices/README.md): Keep the original system operating while progressively substituting domain-aligned services for its functionality.
- [Hairline Cracks](patterns/hairline-cracks/README.md): Find existing seams in a monolith that can become boundaries for extracted services.
- [Extract Component](patterns/extract-component/README.md): Move loosely connected functionality out of a monolith into an independently deployable component.
- [Macro Service](patterns/macro-service/README.md) †: Extract a larger internally coupled component before refining it into smaller services.
- [Refactor then Extract](patterns/refactor-then-extract/README.md): Reduce internal coupling before moving a portion of the monolith into a service.
- [Replace as Microservice](patterns/replace-as-microservice/README.md): Reimplement tightly coupled functionality as a service when extracting the existing code is impractical.
- [Monolith to Microservice Proxy](patterns/monolith-to-microservice-proxy/README.md): Keep an existing internal interface while redirecting its implementation to a new service.
- [Playback Testing](patterns/playback-testing/README.md): Compare old and new behavior by replaying captured inputs when the original system is not fully understood.
