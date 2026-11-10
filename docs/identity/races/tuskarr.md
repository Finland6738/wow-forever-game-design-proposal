# Tuskarr — Race Dossier

[← Race catalog](../races.md) · [Implementation standard](../implementation-standard.md) · [Class catalog](../classes.md)

**Status:** implementation-evaluation specification. The historical appearance is a visual reference; player-rig, equipment and animation compatibility remain unverified. Neutral introduction, either-faction choice and recognizable anatomy adaptations are selected boundaries.

## Identity and historical reference

**Reference:** Wrath-era Kalu'ak and coastal settlements. Blizzard's [Wrath zone guide](https://news.blizzard.com/en-gb/article/23816544/wrath-classic-zone-guide-borean-tundra-and-howling-fjord) describes their Northrend presence and contact with both factions.

**Fantasy:** a walrus-like seafaring people with communal craft and harsh-coast stories. Retain the older proportions and materials.

**Equipment proposal:** helmets around tusks, chest and robe fitting over the broad torso, shoulders, gloves, boots, shields and cloak movement. Fishing tools and fixed garments do not prove arbitrary weapons or armor work.

**Story proposal:** a visiting crew, rescued settlement or trade mission could introduce them. Wrath-era eligibility does not require importing the full Northrend campaign or its level cap. The origin must support either major-faction choice.

**Prototype gate:** playable scale, indoor movement, mounts, varied equipment and full cast/melee actions. Keep the body recognizable under gear. Coastal identity cannot make fishing or water access an exclusive source of necessary progression.

## Scope of the first implementation spike

The older walrus-like coastal body and a communal seafaring identity.

Build one representative playable body and a test wardrobe before committing a release roster. The spike must demonstrate arbitrary item presentation and player actions, not just one authored NPC costume. Record the exact reference model/build, required mesh or rig changes and unsupported attachments after inspecting the actual client assets.

## Equipment and body presentation

| Surface / attachment | Required treatment |
| --- | --- |
| Tusks and headgear | Fit open and closed helmets around the tusks and face. |
| Broad torso | Keep belts, chest items, robes and shoulder attachments recognizable in motion. |
| Hands, feet and back | Demonstrate weapons beyond fishing tools, shields, boots and moving cloaks. |

Use the same item identity, slots, stats, enchants and set behavior as other races. Test relevant cloth, leather, mail and plate samples even if race/class combinations are narrowed later. Normally invisible jewelry stays normally invisible. Adaptation must preserve recognizable earned equipment rather than substituting one racial costume.

## Animation, camera and traversal

Ordinary cast, melee, ranged, swimming, sitting, transport and mounted actions need testing; practical playable scale must retain the characteristic build.

Use standard encounter positioning and reach rules. Inspect doors, lifts, stairs, slopes, swimming, camera occlusion, ground indicators, mount seats and transport interactions. Visual anatomy is not permission for extra attacks, immunity or a different collision advantage.

## Proposed neutral introduction

1. A visiting crew or displaced coastal community seeks safe harbor and mutual assistance.
2. The player restores a route or settlement service through cooperation with local representatives.
3. The individual joins Alliance or Horde after the introduction, without requiring the full Wrath campaign or its level cap.

These are proposed story beats, not established lore or an approved quest script. The final introduction needs a quest dependency map, leveling pace, trainers, death/recovery path, travel and service continuity. No prestige rank, raid clear or territorial victory is required. Faction choice determines eligible city standards; later faction-change policy is separate.

## Customization and cultural direction

Tusks, whiskers, markings and maritime ornaments provide variation. Review every head option with armor and movement.

Seafaring, hospitality and craft support the setting. Fishing yield or water access cannot become an exclusive route to necessary progression.

Numerical racials and race/class combinations are not selected. Compare any later racial proposal across PvE, PvP and Challenge profiles before adoption; existing races remain complete choices. Evaluate casting, shield, ranged and large-weapon compatibility instead of assuming culture permits only one class fantasy.

## Acceptance scenes

1. Show complete cloth and heavy-armor sets without erasing the broad coastal silhouette.
2. Use shield, staff and ranged actions with correct grips and cast source.
3. Travel inland and use ordinary mounts/services on both faction paths without a lore-based gameplay lock.
4. Complete login, death, resurrection, equipment change and mount transitions without detached items or lost state.
5. Finish both faction introductions and verify targeting, guards, party rules, services and eligible Warfare standards.
6. Capture the same wardrobe on a baseline playable body and every supported candidate body option; record each visual exception.

## Evaluation handoff

The character-art team owns mesh/rig/attachment evidence; animation owns player-action coverage; narrative owns the neutral introduction and faction choice; gameplay owns slot/racial parity and encounter positioning; QA owns the wardrobe and traversal matrix. These describe required disciplines, not assigned Blizzard staff or measured costs.

Before advancing, provide the asset audit, defect list, supported body options, approved armor exceptions, race/class matrix, starting-experience dependencies and test captures. The dossier is ready to guide that evaluation; production readiness requires the evidence defined in the [implementation standard](../implementation-standard.md).

## Selected silhouette and equipment exception policy

Wrist items, cloaks and gloves may be hidden or anatomically varied where needed; document every exception. Footwear is audited per anatomy and has no blanket invisibility approval. Head and weapon presentation are key audit requirements: preserve readable headgear/weapon identity, casting source and the wider class signals in PvP. Gear silhouette alone cannot prove class recognition, so test poses, effects, movement and authoritative nameplate/faction cues too. These requirements revise any earlier all-items-visible assumption; they do not erase slot effects or item ownership.
