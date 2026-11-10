# Warfare Models — Factions, Cities and a Bivalent Prototype

[← Faction Warfare](faction-warfare.md) · [City Rewards](warfare-rewards.md) · [PvP](pvp.md)

> **Status: design recommendation.** The bivalent architecture below is the preferred prototype after clarifying that the city flag is voluntarily enabled and disabled through an NPC. The full attack/support and capture-resolution rules still require review before this becomes a complete implementation specification.

## The recommendation

Use **Horde-versus-Alliance territorial conflict as the ordinary channel**, and add **voluntary city rivalry inside designated Warfare areas**. A player who has no active city flag does not become an enemy to allied cities. Two players with different city flags can become opponents locally, including within the same major faction.

This preserves the requested city rivalry without making city choice a permanent global hostility or an unavoidable guild split. It also means the system does not globally change mode when a single person switches a flag: combat legality is resolved for each pair of participants.

## What the Vanilla reference establishes

Blizzard's [Classic introductory guide](https://news.blizzard.com/en-us/article/23317716/taking-your-first-steps-in-world-of-warcraft-classic) describes Horde/Alliance membership and different Normal/PvP realm expectations. It provides historical context for the ordinary channel, not proof that a proposed city mode is impossible or automatically appropriate.

The judgments below are design assessments against this project's goals: cooperative play, readable rules, recognizable identity and persistent territorial activity. Population effects and player reactions remain hypotheses for testing.

## Comparison

| Criterion | Two-faction warfare | Full city-based warfare | Bivalent warfare |
| --- | --- | --- | --- |
| Immediate readability | Strong: the major faction identifies ordinary allies/enemies | More city relations and objective ownership to explain | Major-faction foundation plus one explicitly local exception |
| Compatibility with ordinary faction identity | Strong | Needs a convincing reason for allied-city conflict | Ordinary identity remains; local rivalry is voluntary |
| Participation concentration | Fewer competing pools | More camps can compete for the same players | One common war plus opt-in local rivalry; fragmentation still needs measurement |
| City identity and rewards | Present through patrons, but no actual city combat | Strong direct rivalry and territorial identity | City service can include both identity and voluntary combat |
| Guilds and friend groups | Straightforward within a major faction | Can pressure members to align if hostility is persistent | Neutral/off-city-flag members can remain outside the local rivalry |
| Targeting and support rules | Closest to the ordinary faction relationship | Requires detailed allied-faction hostility and assistance rules | Requires those exceptions only inside the defined area/state |
| Population imbalance | A large major faction can dominate | Dominant cities and major-faction third parties create new imbalance patterns | Adds choices but does not automatically solve either imbalance |
| Development and maintenance | Smallest relative rule expansion | Largest general relationship rewrite | Moderate-to-high cost; credible only with strict area/flag boundaries |
| Best use | A restrained initial territorial system | A deliberately broader political-conflict game | The preferred test for this project's optional city idea |

## Why the voluntary flag changes the assessment

A permanent city allegiance that makes friends enemies everywhere would conflict with the project's social priorities. A local participation flag has a different cost: members can switch off city rivalry for ordinary guild activity, while participants can choose rival sides for the event.

This does not remove every social issue. Inside the Warfare area, two flagged rival-city characters remain opponents even if they share a guild or party. The interface, beneficial effects and objective rewards must honor that choice consistently. Guild membership cannot secretly override the combat rule.

Outside the area, the city flag creates no allied-faction hostility. Ordinary legal opposing-faction PvP remains possible under its own rules. A city pledge must not become an immunity toggle against a traditional opponent.

## Resolve relations per pair

| Participants | Ordinary channel | Added city channel |
| --- | --- | --- |
| Two characters with no city flags | Follow the applicable ordinary PvP rules | None |
| One city-flagged character and one city-neutral allied character | Allied under ordinary faction rules | None; both city flags are required |
| Two characters of the same active city | Ordinary rules still apply | No city hostility |
| Different city flags, both active, inside Warfare | Ordinary rules still apply | Voluntary rivalry, including allied major factions |
| Different city flags outside Warfare | Ordinary rules still apply | No city hostility |
| Opposing major factions where ordinary PvP is legal | Ordinary hostility applies regardless of city flag | The city system cannot remove that permission |

On a Normal ruleset, ordinary faction Warfare capture must communicate and obtain the appropriate PvP consent. City enrollment alone is not a universal ordinary-PvP flag. Exact capture-action flag transitions must be specified before playtesting, so a player is not surprised by an expanded combat state.

## A single territorial record with two levels

The cleanest prototype records an objective's **major-faction owner** and, where relevant, **city stewardship**. It does not maintain two contradictory sovereign owners for the same camp.

For example, an Alliance-controlled fort can be captured by Horde participants. The major-faction owner changes to Horde. City service can then determine which eligible Horde standard is represented. A later rival-city contest may change stewardship while leaving the Horde territorial owner intact.

Neutral city participants still contribute to the ordinary faction objective. Mixed city standards, simultaneous assaults and the claim process need explicit rules; the final hit cannot arbitrarily overwrite the collective result.

Each capture occurrence must declare which change is being resolved and commit its result atomically. Ownership cannot flip twice because two clients report the same boss death. Public UI should distinguish major-faction control, city stewardship and an active contest.

## Three independent states

1. **City service:** which eligible city the character currently serves and its Warfare reputation.
2. **City combat flag:** whether the character participates in local city rivalry; enabled/disabled through the city NPC.
3. **Ordinary PvP state:** the ruleset's normal combat eligibility, unaffected by an attempt to gain city-mode immunity.

Turning off a combat flag is not changing city allegiance. The recommendation is no reputation loss merely for leaving the mode to raid, trade or play with guildmates. The chosen reputation-loss idea applies when changing the served city; its amount remains open.

## Cases that must work before expanding

- A city-neutral healer cannot indefinitely sustain a city combatant while remaining immune to that combat relation. Require the appropriate opt-in to provide that assistance, or clearly disallow the protected interaction; do not assign a city silently.
- Leaving combat, crossing a boundary, relogging or visiting an NPC cannot instantly remove an existing hostile commitment or erase a contested reward claim.
- Mixed-city group buffs and area effects cannot treat a player as friendly for healing but hostile for reward farming at the same time.
- Same-guild capture trading, alt manipulation and deliberately handing a camp back and forth need claim limits and meaningful contribution checks.
- Only event guards/bosses change Warfare state. Ordinary questgivers, town services and unrelated NPCs retain their own rules.
- A dominant city or faction must not make essential PvE resources inaccessible.

## Pilot and decision gate

Start with one Warfare area, a few capture objectives and a limited eligible city set. Test ordinary faction capture first, then enable voluntary city rivalry in the same controlled environment. Compare participation, guild-group continuity, role inclusion, hostility mistakes, support exploits, capture trading and the clarity of ownership.

Retain the city layer if it adds enjoyable choices without making neutral participation confusing or dispersing groups too heavily. If those tests fail, the fallback is two-faction warfare with city service/rewards. No live population data currently justifies claiming that either arrangement is guaranteed to succeed.
