# Arakkoa — Race Dossier

[← Race catalog](../races.md) · [Implementation standard](../implementation-standard.md) · [Class catalog](../classes.md)

**Status:** implementation-evaluation specification. The historical appearance is a visual reference; player-rig, equipment and animation compatibility remain unverified. Neutral introduction, either-faction choice and recognizable anatomy adaptations are selected boundaries.

## Identity and historical reference

**Reference:** the original TBC **hunched, flightless** appearance. Blizzard distinguishes these familiar Arakkoa from the later winged treatment in its [Spires of Arak preview](https://worldofwarcraft.blizzard.com/en-gb/news/15108050/warlords-of-draenor-zone-preview-spires-of-arak).

**Fantasy:** avian body language, feathered ritual clothing and a recognizable beaked silhouette. The first concept includes neither unrestricted flight nor a required later upright model.

**Equipment proposal:** test helmets around beak and crest, shoulder/feather overlap, hand grips, taloned feet, robes and a cloak attachment on the hunched back. Permanent species clothing with hidden items would not fulfill the equipment goal.

**Story proposal:** a traveler or small group needs a credible arrival route. The early visual reference does not automatically adopt later stories or political allegiances.

**Prototype gate:** cloth and heavy-armor presentations, weapons and traversal. If fitting arbitrary armor erases the feathered identity, reconsider the approach. Existing NPC appeal can justify research without proving a low-cost playable conversion.

## Scope of the first implementation spike

The original hunched, flightless TBC appearance rather than a later winged model.

Build one representative playable body and a test wardrobe before committing a release roster. The spike must demonstrate arbitrary item presentation and player actions, not just one authored NPC costume. Record the exact reference model/build, required mesh or rig changes and unsupported attachments after inspecting the actual client assets.

## Equipment and body presentation

| Surface / attachment | Required treatment |
| --- | --- |
| Beak and crest | Adapt helmets without hiding the defining head shape. |
| Feathers and shoulders | Resolve shoulder, robe and cape intersections on the hunched back. |
| Talons and grips | Test gloves, feet, ranged weapons and held foci with stable attachment and action poses. |

Use the same item identity, slots, stats, enchants and set behavior as other races. Test relevant cloth, leather, mail and plate samples even if race/class combinations are narrowed later. Normally invisible jewelry stays normally invisible. Adaptation must preserve recognizable earned equipment rather than substituting one racial costume.

## Animation, camera and traversal

Flightless movement, jumps, casting, combat, sitting, mounts and death need complete authored behavior. Feathers do not grant flight or bypass terrain.

Use standard encounter positioning and reach rules. Inspect doors, lifts, stairs, slopes, swimming, camera occlusion, ground indicators, mount seats and transport interactions. Visual anatomy is not permission for extra attacks, immunity or a different collision advantage.

## Proposed neutral introduction

1. A small visiting group arrives through a credible route appropriate to the level-60 setting.
2. The player establishes a refuge and local trust through a shared threat and cultural exchange.
3. Both faction representatives offer individual membership; no later expansion political order is imported automatically.

These are proposed story beats, not established lore or an approved quest script. The final introduction needs a quest dependency map, leveling pace, trainers, death/recovery path, travel and service continuity. No prestige rank, raid clear or territorial victory is required. Faction choice determines eligible city standards; later faction-change policy is separate.

## Customization and cultural direction

Beaks, crests, feather patterns and ritual details must remain compatible with head/back gear. A fixed species costume is not full equipment support.

Ritual scholarship and avian body language inform narrative; flight, immunity and later model forms are not selected racials.

Numerical racials and race/class combinations are not selected. Compare any later racial proposal across PvE, PvP and Challenge profiles before adoption; existing races remain complete choices. Evaluate casting, shield, ranged and large-weapon compatibility instead of assuming culture permits only one class fantasy.

## Acceptance scenes

1. Identify several different chest/robe/helmet sets on the feathered body.
2. Use ranged and heavy-weapon actions without clipping that obscures aim or attack origin.
3. Complete mount/transport and indoor traversal tests while remaining flightless.
4. Complete login, death, resurrection, equipment change and mount transitions without detached items or lost state.
5. Finish both faction introductions and verify targeting, guards, party rules, services and eligible Warfare standards.
6. Capture the same wardrobe on a baseline playable body and every supported candidate body option; record each visual exception.

## Evaluation handoff

The character-art team owns mesh/rig/attachment evidence; animation owns player-action coverage; narrative owns the neutral introduction and faction choice; gameplay owns slot/racial parity and encounter positioning; QA owns the wardrobe and traversal matrix. These describe required disciplines, not assigned Blizzard staff or measured costs.

Before advancing, provide the asset audit, defect list, supported body options, approved armor exceptions, race/class matrix, starting-experience dependencies and test captures. The dossier is ready to guide that evaluation; production readiness requires the evidence defined in the [implementation standard](../implementation-standard.md).
