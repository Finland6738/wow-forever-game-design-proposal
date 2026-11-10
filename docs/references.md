# Sources and factual boundaries

[← Main proposal](../README.md) · [Documentation index](README.md)

Last checked: **10 November 2026**. Official pages may change; this register states the limited purpose for which each is cited. The design does not depend on a particular future raid launch date or an unverified interview summary.

## Verified context

| Source | What it supports here | What it does not establish |
| --- | --- | --- |
| Blizzard, [Carve a New Path with World of Warcraft: Forever](https://news.blizzard.com/en-us/article/24302093/carve-a-new-path-with-world-of-warcraft-forever) | Forever is presented as a permanent home with a level 1–60 journey and ongoing additions | A promise that permanent gear power will never increase |
| Blizzard, [World of Warcraft: Forever Now Live!](https://news.blizzard.com/en-us/article/24315820/world-of-warcraft-forever-now-live) | The level-60 setting, account-wide Legacy System and different PvP/ruleset expectations | Our proposed raid scopes, Veteran difficulty, Heroics, Challenge Modes or reward model |
| Blizzard EU forums, [WoW: Forever General Discussion](https://eu.forums.blizzard.com/en/wow/c/wow-forever/wow-forever-general-discussion/360) | A dedicated Forever discussion category exists and is a relevant destination for a future summary | That a thread has been created or that the community endorses this proposal |
| Blizzard, [Playable Races](https://worldofwarcraft.blizzard.com/en-gb/game/races) | A direct roster reference when reviewing how a proposed playable identity differs from existing choices | That an invented working concept is feasible or approved for this setting |
| Blizzard, [Taking Your First Steps in World of Warcraft Classic](https://news.blizzard.com/en-us/article/23317716/taking-your-first-steps-in-world-of-warcraft-classic) | Historical context for major-faction membership and Normal/PvP realm distinctions | That the proposed city flag, bivalent ownership or reward policy already exists or is endorsed |

## Proposal and interpretation

The following are design choices developed in this repository:

- A stable long-term permanent equipment budget.
- Update-wide contextual raid effects with strict difficulty boundaries.
- Separate Normal/Veteran contextual equipment tracks and difficulty-specific permanent ability unlocks.
- A fixed lifetime Rune-stat allowance, with history rather than another rank ladder.
- A globally useful one-slot historical raid repertoire; no automatic Normal unlock from Veteran.
- A preferred ordinary-faction/local-city Warfare prototype, with conditional city variants and a reputation-loss concept whose amount remains open.
- A tactical level-60 Heroic catalog and the proposed Challenge Mode access/reward rules.
- Elite regions, territorial World Bosses, regional PvP objectives and the proposed crafting safeguards.
- Hostile-NPC invasions, settlement recovery, replacement NPC tasks and Explorer civic commendations.
- Procedural portal expeditions for 5–20 players with committed 1–5-floor depth, generated geometry and reviewed encounter pools.
- Separate non-statistical prestige tracks, illustrative kill multipliers and rank tiers, and the role-aware eligibility rules.
- The future-region direction, race candidates, class families and mechanical studies; these are a creative wishlist, not announced additions.
- The conceptual server-side data model, normalization profiles, acceptance cases and pilot sequence.

The proposal defines tactical dungeon play and normalized timed mastery directly, through its own encounter, access and reward rules.

The reasoning that repeated permanent upgrades accumulate power is a design inference. The further claim that players must consequently complete every old raid would be too strong: catch-up systems, alternative sources and resets can prevent that requirement. The proposal favors stable power because of its intended player experience, while acknowledging those alternatives.

Four-to-eight-week raid progression, 30–60-minute territorial benefits and short scenario durations are hypotheses requiring playtests. No staffing, cost, delivery date or completion-rate guarantee is made.

The level ×1/×2/×5 prestige formula is a user-proposed prototype, not a validated performance model. The 5–20-player range and 1–5-floor envelope are requested design parameters; exact scaling, reward rates and feasibility remain unproven. Generated module assemblies can repeat, so the design does not promise a globally unique layout for every run.

The [concept catalog](09-regions-races-and-classes.md) now distinguishes established Warcraft peoples from six secondary original alternatives, and uses English class archetypes with self-contained mechanics. The role/spec proposals, neutral introductions and armor adaptations are design choices, not statements that Blizzard has approved or implemented them. Claims such as “no class has ever done this” or “the most requested class” are not treated as verified facts.

## Historical race references and technical limits

The following references identify the early-era appearances used by the [race catalog](identity/races.md). Community pages are secondary historical indexes; their later expansion sections are not automatically adopted. Blizzard's retrospective Arakkoa and Wrath zone articles support the limited historical distinctions listed below.

| Reference | Limited use in this proposal |
| --- | --- |
| [Ethereals](https://warcraft.wiki.gg/wiki/Ethereal) | TBC-era wrapped-energy people and their Outland appearances |
| [Classic Dustwallow Marsh](https://warcraft.wiki.gg/wiki/Dustwallow_Marsh_%28Classic%29) | Stonemaul/Brackenwall as one Vanilla Ogre connection |
| [Blackfathom](https://warcraft.wiki.gg/wiki/Blackfathom) | Naga represented in a Vanilla dungeon group |
| [Sons of Arugal](https://warcraft.wiki.gg/wiki/Son_of_Arugal) and Blizzard's [Worgen race profile](https://worldofwarcraft.blizzard.com/en-gb/game/races/worgen) | Separate the original Silverpine reference from the later playable race treatment |
| [Razormane tribe](https://warcraft.wiki.gg/wiki/Razormane) | Razormane is a Quilboar tribe represented in Durotar and the Barrens |
| [Kobold Tunneler](https://warcraft.wiki.gg/wiki/Kobold_Tunneler) | Elwynn mine-dwellers as a Vanilla visual reference |
| [Gnolls](https://warcraft.wiki.gg/wiki/Gnoll) | Riverpaw and other early-world packs |
| [Timbermaw Furbolgs](https://warcraft.wiki.gg/wiki/Timbermaw_furbolg) | An existing forest community and neutral-relationship reference |
| Blizzard, [Spires of Arak preview](https://worldofwarcraft.blizzard.com/en-gb/news/15108050/warlords-of-draenor-zone-preview-spires-of-arak) | Distinguishes familiar TBC cursed/flightless Arakkoa from the later winged treatment |
| Blizzard, [Wrath zone guide](https://news.blizzard.com/en-gb/article/23816544/wrath-classic-zone-guide-borean-tundra-and-howling-fjord) | Tuskarr/Kalu'ak presence in Northrend and interaction with both factions |

**No local game-client, mesh, skeleton, UV or equipment-attachment audit has been performed.** Gear-fitting work bands are design estimates based on the proposed anatomies. A cost band is not an implementation measurement, and a model seen holding a weapon does not establish support for arbitrary player items. TBC/Wrath references do not prove those assets are already present in Forever's client.

Pure support, stationary tank dummies, the extra autonomous puppet and the Summoner's no-HP small beings are proposal rules developed from the author's briefs. Their descriptions are not balance results or claims about an existing engine. The [role register](identity/class-roles-and-specializations.md) records selected constraints. The [coverage audit](identity/mechanic-coverage.md) maps the supplied archetypes and thirteen studies; the [implementation standard](identity/implementation-standard.md) distinguishes a specification from engine/production evidence.

## Source handling

Prefer direct official links for claims about announced game behavior. When a source changes, update the affected claim and this register. Secondary reports and unsourced statements in earlier brainstorming are not treated as verified facts.

Use original wording and concise paraphrases. The repository does not reproduce official articles, screenshots or promotional art. Its cover is generated concept art, and its diagrams describe hypothetical systems; see [asset provenance](../assets/README.md).
