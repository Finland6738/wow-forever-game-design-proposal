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
| Rune milestone | An authored completion granting a declared unlock/history; no statistical allowance or use counter |
| Rune record | Completion and unlock history, without stat progress or another prestige rank |
| Adventurer Repertoire | Permanent final-boss raid talent collection; one entry active only in raids of its matching difficulty |
| Gladiator | Arena competitive standing, with five selected queue profiles and rating formulas still open |
| Challenger | The timed Challenge Dungeon performance domain, distinct from participation tiers |
| City standard | One active Warfare allegiance inside the character's existing major faction |
| City service | Warfare-specific reputation and cosmetic recognition; separate from ordinary reputation and combat ratings |
| Claim ledger | Authoritative records preventing duplicate rewards for the same entitlement |
| Idempotent operation | Repeating a request returns the intended result without repeating its side effects |
| Source of truth | Repository Markdown from which the published wiki is generated |
| Neutral race origin | A new race's introduction before the player chooses Alliance or Horde |
| Armor adaptation | Anatomy-specific visible fitting that preserves an item's identity, slots and power |
| Pure support | A distinct utility responsibility with low direct damage and no full healer/tank role |
| Specialization | A coherent role/resource branch within a class family, not an additional class by default |
| Summoner reserve | Small beings accumulated and committed through abilities; no individual targetability or HP |
| Puppet Warden | Artificer tank specialization using stationary repairable dummies and commanded positioning |

## Status vocabulary

**Commitment** means a selected design boundary. **Prototype** means a proposed starting behavior that needs testing. **Open** means a value or implementation choice remains undecided. None describes shipped gameplay or an official roadmap.

## Decision register

| ID | Decision | Status | Detail |
| --- | --- | --- | --- |
| D01 | Keep level 60 and avoid automatic permanent-budget increases with new content | Commitment | [Progression contract](01-progression-and-raids.md#design-contract) |
| D02 | Permanent items remain usable; additional raid effects have explicit scopes | Commitment | [Raid item model](01-progression-and-raids.md#a-worked-example) |
| D03 | Approved sibling raids share one update/difficulty track with independent entry paths | Commitment | [Shared scope](01-progression-and-raids.md#update-wide-scope-without-a-mandatory-sibling-raid) |
| D04 | Normal and Veteran equipment/currency and reward-talent activation stay separate; each final boss teaches only its own option | Commitment, revised v0.11 | [Difficulties](01-progression-and-raids.md#independent-normal-and-veteran-paths) |
| D05 | Challenge attempts are keyless, normalized and freely repeatable | Commitment | [Challenge rules](activities/challenge-dungeons.md#challenge-mode-rules) |
| D06 | World rewards cannot become exclusive raid prerequisites | Commitment | [Crafting boundaries](activities/world-bosses.md#world-boss-artifacts-and-crafting) |
| D07 | Settlement loss opens communal recovery with essential-service continuity | Commitment | [Recovery](06-invasions-and-reconstruction.md#reconstruction-and-service-continuity) |
| D08 | Expeditions target 5–20 players and a committed 1–5-floor envelope | Requested prototype | [Expedition access](07-procedural-expeditions.md#entry-and-expedition-identity) |
| D09 | Prestige is separate from statistics, economic throughput and skill ratings | Commitment | [Prestige boundaries](08-prestige-ranks.md#rewards-and-progression-boundaries) |
| D10 | Kill scoring starts from native level ×1/×2/×5 before eligibility/repeat rules | Prototype | [Scoring](08-prestige-ranks.md#adventurer-a-simple-starting-score) |
| D11 | New identities need distinct culture/loops and the same power policy | Commitment | [Identity gates](identity/classes.md#shared-balance-and-development-gates) |
| D12 | Cooperative play anchors meaningful endgame achievement; prestige remains earned | Commitment | [Social design](10-social-design-and-earned-prestige.md) |
| D13 | Loot cadence, shared allowances, rates, caps and economic tuning require pilots | Open | [Reward policies](11-rewards-and-acquisition.md) |
| D14 | Exact rank thresholds, repeat windows and public presentation require evaluation | Open | [Prestige evaluation](08-prestige-ranks.md#evaluation-and-unresolved-choices) |
| D15 | Established race candidates and English class archetypes form an exploratory catalog, not a release roster | Clarified in v0.7 | [Classes](identity/classes.md) · [Races](identity/races.md) |
| D16 | Repository edits automatically publish the wiki after validation | Commitment | [Wiki maintenance](14-wiki-maintenance.md) |
| D17 | Runes grant completion milestones and targeted unlocks, no numerical or usage-based growth | Commitment v0.11; supersedes the prior fixed-stat allowance | [Runes](systems/runes.md) |
| D18 | Historical final-boss talents remain source-exclusive; one slot works only in matching-difficulty raids | Commitment v0.11; supersedes global use | [Raid talents](systems/adventurer-abilities.md) |
| D19 | Veteran does not automatically teach the Normal ability | Commitment | [Ability acquisition](systems/adventurer-abilities.md#working-acquisition-model) |
| D20 | City rivalry allows allied-major-faction opponents only in Warfare areas with both city flags active; ordinary PvP remains separate | Selected constraint of the preferred bivalent prototype | [Warfare models](activities/warfare-models.md) |
| D21 | Permanent base cosmetics, service-qualified city variants; city switch offers preserved standing plus quarantine OR 50% departure-standing loss without a new quarantine | Selected v0.11; duration and claim safeguards open | [City rewards](activities/warfare-rewards.md) |
| D22 | Toggling city combat and changing the city served are distinct operations | Recommended separation for the prototype | [Warfare states](activities/warfare-models.md#three-independent-states) |
| D23 | Every new race permits Alliance or Horde choice after its introduction | Selected boundary | [Neutral origins](identity/races.md#neutral-origins-and-faction-choice) |
| D24 | Recognizable anatomical equipment fitting; wrists/cloaks/gloves may be adapted or hidden, footwear audited individually, head/weapons retain combat readability | Selected v0.11; fitting and recognition unverified | [Armor contract](identity/races.md#equipment-contract-for-every-candidate) |
| D25 | Pure support is distinct; it may replace a DPS in five-player content, while both compositions remain viable | Selected prototype goal; numbers unvalidated | [Group roles](identity/class-roles-and-specializations.md#five-player-compositions) |
| D26 | Artificer tank uses stationary movable dummies with independent HP repaired only by the Artificer; autonomous capstone is extra and temporary | Selected concept; exact budgets open | [Artificer](identity/classes/artificer.md) |
| D27 | Summoner beings follow/order-attack, cannot be selected and have no HP; counterplay targets the caster/effects | Selected constraint | [Summoner](identity/classes/summoner.md#targetability-and-counterplay) |
| D28 | Summoner contains Swarmcaller and Soulbinder DPS trees and Sporekeeper pure support | Selected three-tree direction; kit/numbers require testing | [Summoner trees](identity/classes/summoner.md) |
| D29 | Each candidate class has three Vanilla-style talent trees; hybrid allocation is evaluated at the approved level-60 point budget | Selected structure; individual proposed kits require evaluation | [Implementation contract](identity/implementation-standard.md#class-and-talent-tree-contract) |
| D30 | Moon Predator alternates through an automatic internal combat cycle, independent of world day/night | Selected constraint; phase timing/reset parameters open | [Moon Predator](identity/classes/warden.md#moon-predator) |
| D31 | Work from 51 talent points at level 60 and a 31-point capstone; test hybrid allocations | Selected proposal reference; target-game integration and node grids unvalidated | [Talent contract](identity/implementation-standard.md#class-and-talent-tree-contract) |
| D32 | Support groups trade speed for control/safety; both five-player lineups remain viable | Selected qualitative goal; no numerical speed/wipe targets adopted | [Group compositions](identity/class-roles-and-specializations.md#five-player-compositions) |
| D33 | Loss of the last tank dummy permits brief owner emergency defense and paid reconstruction | Selected behavior; input, timings and costs open | [Artificer recovery](identity/classes/artificer.md#failure-recovery-pvp-and-group-access) |

| D34 | A finite post-60 route earns a role-appropriate default raid-entry preset retained across seasons at a stable budget | Selected; acquisition/representation open | [Raid Entry Preset](systems/raid-entry-preset.md) |
| D35 | Normal targets broad approachability (~70% of relevant raiding guilds); Veteran a more demanding ~30% with 1–2 months of mechanical progression for its reference guild | Design targets, no access quotas or validated clear rates | [Raid tuning](01-progression-and-raids.md) |
| D36 | Group problems permit multiple valid tool combinations; no specific class is mandatory | Selected boundary | [Group tools](identity/group-tools-and-class-identity.md) |
| D37 | Captured objectives show faction/city banners, city-style structures and NPCs; neutral objectives use regional NPC-faction presentation | Selected; asset transitions and mixed claims need prototyping | [Capture appearance](activities/faction-warfare.md#ownership-and-visual-transformation) |
| D38 | Arena queue profiles distinguish 1v1, premade 2v2, solo-assembled 2v2, premade 5v5 and duo+trio 5v5 | Selected; MMR/division formulas and population policy open | [Arenas](activities/arenas.md) |
| D39 | Historical and community recognition rewards mastery, variety and contribution without compulsory daily power chores | Selected boundary | [Recognition](08-prestige-ranks.md) |

Keep IDs stable when clarifying a decision. A substantial reversal should explain the affected player experience, trade-off and evidence, with a change-history entry. Unsettled numbers must not quietly become fixed rules merely because a wiki page describes them.
