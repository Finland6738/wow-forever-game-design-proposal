# Incoming Reports — Design Review

[← Topic directory](../README.md) · [Current decisions](../13-glossary-and-decisions.md) · [Faction Warfare](../activities/faction-warfare.md)

> **Status: under discussion.** This page evaluates two user-provided reports on endgame progression, territorial warfare, Rune statistics and Adventurer abilities. Their recommendations are not adopted gameplay rules. The current power and reward contract remains in force until explicit decisions are made.

## Overall assessment

The strongest shared ideas are predictable recognition for group sessions, varied build choices, a permanent record of accomplishments and collective territorial goals. They can support the project's social direction.

The main conflicts are a permanent stat ceiling that rises each season, globally usable raid-exclusive abilities, conventional vertical raid gearing, and a potentially large new campaign/currency system. Calling an effect small, situational or limited to one slot does not establish that it is horizontal or optional.

## Compatibility matrix

| Proposal | What is useful | Conflict or unresolved risk | Recommended treatment |
| --- | --- | --- | --- |
| Class Masteries | Predictable progression and alternate configurations | Extra XP grind can become required preparation; overlaps Adventurer abilities | Investigate one coherent choice system rather than several overlapping power tracks |
| General Mastery XP after a completed track | Allows preferred play to develop other configurations | Farming the easiest activity could dominate every unlock path | Compare earning rates and preserve bounded, accessible preparation |
| Rune objective history | Readable records of exploration, group work and assistance | Duplicates parts of Explorer/Adventurer prestige | Consider shared objective tracking and distinct presentation, without duplicate grind |
| Seasonal permanent Rune statistics | A visible long-term numerical record | Seasonal caps still raise permanent power; catch-up reduces the gap but does not keep the ceiling fixed | Prefer no-stat recognition or a truly fixed global budget unless the core contract is deliberately revised |
| One selectable Adventurer ability | Bounds simultaneously equipped options | Does not prove equal effective power or prevent an old-raid utility prerequisite | Require explicit scope, acquisition alternatives, budget review and competitive normalization |
| Final-boss deterministic unlock | Recognizes completion without random loot distribution | Globally useful exclusive unlocks can make historical raids mandatory | Decide whether the reward is contextual, an equivalent accessible option, or prestige |
| Higher difficulty unlocks lower-difficulty option | Avoids a compulsory lower-difficulty clear | Can violate independent contextual acquisition if treated as power transfer | Reconcile with the Normal/Veteran contract before adoption |
| Specialization-specific repertoire | Supports distinct class play | Hybrid builds, declared disciplines and repeated clears add complexity | Start with a small prototype and explicit compatibility rules |
| Mentoring | Creates cross-level social contact and revives group opportunities | Can become boosting, low-level-player farming or another weekly obligation | Prefer meaningful learner participation and non-power recognition; test any scaling |
| Provinces, Supplies and fortress sieges | Creates a readable collective campaign and meaningful logistics | Population snowballing, queue imbalance, time-zone coverage and production scope | Start with a bounded territorial pilot if the participation model is selected |
| Separate campaign enrollment and combat consent | Allows contribution without forced combat exposure | Protected event rules on PvP realms are an explicit exception, not merely a flag toggle | Decide the ruleset model before specifying access or transport |
| Faction Points distinct from collective Supplies | Preserves personal recognition even when the faction loses | Adds another currency/rank alongside existing prestige | Decide whether recognition integrates with existing tracks or needs its own presentation |

## Rune statistics and the permanent ceiling

The report proposes +0.50 to each primary statistic per season, reaching +5 after ten seasons, alongside health, mana, hit, critical, speed and regeneration increments. These are illustrative numbers, not validated tuning.

The arithmetic can be small while the design remains vertical: the permitted permanent maximum still rises each season. A returning player also gains a new preparation task. Catch-up helps acquisition, but does not remove that change to the contract.

Three possible directions need a choice: objective history with cosmetic prestige; a finite global stat budget that never grows with updates; or an intentional acceptance of recurring permanent micro-power. The last option requires revising the progression contract, reward matrix, competitive rules and player-facing promise together.

Fractional stat display is a separate implementation problem. Storage precision, derived-stat computation, rounding and actual gameplay effect require investigation. A visible +0.01 is neither proof of a meaningful reward nor proof that the engine applies it correctly.

## A larger ability library is not automatically power-neutral

One equipped ability prevents twenty simultaneous extra buttons. It does not prevent a larger library from offering the strongest answer to more encounters. Mobility, control, threat and immunities can be decisive even when average damage is comparable.

If one old raid is the only source of the best practical answer, the current direct-entry promise is weakened. Decide whether abilities remain local to their update/difficulty, are globally usable within an accessible equivalence model, or stay outside the current concept.

Maestrie and Adventurer abilities also risk becoming two unlock systems for the same kind of choice. Their relationship should be decided before inventing separate XP, interfaces and maintenance requirements. Deterministic acquisition and an archive can be useful without accepting every proposed power rule.

The report's production illustration is 9 classes × 3 specializations × 2 difficulties × 10 seasons = 540 variants under those assumptions. Reusable effect components can help implementation but do not eliminate interaction testing, class identity work or the cost of maintaining every variant.

## Territorial campaign risks

The proposal separates collective Supplies, persistent individual recognition and actual combat consent. That separation is useful. Its protected areas on PvP rulesets would, however, need explicit event access and combat rules while ordinary world behavior remains defined separately.

Adjacent-only attacks create readable fronts, but also need a recovery path if a faction loses every useful foothold. More simultaneous objectives do not alone solve population imbalance; the larger side may simply cover more of them. Evaluate supply-generation rates, limits, siege admission, time windows, alternate-character manipulation and repeated attacks.

Economic benefits require the same scrutiny as combat bonuses. Faster access to essential materials or universally valuable production can make territorial victory a PvE requirement. Guaranteed functional alternatives and sensible supply rates remain necessary.

Solo logistics can let players participate during quiet hours. If it becomes the most efficient way to determine the war, it conflicts with the project's emphasis on cooperative achievements. Compare contribution by activity and group size rather than assuming every source needs the same reward or that larger groups should always earn more per person.

## Decisions requested

1. Rune progression: recognition only, fixed lifetime stat budget, or a deliberate growing permanent ceiling?
2. Combat options: context-scoped, globally usable under equivalence/normalization, or deferred?
3. Faction participation: protected dedicated campaign areas, ruleset-specific open conflict, or retain local objectives for now?

After those answers, resolve the relationship between Maestrie and Adventurer abilities, acquisition/recovery expectations, mentoring rewards, personal faction recognition and the smallest useful territorial pilot. Until then, this page remains a review rather than a feature specification.
