# Glossary and decision register

[← Main proposal](../README.md) · [Documentation index](README.md)

## Glossary

| Term | Meaning in this proposal |
| --- | --- |
| Permanent baseline | Accessible equipment power sufficient to start the intended endgame, inside a lasting budget |
| Permanent budget | Approved long-term range of effective equipment power, including effects and interactions |
| Sidegrade | A meaningful alternative within that range, rather than a new permanently stronger tier |
| Contextual progression | Additional power earned and active only inside its approved content scope |
| Content group | The approved raids belonging to one update's progression scope |
| Difficulty scope | A Normal or Veteran boundary that prevents power transfer between the two |
| Context budget | The cap and interaction rules for eligible local effects in one update/difficulty |
| Effect family | A group of bonuses with defined stacking or exclusivity rules |
| Normalization profile | An explicit versioned replacement for effective equipment behavior in an activity |
| Effective power | Real combat capability from stats, procs, synergies, pets, buffs and encounter interactions |
| Heroic dungeon | A fixed-layout, tactical five-player level-60 adventure |
| Challenge Mode | A normalized, fixed-difficulty timed dungeon run with free retries |
| Procedural expedition | An untimed 5–20-player adventure assembled from reviewed modules and encounters |
| Seed | A server-owned generation input, meaningful alongside its generator/content versions |
| Floor snapshot | The committed roster/scaling profile and state for one expedition floor |
| Canonical event ID | The durable identity used to coordinate state and rewards for a world event |
| Reconstruction project | A bounded communal objective restoring a damaged settlement function |
| Civic commendation | Explorer recognition for valid defense or recovery work, without PvP Honor or stats |
| Adventurer | The instanced-PvE participation prestige track |
| Explorer | The discovery and open-world contribution prestige track |
| Honor | The separate PvP recognition identity, not redefined by this proposal |
| Prestige | Recognition and collections earned under stated rules, without permanent combat power |
| Mastery | Demonstrated execution or accomplishment, distinct from an accumulated activity total |
| Claim ledger | Authoritative records preventing duplicate rewards for the same entitlement |
| Idempotent operation | Repeating a request returns the intended result without repeating its side effects |
| Source of truth | Repository Markdown from which the published wiki is generated |

## Status vocabulary

**Commitment** means a selected design boundary. **Prototype** means a proposed starting behavior that needs testing. **Open** means a value or implementation choice remains undecided. None describes shipped gameplay or an official roadmap.

## Decision register

| ID | Decision | Status | Detail |
| --- | --- | --- | --- |
| D01 | Keep level 60 and avoid automatic permanent-budget increases with new content | Commitment | [Progression contract](01-progression-and-raids.md#design-contract) |
| D02 | Permanent items remain usable; additional raid effects have explicit scopes | Commitment | [Raid item model](01-progression-and-raids.md#a-worked-example) |
| D03 | Approved sibling raids share one update/difficulty track with independent entry paths | Commitment | [Shared scope](01-progression-and-raids.md#update-wide-scope-without-a-mandatory-sibling-raid) |
| D04 | Normal and Veteran do not exchange required power or acquisition currency | Commitment | [Difficulties](01-progression-and-raids.md#independent-normal-and-veteran-paths) |
| D05 | Challenge attempts are keyless, normalized and freely repeatable | Commitment | [Challenge rules](activities/challenge-dungeons.md#challenge-mode-rules) |
| D06 | World rewards cannot become exclusive raid prerequisites | Commitment | [Crafting boundaries](activities/world-bosses.md#world-boss-artifacts-and-crafting) |
| D07 | Settlement loss opens communal recovery with essential-service continuity | Commitment | [Recovery](06-invasions-and-reconstruction.md#reconstruction-and-service-continuity) |
| D08 | Expeditions target 5–20 players and a committed 1–5-floor envelope | Requested prototype | [Expedition access](07-procedural-expeditions.md#entry-and-expedition-identity) |
| D09 | Prestige is separate from statistics, economic throughput and skill ratings | Commitment | [Prestige boundaries](08-prestige-ranks.md#rewards-and-progression-boundaries) |
| D10 | Kill scoring starts from native level ×1/×2/×5 before eligibility/repeat rules | Prototype | [Scoring](08-prestige-ranks.md#adventurer-a-simple-starting-score) |
| D11 | New identities need distinct culture/loops and the same power policy | Commitment | [Identity gates](identity/classes.md#development-gates) |
| D12 | Cooperative play anchors meaningful endgame achievement; prestige remains earned | Commitment | [Social design](10-social-design-and-earned-prestige.md) |
| D13 | Loot cadence, shared allowances, rates, caps and economic tuning require pilots | Open | [Reward policies](11-rewards-and-acquisition.md) |
| D14 | Exact rank thresholds, repeat windows and public presentation require evaluation | Open | [Prestige evaluation](08-prestige-ranks.md#evaluation-and-unresolved-choices) |
| D15 | Class/race working names are exploratory and do not define a release roster | Prototype | [Concept catalog](09-regions-races-and-classes.md) |
| D16 | Repository edits automatically publish the wiki after validation | Commitment | [Wiki maintenance](14-wiki-maintenance.md) |

Keep IDs stable when clarifying a decision. A substantial reversal should explain the affected player experience, trade-off and evidence, with a change-history entry. Unsettled numbers must not quietly become fixed rules merely because a wiki page describes them.
