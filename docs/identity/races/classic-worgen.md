# Classic Worgen — Race Dossier

[← Race catalog](../races.md) · [Implementation standard](../implementation-standard.md) · [Class catalog](../classes.md)

**Status:** implementation-evaluation specification. The historical appearance is a visual reference; player-rig, equipment and animation compatibility remain unverified. Neutral introduction, either-faction choice and recognizable anatomy adaptations are selected boundaries.

## Identity and historical reference

**Reference:** the original Silverpine/Shadowfang appearance, exemplified by [Sons of Arugal](https://warcraft.wiki.gg/wiki/Son_of_Arugal). Distinguish it from the [later playable Worgen race](https://worldofwarcraft.blizzard.com/en-gb/game/races/worgen).

**Fantasy:** the older feral werewolf profile, with its original proportions and mood. A playable conversion may require a rebuilt rig and missing animations while preserving that appearance; the unmodified NPC mesh is not promised to support all player actions.

**Equipment proposal:** recognizable helmets around the muzzle and ears, chest/robe fitting on the hunched torso, weapon grips with claws, shoulders and foot treatments. A permanent bare-claw outfit does not fulfill the gear-visibility goal.

**Story proposal:** explain retained intelligence, communication and social acceptance through a local story. Neither a mandatory human form nor automatic real-world day/night transformation is selected.

**Prototype gate:** casting, ranged weapons, shields, sitting, mounts, emotes and customization. Racial appearance is separate from class transformations; Worgen membership must not be the only way to access a shapeshifting specialization.

## Scope of the first implementation spike

The older Silverpine/Arugal-associated werewolf appearance, with a player-capable rig preserving its mood.

Build one representative playable body and a test wardrobe before committing a release roster. The spike must demonstrate arbitrary item presentation and player actions, not just one authored NPC costume. Record the exact reference model/build, required mesh or rig changes and unsupported attachments after inspecting the actual client assets.

## Equipment and body presentation

| Surface / attachment | Required treatment |
| --- | --- |
| Muzzle and ears | Adapt closed/open helmets without replacing the head with the later playable model. |
| Hunched torso | Keep chest, robe, shoulder and cape attachments stable across the combat posture. |
| Claws and feet | Fit weapon grips, gloves and foot items while retaining the older silhouette. |

Use the same item identity, slots, stats, enchants and set behavior as other races. Test relevant cloth, leather, mail and plate samples even if race/class combinations are narrowed later. Normally invisible jewelry stays normally invisible. Adaptation must preserve recognizable earned equipment rather than substituting one racial costume.

## Animation, camera and traversal

Complete casting, ranged weapons, shield use, sitting, emotes and mount actions. A missing NPC animation is a work item, not a reason to hide the class action.

Use standard encounter positioning and reach rules. Inspect doors, lifts, stairs, slopes, swimming, camera occlusion, ground indicators, mount seats and transport interactions. Visual anatomy is not permission for extra attacks, immunity or a different collision advantage.

## Proposed neutral introduction

1. A local group seeks reliable control of its curse and a place to live without surrendering its identity.
2. The player proves communication and restraint through a shared crisis and cooperation with outsiders.
3. The introduction offers both faction choices; race appearance and a class's combat transformation remain separate systems.

These are proposed story beats, not established lore or an approved quest script. The final introduction needs a quest dependency map, leveling pace, trainers, death/recovery path, travel and service continuity. No prestige rank, raid clear or territorial victory is required. Faction choice determines eligible city standards; later faction-change policy is separate.

## Customization and cultural direction

Older muzzle, ear, fur and posture choices define the visual target. Human-form availability is an open narrative/art choice, not inherited automatically from the later playable race.

Scent, pack rituals and curse management can inform quests. No automatic player-stealth reveal or required Worgen-only class unlock is selected.

Numerical racials and race/class combinations are not selected. Compare any later racial proposal across PvE, PvP and Challenge profiles before adoption; existing races remain complete choices. Evaluate casting, shield, ranged and large-weapon compatibility instead of assuming culture permits only one class fantasy.

## Acceptance scenes

1. Show cloth, robe and heavy armor on the original-style posture during a full cast cycle.
2. Use bows/firearms and shields without hand or muzzle clipping that obscures the action.
3. Play a non-transforming class and the proposed Moon Predator without a race-exclusive mechanical advantage.
4. Complete login, death, resurrection, equipment change and mount transitions without detached items or lost state.
5. Finish both faction introductions and verify targeting, guards, party rules, services and eligible Warfare standards.
6. Capture the same wardrobe on a baseline playable body and every supported candidate body option; record each visual exception.

## Evaluation handoff

The character-art team owns mesh/rig/attachment evidence; animation owns player-action coverage; narrative owns the neutral introduction and faction choice; gameplay owns slot/racial parity and encounter positioning; QA owns the wardrobe and traversal matrix. These describe required disciplines, not assigned Blizzard staff or measured costs.

Before advancing, provide the asset audit, defect list, supported body options, approved armor exceptions, race/class matrix, starting-experience dependencies and test captures. The dossier is ready to guide that evaluation; production readiness requires the evidence defined in the [implementation standard](../implementation-standard.md).
