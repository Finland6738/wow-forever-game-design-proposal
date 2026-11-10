# Quilboar / Razormane — Race Dossier

[← Race catalog](../races.md) · [Implementation standard](../implementation-standard.md) · [Class catalog](../classes.md)

**Status:** implementation-evaluation specification. The historical appearance is a visual reference; player-rig, equipment and animation compatibility remain unverified. Neutral introduction, either-faction choice and recognizable anatomy adaptations are selected boundaries.

## Identity and historical reference

**Reference:** Quilboar are the people; **Razormane is a tribe**, not a separate species. The [Razormane reference](https://warcraft.wiki.gg/wiki/Razormane) places them in Durotar and the Barrens.

**Fantasy:** bristled, tusked thornland inhabitants with a serious cultural identity. Architecture, spirituality and materials should support more than a joke or recolor.

**Equipment proposal:** preserve the mane and tusks while fitting helmets, shoulder plates, back items, robes and belts. Decide which bristles deform or need clearance. Different earned items should remain distinguishable on this body.

**Story proposal:** existing conflict with neighbors requires reconciliation, a splinter group or a negotiated relationship. Proximity to a capital is insufficient, and not every hostile clan becomes friendly.

**Prototype gate:** a complete armored caster and melee character using the older visual language. Test whether its anatomy supports the equipment range without losing identity, then develop customization. Introductory diplomacy and racial powers remain open; either-faction choice is selected.

## Scope of the first implementation spike

Bristles, tusks and a coherent thornland culture; Razormane remains a tribal reference.

Build one representative playable body and a test wardrobe before committing a release roster. The spike must demonstrate arbitrary item presentation and player actions, not just one authored NPC costume. Record the exact reference model/build, required mesh or rig changes and unsupported attachments after inspecting the actual client assets.

## Equipment and body presentation

| Surface / attachment | Required treatment |
| --- | --- |
| Mane and cape | Choose deformable bristle/attachment rules so back items remain visible and distinct. |
| Tusks and helmets | Author clearance for headgear rather than hiding every helmet. |
| Chest and limbs | Test armor surfaces, robes, belts, gloves and boots on the older proportions. |

Use the same item identity, slots, stats, enchants and set behavior as other races. Test relevant cloth, leather, mail and plate samples even if race/class combinations are narrowed later. Normally invisible jewelry stays normally invisible. Adaptation must preserve recognizable earned equipment rather than substituting one racial costume.

## Animation, camera and traversal

Weapon, shield and casting actions need to respect tusks and bristles. Heavy armor cannot remove every identifying feature, and the model needs ordinary sitting/death/mount coverage.

Use standard encounter positioning and reach rules. Inspect doors, lifts, stairs, slopes, swimming, camera occlusion, ground indicators, mount seats and transport interactions. Visual anatomy is not permission for extra attacks, immunity or a different collision advantage.

## Proposed neutral introduction

1. A particular community faces a threat to its thornland home and disputes the direction of its leaders.
2. The player participates in a negotiated defense and restitution process with neighboring settlements.
3. Both factions become individual choices after the introduction; existing hostile tribes keep their own politics.

These are proposed story beats, not established lore or an approved quest script. The final introduction needs a quest dependency map, leveling pace, trainers, death/recovery path, travel and service continuity. No prestige rank, raid clear or territorial victory is required. Faction choice determines eligible city standards; later faction-change policy is separate.

## Customization and cultural direction

Bristle patterns, tusks, markings and culturally appropriate ornaments can supply variation beyond skin recolors. Fit every supported option against head/back equipment.

Thornland spirituality and communal craftsmanship provide story hooks. Passive reflected damage or mandatory profession throughput is not selected as a racial.

Numerical racials and race/class combinations are not selected. Compare any later racial proposal across PvE, PvP and Challenge profiles before adoption; existing races remain complete choices. Evaluate casting, shield, ranged and large-weapon compatibility instead of assuming culture permits only one class fantasy.

## Acceptance scenes

1. Equip a large helmet and cape while preserving a readable mane and tusk profile.
2. Cast and use a shield without armor/limb intersections concealing telegraphs.
3. Complete the introduction on both faction paths without rewriting all nearby hostile NPCs as friendly.
4. Complete login, death, resurrection, equipment change and mount transitions without detached items or lost state.
5. Finish both faction introductions and verify targeting, guards, party rules, services and eligible Warfare standards.
6. Capture the same wardrobe on a baseline playable body and every supported candidate body option; record each visual exception.

## Evaluation handoff

The character-art team owns mesh/rig/attachment evidence; animation owns player-action coverage; narrative owns the neutral introduction and faction choice; gameplay owns slot/racial parity and encounter positioning; QA owns the wardrobe and traversal matrix. These describe required disciplines, not assigned Blizzard staff or measured costs.

Before advancing, provide the asset audit, defect list, supported body options, approved armor exceptions, race/class matrix, starting-experience dependencies and test captures. The dossier is ready to guide that evaluation; production readiness requires the evidence defined in the [implementation standard](../implementation-standard.md).
