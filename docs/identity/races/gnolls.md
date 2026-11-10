# Gnolls — Race Dossier

[← Race catalog](../races.md) · [Implementation standard](../implementation-standard.md) · [Class catalog](../classes.md)

**Status:** implementation-evaluation specification. The historical appearance is a visual reference; player-rig, equipment and animation compatibility remain unverified. Neutral introduction, either-faction choice and recognizable anatomy adaptations are selected boundaries.

## Identity and historical reference

**Reference:** Vanilla packs including the [Riverpaw in Elwynn](https://warcraft.wiki.gg/wiki/Gnoll), with their early bestial design as the baseline.

**Fantasy:** a hyena-like frontier people with pack relationships, scavenged equipment and individual agency. A playable group needs more depth than a generic enemy faction.

**Equipment proposal:** helmets around muzzle and mane, shoulders on a hunched back, torso armor, weapon/shield grips, robes, boots and cloak attachment. Existing NPC weapons provide a visual starting point, not proof of the whole item system.

**Story proposal:** a specific group's cooperation is earned through events. Existing hostility toward settlements needs consequences and cannot be resolved solely by changing a reaction flag.

**Prototype gate:** compare the same equipment set on a Gnoll and a baseline race, then test melee, ranged and casting actions. This is a useful bestial-biped comparison with the Ogre study, not a certified cheaper conversion. No mandatory pack damage aura is selected.

## Scope of the first implementation spike

The early hyena-like frontier profile with individual agency and recognizable equipment.

Build one representative playable body and a test wardrobe before committing a release roster. The spike must demonstrate arbitrary item presentation and player actions, not just one authored NPC costume. Record the exact reference model/build, required mesh or rig changes and unsupported attachments after inspecting the actual client assets.

## Equipment and body presentation

| Surface / attachment | Required treatment |
| --- | --- |
| Head and mane | Fit muzzle, ears and mane with a documented helmet exception list. |
| Torso and shoulders | Support armor and robes on the hunched body without sliding shoulder anchors. |
| Weapons and back | Test shield grips, sheathing and cape behavior on the bestial silhouette. |

Use the same item identity, slots, stats, enchants and set behavior as other races. Test relevant cloth, leather, mail and plate samples even if race/class combinations are narrowed later. Normally invisible jewelry stays normally invisible. Adaptation must preserve recognizable earned equipment rather than substituting one racial costume.

## Animation, camera and traversal

Melee, ranged and casting all need intentional poses. Social interaction and customization should support a playable community rather than only an enemy attack animation set.

Use standard encounter positioning and reach rules. Inspect doors, lifts, stairs, slopes, swimming, camera occlusion, ground indicators, mount seats and transport interactions. Visual anatomy is not permission for extra attacks, immunity or a different collision advantage.

## Proposed neutral introduction

1. A specific pack seeks a durable settlement after a leadership or resource conflict.
2. The player helps repair relations with local inhabitants through accountability and a shared defense.
3. The individual chooses Alliance or Horde after negotiation; existing hostile packs are not globally converted.

These are proposed story beats, not established lore or an approved quest script. The final introduction needs a quest dependency map, leveling pace, trainers, death/recovery path, travel and service continuity. No prestige rank, raid clear or territorial victory is required. Faction choice determines eligible city standards; later faction-change policy is separate.

## Customization and cultural direction

Mane, muzzle, fur patterns and scavenged adornment should communicate culture beyond a recolored enemy model.

Pack bonds and frontier survival inform narrative. An unconditional pack damage aura or extra pet power is not selected.

Numerical racials and race/class combinations are not selected. Compare any later racial proposal across PvE, PvP and Challenge profiles before adoption; existing races remain complete choices. Evaluate casting, shield, ranged and large-weapon compatibility instead of assuming culture permits only one class fantasy.

## Acceptance scenes

1. Compare identical armor on the candidate and a baseline body, including helmet, cape and long robe.
2. Use ranged/caster actions without a posture that hides the cast source or target.
3. Resolve both faction introductions while retaining meaningful consequences of prior local hostility.
4. Complete login, death, resurrection, equipment change and mount transitions without detached items or lost state.
5. Finish both faction introductions and verify targeting, guards, party rules, services and eligible Warfare standards.
6. Capture the same wardrobe on a baseline playable body and every supported candidate body option; record each visual exception.

## Evaluation handoff

The character-art team owns mesh/rig/attachment evidence; animation owns player-action coverage; narrative owns the neutral introduction and faction choice; gameplay owns slot/racial parity and encounter positioning; QA owns the wardrobe and traversal matrix. These describe required disciplines, not assigned Blizzard staff or measured costs.

Before advancing, provide the asset audit, defect list, supported body options, approved armor exceptions, race/class matrix, starting-experience dependencies and test captures. The dossier is ready to guide that evaluation; production readiness requires the evidence defined in the [implementation standard](../implementation-standard.md).
