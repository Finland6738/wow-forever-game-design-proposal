# Raids

[← Main proposal](../README.md) · [Documentation index](README.md) · [Technical rules](04-technical-framework.md)

## Design contract

The permanent equipment-power range does not increase merely because a new content update arrives. Each update adds its own raid progression within that stable foundation. An adequate permanent set is enough to start any new raid, in either proposed difficulty.

This allows a finite initial gearing journey. It does not require every level-60 character to have identical stats or immediately enter every encounter without preparation. Accessible quests, dungeons, world activities and crafting provide routes to the agreed baseline. Those routes stay available as the game grows.

The [prestige ranks](08-prestige-ranks.md), [settlement events](06-invasions-and-reconstruction.md) and [procedural expeditions](07-procedural-expeditions.md) add optional activities and recognition. They do not grant higher permanent budgets, cross-difficulty bonuses or prerequisites for a newly released raid.

The baseline must include more than visible item level: weapon damage, armor, primary and secondary stats, proc effects, enchantments, consumables, relevant profession benefits and any combat-relevant permanent unlocks all affect effective power. A theoretical budget requires encounter and class testing to become a credible balance target.

## Why use permanent gear with contextual bonuses?

Three choices were considered:

| Model | What it preserves | What it sacrifices |
| --- | --- | --- |
| Small permanent upgrades in every update | Traditional excitement and a familiar gearing loop | A lasting ceiling; it may need new catch-up gear or resets |
| Raid items cannot be equipped elsewhere | Very explicit isolation | Usability and attachment to individual items outside their raid |
| Permanent gear plus contextual bonuses | Ownership, appearances, sidegrades and local raid upgrades | Simplicity; more rules and maintenance are required |

The third model is the selected direction. Its success depends on preventing permanent sidegrades from becoming compulsory upgrades in disguise.

## A worked example

Assume Update A contains two fictional raids: **The Fallen Observatory** and **Vault of Cinders**. Both belong to the same progression scope. Each has Normal and Veteran versions.

A player earns a Normal breastplate in the Observatory. It has an approved permanent stat profile and a Normal contextual effect. The effect can activate in either raid of Update A, but only on Normal. The item itself can still be worn in the open world, Veteran, or Update B; only its additional Update A Normal effect becomes inactive there.

When Update B launches, that player retains the item and all previous progress. Update A bonuses remain available in Update A. Update B starts a separate local progression track. A newcomer with an adequate permanent set can join Update B directly.

| Destination | Permanent stats | Update A Normal bonus |
| --- | --- | --- |
| Observatory — Normal | Approved permanent profile | Active |
| Vault — Normal | Approved permanent profile | Active |
| Either Update A raid — Veteran | Approved permanent profile | Inactive |
| Any Update B raid | Approved permanent profile | Inactive |
| Heroic dungeon or open world | Approved permanent profile | Inactive |
| Challenge Mode | Challenge profile replaces effective item behavior | Inactive |

Actual effect magnitude and encounter mechanics are deliberately unspecified. There is no proposed universal percentage that would be safe for every class and raid.

## Update-wide scope without a mandatory sibling raid

Sharing bonuses across an update is the chosen design. It reduces the number of unrelated sets and supports updates containing raids of different lengths. It also makes power earned in one raid useful in its siblings, which can create an incentive to farm the easiest source.

The design cannot eliminate every efficiency preference while preserving that transfer. It can prevent a hard prerequisite and test whether the remaining incentive becomes an unhealthy social requirement.

Proposed safeguards:

1. Every raid has an intended baseline-to-completion path that does not require clearing a sibling raid.
2. Each raid can independently supply the functional contextual options needed for its encounters. No unique required resistance, damage effect or utility comes only from a sibling.
3. The contextual cap belongs to the **update and difficulty**, rather than stacking separate power caps for every raid.
4. Any duplicate-protection or deterministic acquisition route serves that same capped track. It cannot turn extra raids or alt characters into an uncapped acceleration loop.
5. Single-boss raids offer optional ways to obtain equivalent progression or collections, rather than exclusive mandatory unlocks.
6. Content-specific mechanics must remain solvable by execution at the baseline; local gear increases forgiveness and supports reclears.

A shared progression allowance could reduce double farming, but might also penalize people who enjoy several raids or consume progress on an unintended difficulty. The exact loot and lockout arrangement remains open. Pilot the alternatives before committing to a currency or weekly cap.

## Independent Normal and Veteran paths

Normal targets groups who want to experience the complete raid with basic preparation and coordination. Accessibility requires readable mechanics, understandable feedback and recoverable mistakes. It cannot promise a 100% completion rate for all groups.

Veteran targets organized guilds that want more demanding progression with a manageable mechanic set. The desired feel is deliberate tactical coordination, class identity and meaningful personal responsibility. It should be playable using clear built-in information; external tools must not be assumed to solve intentionally opaque mechanics.

The four-to-eight-week progression goal is a cohort-based tuning hypothesis. It depends on player skill, attendance, raid size and schedule. Avoid enforced calendar gates intended solely to make the raid last that long.

Normal and Veteran begin from the same permanent baseline and maintain separate contextual budgets. Veteran may have more involved local equipment combinations and additional prestige rewards. Its stronger or more specialized local effects do not escape into Normal or future updates.

Independence also applies to the less obvious sources of power:

| Potential leak | Required policy |
| --- | --- |
| A Normal trinket has stronger permanent stats | Bring it within the common permanent budget; provide accessible alternatives |
| A shared currency buys Veteran upgrades after Normal farming | Keep power acquisition difficulty-scoped; no cross-difficulty conversion |
| Normal unlocks an encounter-critical recipe | Provide an equivalent accessible path, or keep the result inside Normal |
| A Veteran title or achievement grants combat stats | Prestige rewards have no combat power |
| An account's alts funnel progression into its main | Ownership and transfer rules prevent contextual power funneling |
| A buff is obtained on one difficulty and snapshotted on another | Revalidate and remove incompatible effects on transition |

Players may choose both difficulties for friends or collections. The model should not reward doing both with faster progress toward a single competitive power track.

## Reward satisfaction and local gear resets

A contextual item still helps the group defeat later encounters, experiment with builds and make reclears smoother. Its appearance, ownership and history persist. That is meaningful progression, but it is narrower than a universally stronger item.

The reward program therefore needs strong art, recognizable item identity, memorable encounter interactions and bounded choices. Contextual effects should reinforce mechanics and playstyles rather than provide only interchangeable damage multipliers.

Within each local track, use a capped bonus budget with non-stacking effect families and clear trade-offs. Avoid endless upgrade ranks. Catch-up for a late joiner to an existing update should make the intended local journey reasonable without requiring another update or difficulty.

There is still a perceived reset: players start a new local gearing journey in each update. Feedback must ask whether this feels motivating, repetitive or wasteful. Permanent ownership alone may not resolve that concern.

## Inventory, collection and interface

Long-lived raid scopes could produce dozens of sets. The design should include an archive for earned contextual effects or a dedicated equipment collection, with saved loadouts and retrieval outside combat. The exact item-versus-unlock representation is an implementation decision.

The interface should show the permanent profile, eligible raids, difficulty, active effects, conflicting effect families and the reason an effect is inactive. Before entering content, players should be able to preview their effective loadout without learning internal identifiers.

An archive must not duplicate tradable items or allow multiple copies of a unique effect. Collection convenience is separate from power transfer: appearances may be account-wide while contextual progression remains owned by the intended character and difficulty.

## Keeping old raids worth visiting

Old raids keep their stories, achievements, appearances, profession projects and their own local progression. Permanent availability and social grouping tools can help new groups experience them. Avoid removing collections to manufacture urgency.

There is a tension: if an old recipe provides uniquely optimal combat power, that raid becomes a prerequisite again. Keep comparable functional alternatives accessible elsewhere, and place stronger exclusivity in visual identity and prestige.

No reward model guarantees that every old raid retains enough players. Evaluate participation and newcomer group formation instead of assuming that cosmetics solve this automatically.

## Acceptance questions

- Can a returning player skip several updates and enter the current one with an adequate permanent set?
- Can a Veteran-only guild progress without Normal loot, unlocks or currency?
- Can either sibling raid be completed without the other becoming the expected gearing route?
- Can an older proc, recipe or permanent unlock become the practical best-in-slot prerequisite despite equal item levels?
- Can a player understand an inactive effect and recover their loadout without excessive inventory work?

The [technical acceptance matrix](04-technical-framework.md#acceptance-matrix) turns these questions into concrete cases. The [evaluation plan](05-roadmap-and-evaluation.md) includes the social behavior that a rules engine alone cannot prove.
