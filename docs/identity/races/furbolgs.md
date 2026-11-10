# Furbolgs — Race Dossier

[← Race catalog](../races.md) · [Implementation standard](../implementation-standard.md) · [Class catalog](../classes.md)

**Status:** implementation-evaluation specification. The historical appearance is a visual reference; player-rig, equipment and animation compatibility remain unverified. Neutral introduction, either-faction choice and recognizable anatomy adaptations are selected boundaries.

## Identity and historical reference

**Reference:** Vanilla forest peoples and [Timbermaw communities](https://warcraft.wiki.gg/wiki/Timbermaw_furbolg).

**Fantasy:** a broad forest-dwelling people with spiritual and communal life. Preserve bear-like proportions and the older forest aesthetic.

**Equipment proposal:** define fur compression under armor, shoulder placement, weapon grips with paws, and fitting for robes, belts, boots and helmets. Fur volume is a problem to solve, not a reason to hide the torso indefinitely.

**Story proposal:** protecting or restoring a community could support a starting experience. Existing Timbermaw neutrality can inform the origin; the individual chooses either major faction after the introduction.

**Prototype gate:** armored readability in a raid, kneeling, sitting, casting, mount fit and grips. Forest spirituality must not force every class toward one nature kit, and racial utility cannot become an exclusive raid requirement.

## Scope of the first implementation spike

A broad forest people with substantial culture and a workable full-armor presentation.

Build one representative playable body and a test wardrobe before committing a release roster. The spike must demonstrate arbitrary item presentation and player actions, not just one authored NPC costume. Record the exact reference model/build, required mesh or rig changes and unsupported attachments after inspecting the actual client assets.

## Equipment and body presentation

| Surface / attachment | Required treatment |
| --- | --- |
| Fur and torso | Define compression/coverage under chest and robe items instead of leaving the body permanently bare. |
| Paws and weapons | Create correct hand/shield poses and sheathing for allowed equipment. |
| Head, shoulders and feet | Fit the bear-like head and fur volume while retaining recognizable earned items. |

Use the same item identity, slots, stats, enchants and set behavior as other races. Test relevant cloth, leather, mail and plate samples even if race/class combinations are narrowed later. Normally invisible jewelry stays normally invisible. Adaptation must preserve recognizable earned equipment rather than substituting one racial costume.

## Animation, camera and traversal

Sitting, kneeling, casting, swimming, mounted and death actions must work at a practical body scale. Preserve the older forest silhouette through those transitions.

Use standard encounter positioning and reach rules. Inspect doors, lifts, stairs, slopes, swimming, camera occlusion, ground indicators, mount seats and transport interactions. Visual anatomy is not permission for extra attacks, immunity or a different collision advantage.

## Proposed neutral introduction

1. A forest community undertakes a restoration or protection effort that requires outside cooperation.
2. The player resolves a spiritual/community dispute without making every character the same nature archetype.
3. The introduction supports either faction through a personal pledge while other communities retain their independence.

These are proposed story beats, not established lore or an approved quest script. The final introduction needs a quest dependency map, leveling pace, trainers, death/recovery path, travel and service continuity. No prestige rank, raid clear or territorial victory is required. Faction choice determines eligible city standards; later faction-change policy is separate.

## Customization and cultural direction

Fur patterns, facial shapes, markings and ritual adornment can differentiate characters; each supported body option requires its own fitting review.

Forest rites and community stewardship provide stories. No exclusive raid resistance or stronger permanent racial stat package is selected.

Numerical racials and race/class combinations are not selected. Compare any later racial proposal across PvE, PvP and Challenge profiles before adoption; existing races remain complete choices. Evaluate casting, shield, ranged and large-weapon compatibility instead of assuming culture permits only one class fantasy.

## Acceptance scenes

1. Show a full armored caster and shield user with visible chest, gloves, feet and cape.
2. Move through a small interior and crowded raid at the approved footprint.
3. Keep cultural identity coherent for martial, technical and magical class candidates.
4. Complete login, death, resurrection, equipment change and mount transitions without detached items or lost state.
5. Finish both faction introductions and verify targeting, guards, party rules, services and eligible Warfare standards.
6. Capture the same wardrobe on a baseline playable body and every supported candidate body option; record each visual exception.

## Evaluation handoff

The character-art team owns mesh/rig/attachment evidence; animation owns player-action coverage; narrative owns the neutral introduction and faction choice; gameplay owns slot/racial parity and encounter positioning; QA owns the wardrobe and traversal matrix. These describe required disciplines, not assigned Blizzard staff or measured costs.

Before advancing, provide the asset audit, defect list, supported body options, approved armor exceptions, race/class matrix, starting-experience dependencies and test captures. The dossier is ready to guide that evaluation; production readiness requires the evidence defined in the [implementation standard](../implementation-standard.md).

## Selected silhouette and equipment exception policy

Wrist items, cloaks and gloves may be hidden or anatomically varied where needed; document every exception. Footwear is audited per anatomy and has no blanket invisibility approval. Head and weapon presentation are key audit requirements: preserve readable headgear/weapon identity, casting source and the wider class signals in PvP. Gear silhouette alone cannot prove class recognition, so test poses, effects, movement and authoritative nameplate/faction cues too. These requirements revise any earlier all-items-visible assumption; they do not erase slot effects or item ownership.
