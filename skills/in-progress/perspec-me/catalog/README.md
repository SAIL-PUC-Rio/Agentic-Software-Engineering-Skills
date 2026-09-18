# PerSpecML

PerSpecML is a perspective-based approach to specifying ML-enabled systems: 28 tasks organize 60 concerns across five perspectives, connecting business objectives to user experience, infrastructure, models, and data. This reading guide adapts the final catalog by Hugo Villamizar, Marcos Kalinowski, Hélio Lopes, and Daniel Mendez; [sources and attribution](SOURCES.md) identify the material and its coverage.

## When to use it

Use PerSpecML when stakeholders need a shared specification of an ML-enabled system, especially to clarify expectations, examine trade-offs, and identify overlooked requirements. Its published scope focuses on supervised learning.

## Application flow

1. Visit the perspectives below in order.
2. Review each perspective's tasks with the recommended stakeholders.
3. Analyze each concern and its relationships, then decide whether it applies.
4. Specify applicable concerns using the available elicitation prompts and revisit experimental decisions as the project develops.

## Perspectives

- [O — System Objectives](perspectives/system-objectives/): Connect the ML problem to organizational, system, user, and model goals.
- [U — User Experience](perspectives/user-experience/): Define how predictions create value for users and fit their interactions with the system.
- [I — Infrastructure](perspectives/infrastructure/): Plan the services that transport data, run and observe models, and sustain their operation.
- [M — Model](perspectives/model/): Specify model development, evaluation, deployment, and quality constraints beyond predictive accuracy.
- [D — Data](perspectives/data/): Specify the data's origin, meaning, quality, preparation, and use in model evaluation.
