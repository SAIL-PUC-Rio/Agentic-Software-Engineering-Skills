# Regression scenarios specify observed behavior, sourced from cited code and tests

`bdd-scenarios` scenarios specify **agreed** behavior: someone decided it, and the source (a story, spec, or conversation) states it. A pure refactor has no agreed behavior change, so the skill used to stop, and a refactor's evidence pack had no claim that behavior was preserved. We add a **regression (characterization)** kind, `**Kind:** regression` in `/to-spec`, that specifies the **observed** behavior of the existing module so the refactor can be checked against it. The two differ in authority: agreed behavior is a requirement, observed behavior is only a fact about today's code, and a regression scenario never claims the observed behavior is what anyone wants.

This does not turn the skill into a requirements-discovery tool. The source of a regression scenario is the existing code and its existing tests, and each scenario cites the test or code line it comes from. Whatever those do not settle (untested branches, ambiguous or accidental behavior, cases nobody pinned down) stays under `### Unresolved behavior`, and no `Then` is invented. The 12-question gate and the three statuses are unchanged. Scope is the surface the refactor can touch, decided in the spec, not the whole system.

## Consequences

- A regression scenario is a constraint: it must pass before and after the change, and pre-existing tests are not edited to make it pass. If observed behavior is wrong, fixing it is a behavior change that needs an agreed (non-regression) scenario, not a silently edited regression one.
- `/evidence` backs the existing-suite claim with runs on both the base and current revisions, and gives one claim per regression scenario. A regression scenario with no verifying test is never `PASS`.
- Legacy specs, specs without the marker, and non-refactor specs are unaffected.
