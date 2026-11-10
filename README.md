# WoW: Forever — A Sustainable Level-60 Endgame

**A community game-design proposal for a fixed long-term power ceiling, lasting raid rewards, city allegiance and a growing world of group adventures.**

![Five adventurers at a crossroads overlooking a forest valley, ruins, a mountain citadel, and a dungeon entrance.](assets/images/a-world-of-parallel-adventures.png)

> **Status: design proposal · v0.5 · 10 November 2026.** This is an independent community project, unaffiliated with Blizzard Entertainment. Everything described as a proposed system is a suggestion for discussion, rather than an announced feature or an implementation of the game.

**[Read the complete GitHub Wiki](https://github.com/Finland6738/wow-forever-game-design/wiki)** · [Documentation index](docs/README.md) · [Questions and discussion](https://github.com/Finland6738/wow-forever-game-design/discussions)

## The proposal in one minute

Keep characters at level 60 and establish an accessible, lasting equipment-power budget. New content should add encounters, builds, stories, collections, and opportunities for mastery without continually raising the minimum permanent power needed to participate.

Raid equipment remains usable throughout the game. Its additional progression bonuses activate only in the **raid group belonging to its content update and in its own difficulty**. Normal and Veteran retain separate contextual equipment tracks. Raids can also teach **permanently usable Adventurer abilities**, with one repertoire option equipped at a time; each difficulty teaches only its own option.

Around that foundation, expand the level-60 endgame with tactical Heroic dungeons, keyless timed Challenge Modes, elite open-world regions, territorial PvP, settlement defense and reconstruction, procedural expeditions, professions, and exploration. Adventurer, Explorer and Honor recognize participation; Gladiator and Challenger identify separate competitive domains. Runes add a fixed-ceiling numerical journey without another rank ladder. Future regions and original playable identities expand the world within the same power policy.

**The revised promise:** a returning player can enter a new raid without a sequential item-level climb through earlier tiers. Historical raids remain worthwhile sources of useful abilities for a chosen build; direct equipment access does not imply an already complete ability collection.

## A world built around playing together

The heart of this proposal is cooperation: finding companions, learning to trust a group, helping a settlement and earning a reputation through shared adventures. Leveling and everyday exploration still have a place, while the most meaningful endgame achievements should reward people who organize, communicate and overcome challenges together.

Keep the rules understandable and let depth come from decisions and teamwork. Approachable entry does not mean automatic completion or identical rewards for every activity. Difficult encounters and prestigious cosmetics should remain earned, recognizable accomplishments. Normal and Veteran offer independent contextual equipment progression. Collecting both of their permanent repertoire options intentionally requires both completions.

[Read the social principles and earned-reward policy →](docs/10-social-design-and-earned-prestige.md)

## Find a topic

The [Wiki Home](https://github.com/Finland6738/wow-forever-game-design/wiki) and sidebar are organized by activity. Use the dedicated page for the topic you want:

| Area | Topics |
| --- | --- |
| PvE — Raids and Dungeons | [Raids](docs/01-progression-and-raids.md) · [World Bosses](docs/activities/world-bosses.md) · [Dungeon Overview](docs/02-dungeons-and-challenges.md) · [Heroic Dungeons (HC)](docs/activities/heroic-dungeons.md) · [Challenge Dungeons](docs/activities/challenge-dungeons.md) · [Procedural Dungeons](docs/07-procedural-expeditions.md) |
| Open World | [Open World](docs/03-world-and-professions.md) · [NPC Invasions and Reconstruction](docs/06-invasions-and-reconstruction.md) · [Exploration and Small-Group Adventures](docs/activities/exploration-and-adventures.md) · [Professions and Crafting](docs/activities/professions.md) · [New Regions](docs/09-regions-races-and-classes.md) |
| PvP and Faction Warfare | [PvP Overview](docs/activities/pvp.md) · [Arenas and Gladiator](docs/activities/arenas.md) · [Open-World PvP](docs/activities/open-world-pvp.md) · [Faction Warfare](docs/activities/faction-warfare.md) · [Warfare Models and Rules](docs/activities/warfare-models.md) · [Warfare Reputation and Cosmetics](docs/activities/warfare-rewards.md) |
| Character and Progression | [Equipment and Progression](docs/systems/equipment-and-progression.md) · [Runes](docs/systems/runes.md) · [Adventurer Abilities](docs/systems/adventurer-abilities.md) · [Recognition and Competitive Standing](docs/08-prestige-ranks.md) · [Races](docs/identity/races.md) · [Classes](docs/identity/classes.md) · [Rewards and Acquisition](docs/11-rewards-and-acquisition.md) |

For technical rules, design philosophy, FAQ, glossary, roadmap and report reviews, see the [complete topic directory](docs/README.md). To propose an improvement, read [CONTRIBUTING.md](CONTRIBUTING.md).

## 1. Why a permanent level cap needs a permanent power policy

A fixed character level does not, by itself, prevent an endless gearing ladder. If every release introduces permanently stronger equipment, effective character power can continue increasing while the level display stays unchanged.

Smaller increases delay this problem. Catch-up systems can also make old tiers unnecessary, so a sequential raid grind is **not an inevitable outcome** of vertical progression. However, that approach still needs recurring replacement gear, resets, or upward retuning. This proposal explores a different contract: keep the long-term power range stable and put most new growth into content, choices, collections, and local progression.

The aim is to preserve the pleasure of earning a useful drop while making a long absence less costly. It is a design preference with real trade-offs, rather than a claim that every player wants horizontal progression.

Blizzard describes Forever as a permanent home with a level 1–60 journey and an account-wide Legacy System. Those are the verified starting points for this discussion. A permanent equipment ceiling and the systems below are **our proposals**, not conclusions about Blizzard's future roadmap. See the [official sources and claim register](docs/references.md).

## 2. Progression channels with different purposes

| Channel | What develops | Boundary |
| --- | --- | --- |
| Permanent equipment | Finite preparation, stat profiles and reviewed sidegrades | No automatic stronger baseline every update |
| Runes | A finite permanent stat allowance and activity history | One fixed lifetime ceiling, no seasonal increases and no Rune rank |
| Contextual raid equipment | Local bonuses in an approved update and difficulty | No transfer of those equipment bonuses to another scope |
| Adventurer Repertoire | Permanently learned raid abilities usable beyond their source | One active or passive option equipped at a time; each difficulty teaches its own option |
| Recognition and collections | Participation, competitive results, city service and earned identity | No hidden combat/yield bonus from a rank |

The permanent power envelope includes the complete fixed Rune allowance. New objectives can vary how that allowance is earned; they do not enlarge it. Rune amounts and acquisition time still require tuning.

A larger repertoire offers useful answers to more encounters. One slot limits simultaneous options but does not prove equal power or remove the incentive to revisit an old raid. This is an intended long-term collection goal, with interaction balance and group access to evaluate.

[Runes →](docs/systems/runes.md) · [Adventurer Abilities →](docs/systems/adventurer-abilities.md)

## 3. Raids: a new challenge without a new permanent gear ladder

![A permanent level-60 baseline feeds three independent raid updates. Each update contains separate Normal and Veteran contextual equipment progression, with no contextual equipment-power transfer between updates or difficulties.](assets/diagrams/raid-progression.svg)

This diagram shows the equipment channel. Permanent Rune development and the one-slot ability repertoire are separate systems.

### Permanent items, contextual bonuses

A raid item keeps its appearance and an approved permanent stat profile. Its additional progression effect has a visible activation scope.

**Illustrative item — Ancient Guardian's Breastplate**

| Property | Proposed behavior |
| --- | --- |
| Required level | 60 |
| Permanent stats | Within the lasting equipment budget; usable outside its raid group |
| Progression scope | All approved raids in **Update A** |
| Difficulty scope | **Normal only** |
| Contextual effect | An encounter-oriented bonus, funded from Update A Normal's capped bonus budget |
| Outside that scope | The contextual effect is inactive; the item remains equipped |

The example uses fictional identifiers. It does not describe an actual item or an announced raid update.

Disabling a set bonus alone would be insufficient if the item's base stats, proc or enchant still exceeded the permanent budget. Every source of effective power needs the same policy, including effects carried across instance boundaries.

### Shared across the raids of one update

The chosen scope is a **content update's raid group**, rather than a separate set for every raid. This reduces fragmented progression, especially when an update contains raids of different lengths.

Shared bonuses create a risk: players may farm the shortest raid before attempting another. Each raid must therefore be independently startable and completable from the permanent baseline, with its own route to the shared progression budget. Avoid exclusive power unlocks in sibling raids, additive per-raid power caps, or an uncapped shared currency. Test whether the easiest raid becomes the practical gearing prerequisite anyway.

### Normal and Veteran equipment tracks are independent

| Rule | Normal | Veteran |
| --- | --- | --- |
| Entry preparation | Accessible permanent baseline | The same accessible permanent baseline |
| Encounter goal | Full raid experience for reasonably prepared casual groups | More demanding execution and coordination for organized guilds |
| Local progression | Update-specific Normal bonuses | Update-specific Veteran bonuses |
| Cross-difficulty effects | Veteran bonuses inactive | Normal bonuses inactive |
| Prestige | Core collections and completion rewards | Additional appearances, titles, mounts and achievements |

Veteran is a proposed difficulty name. It is separate from any Hardcore ruleset. Its intended feel is readable tactical progression: deliberate preparation, important individual responsibilities and coordination without excessive mechanical clutter. A roughly **four-to-eight-week progression journey** for an appropriately prepared target guild is a tuning hypothesis, not a forced waiting period or a guarantee. Skilled groups may finish sooner.

Neither difficulty feeds the other's contextual equipment currency or upgrades. Permanent abilities are a separate reward: Normal teaches its own option and Veteran teaches its own option, without automatically granting Normal. Collecting both can motivate both clears; a shared equipment ladder is still avoided.

### What happens when Update B arrives?

The player keeps their items, collections and Update A progress. Update A bonuses continue working in Update A. They do not work in Update B, which starts its own progression from the same lasting baseline. Old content remains available; the proposal does not require expiring its rewards.

Older raids retain their local progression, stories, collections, profession projects and permanently useful ability unlocks. A player can deliberately seek an old ability for a preferred build. Group organization and reward balance still matter; one useful unlock does not guarantee a healthy population at every hour.

[Read the raid design, trade-offs and safeguards →](docs/01-progression-and-raids.md)

## 4. Heroic dungeons: make the leveling catalog matter at 60

Add level-60 Heroic versions of existing dungeons, gradually. Preserve the leveling versions and their original purpose.

Heroics use five-player groups, familiar layouts and recognizable encounters, with reworked abilities, carefully placed elite packs and additional boss mechanics. Their challenge comes from target priority, crowd control, interrupts, dispels, positioning, threat and resource management.

For example, a pack might contain a healer, a summoner, a guardian and a scout. Groups can control one threat and interrupt another, or focus down a dangerous enemy while stopping reinforcements. Different compositions should have viable solutions. Every pull need not demand the same level of coordination.

Rewards include accessible permanent baseline gear, alternative builds, profession materials, recipes and collections. There is no endlessly increasing difficulty ladder. The long-term ambition is the wider dungeon catalog; the first release should cover a small, representative selection.

## 5. Challenge Modes: practice freely, compete on execution

Challenge Modes are normalized timed dungeon expeditions built around execution, route planning and repeated practice. They use the proposed access and reward rules below.

| Element | Proposed rule |
| --- | --- |
| Access | Level 60, five players, no keystone or consumable entry item |
| Attempts | Unlimited retries and immediate restarts, with narrowly targeted technical safeguards |
| Difficulty | Stable encounter difficulty; no infinitely scaling levels or rotating affixes |
| Equipment | A versioned normalization profile covering stats, effects, enchants and consumables |
| Goals | Bronze, Silver and Gold times, personal records and per-dungeon leaderboards |
| Rewards | Cosmetics, mounts, pets, toys, titles and achievements; no raid-power reward track |
| Group changes | Reform freely between attempts; an active ranked run keeps its starting roster |

Resetting an attempt must not consume an opportunity to play. If someone leaves, the remaining players can replace them and start again. A roster change invalidates the current leaderboard attempt, with an option to continue unranked where technically supported.

Required bosses and explicit encounter objectives prevent trivial bypasses. Major balance changes create a new leaderboard ruleset while preserving previous records in an archive. Permanent medal rewards should remain earnable through a maintained version of the activity.

[Heroic Dungeon design →](docs/activities/heroic-dungeons.md) · [Challenge rules →](docs/activities/challenge-dungeons.md)

## 6. Elite regions and territorial World Bosses

![An elite region offers outer patrols, two parallel routes through cooperative objectives and guardians, and a central territorial World Boss. Optional exploration branches remain separate from the boss route.](assets/diagrams/elite-region.svg)

Create level-60 areas where reaching a World Boss is part of the adventure. Outer patrols and elite camps lead to intermediate objectives, guardians and multiple routes toward a central encounter. Secrets and profession opportunities give the region additional reasons to exist.

Recurring event windows, contribution-based personal eligibility and objectives that require coordination can reduce camping and uncontrolled zerging. These are mitigation ideas, not a complete solution to monopolization, faction imbalance or server-load limits. One region should be tested before expansion.

Bosses may reward artifacts, materials and recipes for specialized crafting. A combat modification must consume an existing effect budget and have a reasonable alternative acquisition path. No World Boss-exclusive advantage should be necessary for a raid or Challenge Mode.

## 7. Territorial conflict, city service and other world activities

The core Warfare activity is a group assault on designated camps or small forts: defeat objective guards and a boss, validate participation, and capture the location. Ordinary questgivers and essential city services are not conquest targets.

City service would let a player choose an eligible standard within their existing major faction, without race restrictions, and earn a separate Warfare reputation. The selected reward direction keeps base banners, cloaks and mounts permanently owned, while city crests/variants require eligible service. Changing the served city loses some departed-city reputation; amount and thresholds remain open. Merely turning the combat flag off is a distinct action.

The preferred bivalent prototype keeps ordinary Horde/Alliance combat and adds voluntary city rivalry inside Warfare areas. Different cities can fight even within the same major faction, but only when both city flags are active. A city-neutral ally remains outside that rivalry. Ordinary legal PvP is evaluated separately, so a city flag never grants immunity from it.

[Faction Warfare →](docs/activities/faction-warfare.md) · [Model comparison →](docs/activities/warfare-models.md) · [City reputation and cosmetics →](docs/activities/warfare-rewards.md)

Other activities include short two- or three-player adventures, class quests, puzzles, stories, professions and collections. Their rewards do not require territorial victory for PvE power. More activities should create more choices rather than a longer compulsory daily checklist.

[Read the world activities →](docs/03-world-and-professions.md)

## 8. NPC invasions: defend a village or help rebuild it

Hostile **NPC factions**, separate from Horde and Alliance players, periodically attack settlements. Players defend objectives, protect residents and repel a commander. A successful defense preserves the village. Defeat leaves a damaged site whose local NPCs withdraw, followed by cooperative resource gathering, construction and recruitment to restore them.

![A settlement cycles from peace through an invasion warning and defense. Victory preserves it; defeat opens reconstruction and NPC restoration before peace returns.](assets/diagrams/settlement-cycle.svg)

Reconstruction uses regional supplies and visible communal projects. NPC recruitment restores approved service roles; players cannot duplicate or control public questgivers. Essential displaced services remain accessible from a fallback camp, and NPC-assisted recovery prevents an unattended village from staying broken indefinitely.

Defense and recovery grant civic recognition within **Explorer prestige**, with no combat bonuses. One event's bounded reward allowance covers both phases, and successful defense should be at least as attractive as deliberately losing and repairing. This must be tested against real reward rates.

[Read the invasion lifecycle and recovery safeguards →](docs/06-invasions-and-reconstruction.md)

## 9. Procedural expeditions: unpredictable routes, finite depth

Portals appearing in the world admit level-60 groups of **5–20 players** into cooperative, untimed expeditions. Authored rooms and corridors assemble into generated layouts; compatible enemy packs, positions and bosses vary as well. Each run commits a depth of **1–5 floors**, with further entrances discovered during play.

Later floors increase challenge within a finite envelope through encounter combinations, bounded health/damage/resistance changes and selected additional abilities. This creates deeper adventures without infinitely scaling levels or a permanent equipment ladder. A finite module library provides variety, rather than a guarantee that every layout is historically unique.

Group size is committed at floor checkpoints so leaving or dying cannot downscale an active boss. Reconnects retain the same expedition and seed; rewards cannot be rerolled or claimed twice. Proposed pilot rewards are modest gold, common crafting materials, cosmetic discoveries and Adventurer prestige. Their exact balance remains open, including safeguards against inflation and easy-seed farming.

[Read generation, scaling and reward options →](docs/07-procedural-expeditions.md)

## 10. Recognition, competitive standing and Rune history

| Identity | What it communicates |
| --- | --- |
| Adventurer | Eligible instanced-PvE participation |
| Explorer | Discovery and meaningful open-world contribution |
| Honor | PvP participation under its separate rules |
| Gladiator | Arena competitive standing; format and rating details remain open |
| Challenger | Validated Challenge Dungeon performance and time-based standings |
| City service | Warfare reputation and cosmetic recognition for a chosen standard |

Runes are not another rank. They show a finite earned stat allowance and its activity history, without an extra prestige ladder. The combat-ability repertoire is likewise distinct from the Adventurer participation score.

The initial Adventurer base-point prototype remains native creature level ×1, ×2 for elites or ×5 for bosses, with role-aware eligibility and repeat rules. Tanking, healing, control and objective assignments count; the final blow does not determine the reward.

Adventurer/Explorer participation tiers use a provisional Wood-to-Legend ladder, reserving Challenger for timed competition. Exact thresholds remain open. Participation totals are not skill ratings, and recognition ranks do not grant statistics or activity-access advantages.

[Recognition rules →](docs/08-prestige-ranks.md) · [Arenas →](docs/activities/arenas.md) · [Rune record →](docs/systems/runes.md)

## 11. New regions and original playable identities

Future updates can add lasting regions, cultures, classes and playable peoples while keeping level 60 and the same permanent power range. They do not need to deliver a new race or class every season, and older regions should keep useful stories, activities and rewards.

The creative direction favors grounded, sometimes ominous fantasy and distinctive new playable identities. Six invented working concepts—Gravemarch, Brineveil, Stonewake, Thornmaw, Briarhide and Veilbound—explore different cultures and silhouettes. Each needs setting, anatomy and narrative review; these names do not identify announced peoples or additions to existing lore.

The class catalog uses invented working names for 18 exploratory identities, including Veilcantor, Cruciblewright, Pactbinder, Aetheredge, Cogwarden and Stillguard. Each entry explains its fantasy, decision loop and group-balance risks. Overlapping ideas are consolidated; a new name alone is insufficient to justify a new class.

Thirteen additional mechanical studies preserve the useful ideas in the brainstorming—forms, swarms, companion empowerment, state consumption, stances, devices, blood resources, parries, ammunition, rune selection and mounted coordination. They are alternatives that may become specializations or talents, rather than 13 more promised classes.

Each concept needs a unique decision loop, readable role, practical animation/pathing plan and the same power constraints as existing choices. New classes must not become mandatory party slots; new races must not supply a stronger permanent racial package. Prestige rank or old raid completion must not be required to unlock them.

[New Regions →](docs/09-regions-races-and-classes.md) · [Races →](docs/identity/races.md) · [Classes →](docs/identity/classes.md)

## 12. A shared technical contract

The technical proposal uses a lasting equipment budget, explicit content scopes, separate difficulty identifiers and versioned normalization profiles. All are conceptual fields; this repository makes no claim about Blizzard's internal architecture.

The server determines whether an effect is active. A tooltip explains that decision, but does not enforce it. Validation must include equipment changes, difficulty changes, login/reconnect, transfers, pets, proc snapshots, consumables and temporary effects.

For Challenge Modes, use approved normalized equipment profiles or accessible template equivalents so legacy item farming cannot become the hidden preparation game. Raw item-level scaling is insufficient. A maintained effect catalog and class/build testing remain necessary.

The same contract covers fixed Rune ceilings, one-slot repertoire state, durable settlements, seeded expeditions, separate recognition ledgers and explicitly resolved Warfare/ordinary-PvP permissions. No new objective silently adds Rune allowance or activates several archived abilities.

[Read the conceptual model and acceptance cases →](docs/04-technical-framework.md)

## 13. Benefits, costs and alternatives

| Approach | Main benefit | Main cost or limitation |
| --- | --- | --- |
| Slow vertical progression | Familiar upgrades and simpler continuity with traditional gearing | Permanent power still rises; catch-up and occasional resets may remain necessary |
| Items usable only in their source raids | Strong isolation of power | Awkward item usability, collection management and weaker attachment outside raids |
| **Permanent gear with scoped progression** | Preserves item ownership and local upgrades while keeping new updates accessible | More rules, normalization work, reward-design pressure and ongoing balance costs |

The equipment model reduces regular obsolescence while local gearing can still feel repetitive. Permanent ability unlocks add a practical old-raid goal, and fixed Runes add a finite numerical journey. Those additions also create acquisition pressure and interaction costs; the design should measure them rather than promise every progression path is interchangeable.

Inventory pressure needs a dedicated bonus collection or archive, clear presets and automatic scope previews. Balance work must detect mandatory sidegrades, not merely keep item levels equal. Development costs require pilots and evidence; reusing dungeon geometry does not make encounter redesign cheap or automatic.

The additions introduce further costs: village consequences can disrupt other players, procedural generation needs authored modules and extensive validation, participation ranks can encourage farming or social exclusion, and new classes/races create long-term art and balance commitments. These risks belong in pilot decisions rather than being hidden behind the word “horizontal.”

## 14. Build evidence before expanding the system

Start by defining the permanent budget and measuring effective power. Then test a small Heroic selection, one update-wide raid group with independent difficulties, and selected normalized Challenge dungeons. Elite regions and territorial PvP follow as separate pilots.

Add one settlement-defense cycle, a limited procedural environment and non-statistical prestige as bounded experiments. New regions and playable identities use separate creative, technical and balance gates; a class wishlist is not a delivery schedule.

Measure preparation time for returning players, the practical need to farm sibling raids or another difficulty, class diversity, reward satisfaction, unwanted activity obligations and maintenance cost. Publish outcomes and revise the design before scaling it.

The critical test is concrete: **can a player with an adequate permanent set enter Update C without gearing through A and B, while still having worthwhile historical ability goals to pursue?**

[Read the pilot sequence and open questions →](docs/05-roadmap-and-evaluation.md)

## Discuss and contribute

The [GitHub Wiki](https://github.com/Finland6738/wow-forever-game-design/wiki) provides the complete reading view, a topic index and detailed navigation. The Markdown files in this repository are the source: changes merged into `main` automatically rebuild the wiki, including new or renamed documentation pages. See [wiki maintenance](docs/14-wiki-maintenance.md) for the publishing rules.

Use [GitHub Discussions](https://github.com/Finland6738/wow-forever-game-design/discussions) for open-ended design debate, [Issues](https://github.com/Finland6738/wow-forever-game-design/issues) for specific problems, and pull requests for proposed edits. Explain the affected player experience, the trade-off and how we could test an improvement.

Three useful starting questions:

1. Would local raid progression feel rewarding if the permanent equipment baseline stayed stable?
2. What would make older raids worth revisiting without making them prerequisites?
3. Which optional activities would keep you playing at 60 without regular item-level increases?

The repository holds the detailed proposal. A short forum introduction can link here once the wording is ready; the [current forum draft](docs/forum-summary.md) has not been posted.

## About the author

I am a software developer and have loved video games since childhood, especially Warcraft, Diablo, StarCraft and World of Warcraft. I started playing WoW in 2004 and spent around fourteen years raiding. Over time, I lost interest as the game moved further from the experience that first drew me in.

My strongest memories are the friendships, unexpected situations and accomplishments shared with other people. The loot and boss strategies mattered, but the people made those experiences last. That is what I hope Forever can preserve from Vanilla: a world where grouping matters, communities recognize effort and success feels earned.

For years I have occasionally shared forum suggestions about what I would improve, add, preserve or remove. This project brings those thoughts together in a form others can examine and challenge. I want to see Forever grow while keeping clear rules, a strong social identity and room for players to pursue more demanding challenges. After so many years of raiding, I would love to see that kind of world thrive for just as long again.

World of Warcraft and related names belong to their respective owners. See [asset provenance](assets/README.md) and the [change history](CHANGELOG.md).
